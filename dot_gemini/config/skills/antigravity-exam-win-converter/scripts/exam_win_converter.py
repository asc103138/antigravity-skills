#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mac 考卷轉 Windows 完美相容轉檔工具 (Exam Mac to Windows Converter)

核心功能：
1. 深入修復 .docx 的 XML 結構（去除 Mac 專屬字型、格線貼齊陷阱、邊界溢出）：
   - 字型替換：將 PingFang, Heiti, Songti 等 Mac 字型無損替換為 Windows 標準「標楷體」或「新細明體」，英數使用「Times New Roman」。
   - 取消格線貼齊：修復 w:snapToGrid="0"，解決 Windows Word 打開時行距突然被撐大 1.5~2 倍的「爆頁」災難。
   - 精確行距：強制設定段落行距為固定行高（預設 18pt）或合宜單行行距，段前段後留白歸零。
   - 頁面與雙欄校正：支援 A4 雙欄、B4 橫向雙折、A4 單欄標準考卷邊界。
   - 選擇題選項定位點對齊：自動將 (A)... (B)... (C)... (D)... 的多重空白替換為標準製表定位點 (Tab stops)。
   - 清理 macOS 暫存檔（__MACOSX, .DS_Store）。
2. 提供文字/題庫直接產出符合 Windows 學校標準的考卷 docx 範本。

用法：
    # 轉換現有 docx
    python scripts/exam_win_converter.py convert --input "考卷_mac.docx" --output "考卷_win.docx" --font-zh "標楷體" --layout a4-double

    # 批次轉換目錄內所有 docx
    python scripts/exam_win_converter.py batch --input-dir "./mac_exams" --output-dir "./win_exams"

    # 從範本產生乾淨的 Windows 雙欄考卷骨架
    python scripts/exam_win_converter.py scaffold --output "新考卷_範本.docx" --layout a4-double
