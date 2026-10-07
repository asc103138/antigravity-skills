---
name: antigravity-advanced-doc-toolkit
description: 教師行政進階文件與資料處理工具包（Word排版、PDF合併分割、PDF表格結構精準抽取、Excel/Pandas段考大表統計、圖片批次處理與浮水印）。包含 macOS 原生適性（中文字型、NFC檔名正規化、EXIF校正、uv隨選安裝）。當使用者提到「進階文件處理」、「PDF表格擷取」、「段考成績分析」、「PDF合併分割」、「Word講義排版」、「圖片批次浮水印」時載入此技能。
---

# 教師行政進階文件與資料處理工具包（macOS 適性強化版）

本技能為專門針對 AI Agent 與教師行政打造的進階自動化擴充包，奠基於核心文件工具之上，深入解決複雜排版、PDF 結構化抽取、成績大表統計與圖片批次處理等高階需求。

---

## 一、 核心架構與執行原則

1. **智慧隨選載入機制 (On-Demand Loading)**：
   - 預先不強制安裝所有套件，Agent 依據使用者當前任務類型（如處理 PDF 表格、段考大表或圖片批次）自主判斷，即時透過 `uv` 安裝對應套件，維持專案環境輕量純淨。
2. **100% 本機端運算與隱私防線**：
   - 學校正式公文、考卷、段考學生成績與教師行政資料，**100% 透過本機 Python 腳本直接在電腦硬碟運算**，絕對禁止上傳至第三方外部分析 API 或非授權雲端。
   - 學生資料處理原則：僅記錄或顯示班級代號與座號，真實姓名一律建議遮蔽或去識別化。

---

## 二、 macOS 專屬適性化配置 (macOS Adaptation)

在 macOS（包含 Apple Silicon M 系列晶片）執行文件與圖形自動化時，必須遵循以下系統適性：

| macOS 適性痛點 | 原因與影響 | 本技能解決方案 |
|---|---|---|
| **Python PEP 668 限制** | 系統防護禁止全域 `pip install` | 一律使用 `uv venv .venv --python 3.12` 隔離，隨選安裝使用 `uv pip install --python .venv/bin/python <pkg>`。 |
| **中文字型缺失 (ReportLab/Matplotlib)** | Linux 字型或 Windows 字型在 macOS 不存在，造成 PDF 亂碼、黑框或 Matplotlib 方塊字 | 自動指向 macOS 系統字型：`/System/Library/Fonts/PingFang.ttc` 或 `/System/Library/Fonts/Supplemental/Songti.ttc`，動態註冊中文字型。 |
| **Unicode NFD 檔名分解** | macOS APFS 預設檔名編碼為 NFD，中文檔名在跨平台傳輸時常變成注音或亂碼 | 讀寫檔時以 `unicodedata.normalize('NFC', path)` 統一轉為 NFC 標準字元。 |
| **系統垃圾檔案干擾** | 資料夾批次處理常受 `.DS_Store`、`__MACOSX`、`._` 檔案阻礙 | 批次遍歷目錄時主動過濾忽略上述隱藏與暫存檔案。 |
| **照片 EXIF 顛倒** | iPhone/iPad 拍攝之考卷或活動照片常有 EXIF 旋轉方向標記 | Pillow 處理圖片前自動調用 `ImageOps.exif_transpose` 轉正方向。 |

---

## 三、 七大工具分工與隨選安裝矩陣

| 工具套件 | 主要定位與任務場景 | 隨選安裝指令 (macOS + uv) |
|---|---|---|
| **`pdfplumber`** | 精準抽取 PDF 成績單、課表、報表中的表格結構與文字座標 | `uv pip install --python .venv/bin/python pdfplumber` |
| **`pypdf`** | PDF 批次合併、依頁碼分割、頁面旋轉、元資料移除 | `uv pip install --python .venv/bin/python pypdf` |
| **`reportlab`** | 程式化動態生成 PDF 格式化公文、研習證書、通知單 | `uv pip install --python .venv/bin/python reportlab` |
| **`pandas`** | 高速清理、合併、樞紐分析與多維度統計大量段考成績大表 | `uv pip install --python .venv/bin/python pandas openpyxl` |
| **`openpyxl`** | 讀寫 Excel 活頁簿、設定單元格顏色、公式與自適應欄寬 | `uv pip install --python .venv/bin/python openpyxl` |
| **`python-docx`** | 建立與修改 Word 文件、套用標準標題階層、表格排版 | `uv pip install --python .venv/bin/python python-docx` |
| **`pillow`** | 批次圖片尺寸調整、格式轉換、教材圖片浮水印壓印 | `uv pip install --python .venv/bin/python pillow` |

---

## 四、 高頻應用標準範例腳本（可直接調用）

### 1. 【PDF 表格抽取】使用 `pdfplumber` 將 PDF 表格轉為結構化資料
適用：段考成績 PDF、研習簽到表、課表 PDF 轉 Excel/CSV。
```python
import pdfplumber
import pandas as pd
from pathlib import Path
import unicodedata

def extract_tables_from_pdf(pdf_path: str, output_excel: str):
    pdf_path = unicodedata.normalize('NFC', pdf_path)
    all_rows = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_idx, page in enumerate(pdf.pages, 1):
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    # 去除換行並過濾空白
                    clean_row = [cell.strip().replace('\n', ' ') if cell else '' for cell in row]
                    if any(clean_row):
                        all_rows.append(clean_row)
                        
    if all_rows:
        df = pd.DataFrame(all_rows[1:], columns=all_rows[0])
        df.to_excel(output_excel, index=False)
        print(f"✅ 成功從 PDF 擷取 {len(df)} 筆資料至 {output_excel}")
    else:
        print("⚠️ 未在 PDF 中偵測到結構化表格")
```

---

### 2. 【PDF 合併與旋轉】使用 `pypdf` 批次整理文件
適用：多份學習單合併、掃描方向轉正、分離封面。
```python
from pypdf import PdfReader, PdfWriter
from pathlib import Path

def merge_and_fix_pdfs(input_files: list[str], output_pdf: str, rotate_degrees: int = 0):
    writer = PdfWriter()
    for file in input_files:
        p = Path(file)
        if p.name.startswith('.') or p.name == '.DS_Store':
            continue
        reader = PdfReader(str(p))
        for page in reader.pages:
            if rotate_degrees in (90, 180, 270):
                page.rotate(rotate_degrees)
            writer.add_page(page)
            
    with open(output_pdf, 'wb') as f:
        writer.write(f)
    print(f"✅ 已成功將 {len(input_files)} 個 PDF 合併儲存至 {output_pdf}")
```

---

### 3. 【段考大表統計】使用 `pandas` 進行學生成績統計與五標分析
適用：期中期末考總分、平均、排名、高低標、及格率分析。
```python
import pandas as pd
import numpy as np

def analyze_exam_scores(excel_path: str, output_path: str):
    df = pd.read_excel(excel_path)
    
    # 假設欄位包含：班級, 座號, 國文, 英文, 數學, 自然, 社會
    score_cols = [c for c in ['國文', '英文', '數學', '自然', '社會'] if c in df.columns]
    
    # 計算總分與平均
    df['總分'] = df[score_cols].sum(axis=1)
    df['平均'] = df[score_cols].mean(axis=1).round(2)
    df['班排名'] = df.groupby('班級')['總分'].rank(ascending=False, method='min').astype(int)
    
    # 統計摘要（五標與平均）
    summary = df[score_cols + ['總分', '平均']].agg([
        ('平均值', lambda x: x.mean().round(2)),
        ('標準差', lambda x: x.std().round(2)),
        ('最高分', lambda x: x.max()),
        ('最低分', lambda x: x.min()),
        ('頂標(88%)', lambda x: np.percentile(x.dropna(), 88).round(1)),
        ('前標(75%)', lambda x: np.percentile(x.dropna(), 75).round(1)),
        ('均標(50%)', lambda x: np.percentile(x.dropna(), 50).round(1)),
        ('後標(25%)', lambda x: np.percentile(x.dropna(), 25).round(1)),
        ('底標(12%)', lambda x: np.percentile(x.dropna(), 12).round(1))
    ])
    
    with pd.ExcelWriter(output_path) as writer:
        df.to_excel(writer, sheet_name='學生成績明細', index=False)
        summary.to_excel(writer, sheet_name='學科統計五標')
    print(f"✅ 段考統計分析完成，已匯出至 {output_path}")
```

---