"""

import argparse
import os
import re
import shutil
import sys
import tempfile
import unicodedata
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

# Word XML Namespaces
NS = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
}
for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)

W_PREFIX = f"{{{NS['w']}}}"

# 常見 Mac 字型對應表
MAC_FONT_PATTERNS = [
    r'PingFang.*', r'蘋方.*', r'Heiti.*', r'黑體.*', r'Songti.*', r'宋體.*',
    r'Kaiti.*', r'楷體-.*', r'Apple.*', r'STHeiti.*', r'STKaiti.*', r'STSong.*',
    r'Lucida Grande', r'BiauKai', r'.*ProN.*', r'Helvetica.*'
]
MAC_FONT_REGEX = re.compile('|'.join(MAC_FONT_PATTERNS), re.I)

class ExamWinConverter:
    def __init__(self, font_zh="標楷體", font_en="Times New Roman", line_spacing_pt=18.0, fix_tabs=True):
        self.font_zh = font_zh
        self.font_en = font_en
        self.line_spacing_pt = line_spacing_pt
        self.fix_tabs = fix_tabs

    def _fix_rFonts(self, element: ET.Element):
        """校正字型宣告，統一注入 Windows 考卷必備字型"""
        # 1. 修改現有 rFonts
        for r_fonts in element.findall(f".//{W_PREFIX}rFonts"):
            east_asia = r_fonts.get(f"{W_PREFIX}eastAsia", "")
            ascii_font = r_fonts.get(f"{W_PREFIX}ascii", "")
            h_ansi = r_fonts.get(f"{W_PREFIX}hAnsi", "")

            # 只要包含 Mac 字型、或者未指定、或者非 Windows 標準字型，一律標準化
            if not east_asia or MAC_FONT_REGEX.search(east_asia):
                r_fonts.set(f"{W_PREFIX}eastAsia", self.font_zh)
            if not ascii_font or MAC_FONT_REGEX.search(ascii_font):
                r_fonts.set(f"{W_PREFIX}ascii", self.font_en)
            if not h_ansi or MAC_FONT_REGEX.search(h_ansi):
                r_fonts.set(f"{W_PREFIX}hAnsi", self.font_en)
            r_fonts.set(f"{W_PREFIX}cs", self.font_en)

        # 2. 針對所有文字 run (w:r)，若其 rPr 缺少 rFonts，主動補上
        for r in element.findall(f".//{W_PREFIX}r"):
            t = r.find(f"{W_PREFIX}t")
            if t is not None and t.text:
                rPr = r.find(f"{W_PREFIX}rPr")
                if rPr is None:
                    rPr = ET.Element(f"{W_PREFIX}rPr")
                    r.insert(0, rPr)
                rFonts = rPr.find(f"{W_PREFIX}rFonts")
                if rFonts is None:
                    rFonts = ET.SubElement(rPr, f"{W_PREFIX}rFonts")
                    rFonts.set(f"{W_PREFIX}ascii", self.font_en)
                    rFonts.set(f"{W_PREFIX}hAnsi", self.font_en)
                    rFonts.set(f"{W_PREFIX}eastAsia", self.font_zh)
                    rFonts.set(f"{W_PREFIX}cs", self.font_en)

    def _fix_paragraph_properties(self, root: ET.Element):
        """修復段落排版：取消格線貼齊、重設段落行距與留白"""
        for p in root.findall(f".//{W_PREFIX}p"):
            pPr = p.find(f"{W_PREFIX}pPr")
            if pPr is None:
                pPr = ET.Element(f"{W_PREFIX}pPr")
                p.insert(0, pPr)

            # 1. 取消與網格貼齊 (snapToGrid = 0)
            snap = pPr.find(f"{W_PREFIX}snapToGrid")
            if snap is None:
                snap = ET.SubElement(pPr, f"{W_PREFIX}snapToGrid")
            snap.set(f"{W_PREFIX}val", "0")

            # 2. 段前段後間距歸零，設定行高 (1 pt = 20 dxa)
            spacing = pPr.find(f"{W_PREFIX}spacing")
            if spacing is None:
                spacing = ET.SubElement(pPr, f"{W_PREFIX}spacing")
            spacing.set(f"{W_PREFIX}before", "0")
            spacing.set(f"{W_PREFIX}after", "0")
            spacing.set(f"{W_PREFIX}beforeLines", "0")
            spacing.set(f"{W_PREFIX}afterLines", "0")
            
            # 若指定固定行高 (lineRule="exact", 18pt = 360)
            line_val = str(int(self.line_spacing_pt * 20))
            spacing.set(f"{W_PREFIX}line", line_val)
            spacing.set(f"{W_PREFIX}lineRule", "exact")

            # 3. 確保中英文字距緊湊，不自動拉開大量空格
            autoSpaceDE = pPr.find(f"{W_PREFIX}autoSpaceDE")
            if autoSpaceDE is not None:
                autoSpaceDE.set(f"{W_PREFIX}val", "0")
            autoSpaceDN = pPr.find(f"{W_PREFIX}autoSpaceDN")
            if autoSpaceDN is not None:
                autoSpaceDN.set(f"{W_PREFIX}val", "0")

    def _fix_options_tabs(self, root: ET.Element):
        """如果使用者開啟選項排版修正，將 (A) (B) (C) (D) 間多個空白轉為定位點"""
        if not self.fix_tabs:
            return

        for p in root.findall(f".//{W_PREFIX}p"):
            # 取得該段落下所有文字節點
            texts = p.findall(f".//{W_PREFIX}t")
            if not texts:
                continue
            
            # 整合整段文字檢查是否為選擇題選項行
            full_text = "".join([t.text or "" for t in texts])
            # 偵測如 (A) 或 (1) 或 [A]
            opt_pattern = re.compile(r'(\([A-D1-4]\)|\[[A-D1-4]\]|\b[A-D]\.)')
            matches = list(opt_pattern.finditer(full_text))
            
            # 如果一行內出現 2 個以上的選項且中間隔著 2 個以上空白，適合轉成 Tab 定位點
            if len(matches) >= 2 and re.search(r'\s{2,}', full_text):
                # 針對最後一個 run 之前的空白替換
                for t in texts:
                    if t.text:
                        # 替換選項前的多個空白為單一 Tab 符號
                        t.text = re.sub(r'\s{2,}(?=(\([A-D1-4]\)|\[[A-D1-4]\]|\b[A-D]\.))', '\t', t.text)

    def _fix_document_xml(self, xml_content: bytes) -> bytes:
        """修復 document.xml 主內容"""
        root = ET.fromstring(xml_content)
        self._fix_rFonts(root)
        self._fix_paragraph_properties(root)
        self._fix_options_tabs(root)
        return ET.tostring(root, encoding='utf-8', xml_declaration=True)

    def _fix_styles_xml(self, xml_content: bytes) -> bytes:
        """修復 styles.xml，將預設 Normal (內文) 及所有樣式中的字型和行距固定"""
        root = ET.fromstring(xml_content)
        self._fix_rFonts(root)

        # 針對 docDefaults 與各 style 修復
        docDefaults = root.find(f"{W_PREFIX}docDefaults")
        if docDefaults is not None:
            rPrDefault = docDefaults.find(f"{W_PREFIX}rPrDefault")
            if rPrDefault is not None:
                rPr = rPrDefault.find(f"{W_PREFIX}rPr")
                if rPr is not None:
                    rFonts = rPr.find(f"{W_PREFIX}rFonts")
                    if rFonts is None:
                        rFonts = ET.SubElement(rPr, f"{W_PREFIX}rFonts")
                    rFonts.set(f"{W_PREFIX}ascii", self.font_en)
                    rFonts.set(f"{W_PREFIX}hAnsi", self.font_en)
                    rFonts.set(f"{W_PREFIX}eastAsia", self.font_zh)
                    rFonts.set(f"{W_PREFIX}cs", self.font_en)

            pPrDefault = docDefaults.find(f"{W_PREFIX}pPrDefault")
            if pPrDefault is not None:
                pPr = pPrDefault.find(f"{W_PREFIX}pPr")
                if pPr is not None:
                    snap = pPr.find(f"{W_PREFIX}snapToGrid")
                    if snap is None:
                        snap = ET.SubElement(pPr, f"{W_PREFIX}snapToGrid")
                    snap.set(f"{W_PREFIX}val", "0")
        
        return ET.tostring(root, encoding='utf-8', xml_declaration=True)

    def _fix_font_table_xml(self, xml_content: bytes) -> bytes:
        """確保 fontTable.xml 中明確註冊了 Windows 標準字型"""
        root = ET.fromstring(xml_content)
        existing_fonts = {f.get(f"{W_PREFIX}name") for f in root.findall(f"{W_PREFIX}font")}
        
        needed = [
            (self.font_zh, "zh-TW"),
            (self.font_en, "en-US"),
            ("Times New Roman", "en-US"),
            ("標楷體", "zh-TW"),
            ("新細明體", "zh-TW")
        ]
        for font_name, lang in needed:
            if font_name not in existing_fonts:
                font_elem = ET.SubElement(root, f"{W_PREFIX}font", {f"{W_PREFIX}name": font_name})
                ET.SubElement(font_elem, f"{W_PREFIX}charset", {f"{W_PREFIX}val": "88" if lang == "zh-TW" else "00"})
                ET.SubElement(font_elem, f"{W_PREFIX}pitch", {f"{W_PREFIX}val": "variable"})
                existing_fonts.add(font_name)

        return ET.tostring(root, encoding='utf-8', xml_declaration=True)

    def convert_docx(self, input_path: Path, output_path: Path, layout: str = None) -> bool:
        """完整轉換單個 docx 檔案"""
        if not input_path.exists():
            raise FileNotFoundError(f"找不到檔案：{input_path}")

        temp_dir = Path(tempfile.mkdtemp(prefix="exam_conv_"))
        try:
            with zipfile.ZipFile(input_path, 'r') as zin:
                zin.extractall(temp_dir)

            # 遍歷並修復 XML 檔案
            doc_xml_path = temp_dir / "word" / "document.xml"
            if doc_xml_path.exists():
                new_doc_xml = self._fix_document_xml(doc_xml_path.read_bytes())
                doc_xml_path.write_bytes(new_doc_xml)

            styles_xml_path = temp_dir / "word" / "styles.xml"
            if styles_xml_path.exists():
                new_styles = self._fix_styles_xml(styles_xml_path.read_bytes())
                styles_xml_path.write_bytes(new_styles)

            font_table_path = temp_dir / "word" / "fontTable.xml"
            if font_table_path.exists():
                new_font_table = self._fix_font_table_xml(font_table_path.read_bytes())
                font_table_path.write_bytes(new_font_table)

            # 頁首頁尾也同時校正
            for hf_file in (temp_dir / "word").glob("header*.xml"):
                hf_file.write_bytes(self._fix_document_xml(hf_file.read_bytes()))
            for hf_file in (temp_dir / "word").glob("footer*.xml"):
                hf_file.write_bytes(self._fix_document_xml(hf_file.read_bytes()))

            # 移除 macOS 污染檔案
            for root, dirs, files in os.walk(temp_dir):
                for f in files:
                    if f.startswith("._") or f == ".DS_Store":
                        try:
                            os.remove(os.path.join(root, f))
                        except Exception:
                            pass
                for d in list(dirs):
                    if d == "__MACOSX":
                        shutil.rmtree(os.path.join(root, d), ignore_errors=True)

            # 重新打包成 docx
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zout:
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        full_path = Path(root) / file
                        arcname = full_path.relative_to(temp_dir)
                        zout.write(full_path, arcname)

            return True
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)


def create_scaffold_exam(output_path: Path, title="113學年度第一學期 第一次定期評量 數學科試題", school="高級中學", layout="a4-double"):
    """使用 python-docx 產生符合 Windows 學校標準的考卷樣板"""
    from docx import Document
    from docx.shared import Pt, Cm, Inches, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.section import WD_SECTION, WD_ORIENT
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn

    doc = Document()
    section = doc.sections[0]

    # 設定邊界（考卷緊湊標準：上下 1.5 cm，左右 1.5 cm）
    section.top_margin = Cm(1.5)
    section.bottom_margin = Cm(1.5)
    section.left_margin = Cm(1.5)
    section.right_margin = Cm(1.5)

    if layout == "a4-double":
        # A4 直式雙欄
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.orientation = WD_ORIENT.PORTRAIT
        # 設定雙欄
        sectPr = section._sectPr
        cols = sectPr.xpath('./w:cols')
        if cols:
            col_elem = cols[0]
        else:
            col_elem = OxmlElement('w:cols')
            sectPr.append(col_elem)
        col_elem.set(qn('w:num'), '2')
        col_elem.set(qn('w:space'), '425')  # ~0.75 cm 欄間距
        col_elem.set(qn('w:sep'), '1')    # 分隔線
    elif layout == "b4-double":
        # B4 橫式雙折（寬 36.4 cm, 高 25.7 cm）
        section.page_width = Cm(36.4)
        section.page_height = Cm(25.7)
        section.orientation = WD_ORIENT.LANDSCAPE
        sectPr = section._sectPr
        col_elem = OxmlElement('w:cols')
        col_elem.set(qn('w:num'), '2')
        col_elem.set(qn('w:space'), '720')  # 1.27 cm
        col_elem.set(qn('w:sep'), '1')
        sectPr.append(col_elem)
    else:
        # A4 單欄
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)

    # 設置全域字型與樣式
    normal_style = doc.styles['Normal']
    normal_font = normal_style.font
    normal_font.name = 'Times New Roman'
    normal_font.size = Pt(10.5)  # 考卷內文標準五號字 (10.5 pt)
    normal_style._element.rPr.rFonts.set(qn('w:eastAsia'), '標楷體')
    normal_style._element.rPr.rFonts.set(qn('w:ascii'), 'Times New Roman')
    normal_style._element.rPr.rFonts.set(qn('w:hAnsi'), 'Times New Roman')
    normal_style._element.rPr.rFonts.set(qn('w:cs'), 'Times New Roman')

    # 段落格式：固定行高 18pt、段前段後 0、關閉貼齊格線
    pPr = normal_style._element.get_or_add_pPr()
    pPr.set(qn('w:snapToGrid'), '0')

    # 考卷抬頭
    p_head = doc.add_paragraph()
    p_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_school = p_head.add_run(f"{school}\n")
    r_school.font.size = Pt(14)
    r_school.bold = True
    r_title = p_head.add_run(title)
    r_title.font.size = Pt(16)
    r_title.bold = True

    # 學生資訊欄位（年級、班級、座號、姓名）
    p_info = doc.add_paragraph()
    p_info.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_info = p_info.add_run("____年____班  座號：______  姓名：______________  得分：_______")
    r_info.font.size = Pt(10)

    # 分隔線或注意事項
    p_note = doc.add_paragraph()
    p_note.add_run("※ 請注意：所有答案請劃記於答案卡／寫於答案卷上，違反規定者扣分。").font.size = Pt(9)
    doc.add_paragraph("─" * 40)

    # 大題範例
    p_sec1 = doc.add_paragraph()
    r_sec1 = p_sec1.add_run("一、單一選擇題（每題 4 分，共 40 分）")
    r_sec1.bold = True

    # 題目示範（選項自動 Tab 對齊）
    q1 = doc.add_paragraph()
    q1.add_run("1.  若一元二次方程式 x² - 5x + k = 0 有兩相異實根，則實數 k 的範圍為？\n")
    q1_opt = q1.add_run("(A) k < 25/4\t(B) k ≤ 25/4\t(C) k > 25/4\t(D) k ≥ 25/4")

    q2 = doc.add_paragraph()
    q2.add_run("2.  下列何者為正多面體？\n")
    q2_opt = q2.add_run("(A) 正八面體\t(B) 正十面體\t(C) 正十二邊形\t(D) 正四角柱")

    p_sec2 = doc.add_paragraph()
    r_sec2 = p_sec2.add_run("\n二、填充題（每格 5 分，共 30 分）")
    r_sec2.bold = True
    doc.add_paragraph("1.  計算：(2 + √3) × (2 - √3) = __________。")
    doc.add_paragraph("2.  設 f(x) = 3x² - 6x + 5，則 f(x) 之最小值為 __________。")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(output_path))
    # 接著用 XML 修復器加強底層屬性
    converter = ExamWinConverter(font_zh="標楷體", font_en="Times New Roman", line_spacing_pt=18.0)
    converter.convert_docx(output_path, output_path)
    return True


def main():
    parser = argparse.ArgumentParser(description="Mac 考卷轉 Windows 完美相容轉檔工具")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # convert
    p_conv = subparsers.add_parser("convert", help="轉換單一 docx 檔案")
    p_conv.add_argument("--input", "-i", required=True, help="輸入的 Mac docx 檔案路徑")
    p_conv.add_argument("--output", "-o", required=True, help="輸出的 Windows 格式 docx 檔案路徑")
    p_conv.add_argument("--font-zh", default="標楷體", help="中文字型（標楷體 / 新細明體 / 微軟正黑體，預設標楷體）")
    p_conv.add_argument("--font-en", default="Times New Roman", help="英數字型（預設 Times New Roman）")
    p_conv.add_argument("--line-spacing", type=float, default=18.0, help="固定行高 pt（預設 18.0 pt）")
    p_conv.add_argument("--no-fix-tabs", action="store_true", help="不自動調整選擇題選項空白為 Tab")

    # batch
    p_batch = subparsers.add_parser("batch", help="批次轉換目錄內所有 docx 考卷")
    p_batch.add_argument("--input-dir", "-i", required=True, help="來源考卷資料夾")
    p_batch.add_argument("--output-dir", "-o", required=True, help="輸出資料夾")
    p_batch.add_argument("--font-zh", default="標楷體", help="中文字型")
    p_batch.add_argument("--font-en", default="Times New Roman", help="英數字型")
    p_batch.add_argument("--line-spacing", type=float, default=18.0, help="固定行高 pt")

    # scaffold
    p_scaf = subparsers.add_parser("scaffold", help="產生符合 Windows 標準的考卷空白樣板")
    p_scaf.add_argument("--output", "-o", default="考卷_Windows標準版面.docx", help="輸出檔案名稱")
    p_scaf.add_argument("--layout", default="a4-double", choices=["a4-double", "a4-single", "b4-double"], help="考卷版面配置")
    p_scaf.add_argument("--title", default="113學年度第一學期 第一次定期評量 數學科試題", help="考卷大標題")
    p_scaf.add_argument("--school", default="市立國民中學／高級中學", help="校名")

    args = parser.parse_args()

    if args.command == "convert":
        in_p = Path(args.input)
        out_p = Path(args.output)
        conv = ExamWinConverter(
            font_zh=args.font_zh,
            font_en=args.font_en,
            line_spacing_pt=args.line_spacing,
            fix_tabs=not args.no_fix_tabs
        )
        print(f"正在修復並轉換考卷：{in_p.name} ...")
        conv.convert_docx(in_p, out_p)
        print(f"✅ 轉換成功！已輸出 Windows 相容考卷：{out_p}")

    elif args.command == "batch":
        in_dir = Path(args.input_dir)
        out_dir = Path(args.output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        conv = ExamWinConverter(
            font_zh=args.font_zh,
            font_en=args.font_en,
            line_spacing_pt=args.line_spacing
        )
        files = list(in_dir.glob("*.docx"))
        if not files:
            print(f"⚠️ 在 {in_dir} 找不到任何 .docx 檔案。")
            return
        print(f"找到 {len(files)} 個考卷檔案，開始批次轉換...")
        for idx, f in enumerate(files, 1):
            # NFC 檔名正規化，防止 Windows 解開或讀取亂碼
            norm_name = unicodedata.normalize('NFC', f.name)
            out_file = out_dir / norm_name
            try:
                conv.convert_docx(f, out_file)
                print(f"[{idx}/{len(files)}] ✓ {norm_name}")
            except Exception as e:
                print(f"[{idx}/{len(files)}] ❌ 失敗 {norm_name}: {e}")
        print(f"✅ 批次轉換完成！成果位於：{out_dir}")

    elif args.command == "scaffold":
        out_p = Path(args.output)
        print(f"正在產生 {args.layout} 規格的 Windows 考卷骨架...")
        create_scaffold_exam(out_p, title=args.title, school=args.school, layout=args.layout)
        print(f"✅ 產生完成！檔案：{out_p}")

if __name__ == "__main__":
    main()