### 4. 【macOS 中文字型 PDF 產出】使用 `reportlab` 生成通知單或研習證書
適用：程式化生成無亂碼的通知單、榮譽榜、研習證書。
```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

def generate_notice_pdf(output_pdf: str, student_title: str, content: str):
    # macOS 繁體中文字型載入（優先使用蘋方或微軟正黑/宋體）
    font_candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
        "/Library/Fonts/Arial Unicode.ttf"
    ]
    font_name = "Helvetica" # fallback
    for fpath in font_candidates:
        if os.path.exists(fpath):
            try:
                pdfmetrics.registerFont(TTFont('macOS-Zh', fpath, subfontIndex=0))
                font_name = 'macOS-Zh'
                break
            except Exception:
                continue

    doc = SimpleDocTemplate(output_pdf, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('TitleStyle', fontName=font_name, fontSize=18, leading=24, alignment=1)
    body_style = ParagraphStyle('BodyStyle', fontName=font_name, fontSize=12, leading=18)
    
    story = [
        Paragraph(student_title, title_style),
        Spacer(1, 20),
        Paragraph(content.replace('\n', '<br/>'), body_style)
    ]
    doc.build(story)
    print(f"✅ 已成功產生 PDF：{output_pdf}（使用字型：{font_name}）")
```

---

### 5. 【圖片批次處理與浮水印】使用 `Pillow` 處理活動與教材照片
適用：成果展照片壓印學校名稱、EXIF 自動轉正、批次壓縮成教材解析度。
```python
from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path
import unicodedata

def batch_process_images(input_dir: str, output_dir: str, watermark_text: str = "", max_width: int = 1600):
    in_path = Path(input_dir)
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    # 支援格式
    valid_exts = {'.jpg', '.jpeg', '.png', '.webp'}
    
    for file in in_path.iterdir():
        # 過濾 macOS 隱藏檔案
        if file.name.startswith('.') or file.suffix.lower() not in valid_exts:
            continue
            
        with Image.open(file) as img:
            # 1. 自動修正 iPhone / iPad 拍照之 EXIF 方向
            img = ImageOps.exif_transpose(img)
            
            # 2. 等比例縮放
            if img.width > max_width:
                scale = max_width / float(img.width)
                new_size = (max_width, int(float(img.height) * scale))
                img = img.resize(new_size, Image.Resampling.LANCZOS)
                
            # 3. 壓製文字浮水印
            if watermark_text:
                draw = ImageDraw.Draw(img)
                # 載入 macOS 系統字型
                font_path = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
                if not Path(font_path).exists():
                    font_path = "/System/Library/Fonts/PingFang.ttc"
                try:
                    font = ImageFont.truetype(font_path, size=max(20, int(img.width * 0.025)))
                except Exception:
                    font = ImageFont.load_default()
                    
                bbox = draw.textbbox((0, 0), watermark_text, font=font)
                w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
                x = img.width - w - 25
                y = img.height - h - 25
                # 陰影與文字
                draw.text((x + 1, y + 1), watermark_text, fill=(0, 0, 0, 128), font=font)
                draw.text((x, y), watermark_text, fill=(255, 255, 255, 220), font=font)
                
            # 儲存 (檔名正規化)
            clean_name = unicodedata.normalize('NFC', file.stem) + ".jpg"
            img.convert('RGB').save(out_path / clean_name, 'JPEG', quality=85)
            
    print(f"✅ 圖片批次處理完成，輸出至 {output_dir}")
```

---

## 五、 使用情境觸發對照表

| 當使用者提到... | 應調用之核心工具 | 行動要點 |
|---|---|---|
| 「幫我把這幾張成績單 PDF 的表格抓出來轉成 Excel」 | `pdfplumber` + `openpyxl` | 抽取邊框表格，按欄位重組為 DataFrame 匯出 |
| 「把這 3 個 PDF 合併成一份，中間有兩頁橫向的幫我轉正」 | `pypdf` | 逐頁讀取、判斷旋轉角度、合併為單一 PDF |
| 「分析這份全學年段考成績，計算五標、排名與各學科平均」 | `pandas` | 讀入 Excel 大表，進行聚合統計並生成摘要分頁 |
| 「把這份教學活動相片縮小到 1600px，並在右下角印上校名」 | `Pillow` | EXIF 轉正、高品質雙三次縮放、壓製半透明浮水印 |
| 「自動產生一份研習簽到表與研習證明 PDF，中文不要跑版」 | `reportlab` | 註冊 macOS 蘋方/黑體字型，組裝標題與段落流式版面 |
