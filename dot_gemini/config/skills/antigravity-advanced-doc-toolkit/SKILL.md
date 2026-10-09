---
name: antigravity-advanced-doc-toolkit
description: 教師行政進階文件與資料處理工具包（PdfCraft 原生 PDF 引擎、Word排版、PDF合併分割、PDF表格結構精準抽取、Excel/Pandas段考大表統計、圖片批次處理與浮水印）。包含 macOS 原生適性（中文字型、NFC檔名正規化、EXIF校正、uv隨選安裝）。當使用者提到「進階文件處理」、「PDF表格擷取」、「段考成績分析」、「PDF合併分割」、「Word講義排版」、「圖片批次浮水印」、「PDF轉圖」、「PDF壓縮最佳化」時載入此技能。
---

# 教師行政進階文件與資料處理工具包（macOS 適性強化版 + PdfCraft 原生引擎整合）

本技能為專門針對 AI Agent 與教師行政打造的進階自動化擴充包，奠基於核心文件工具之上，深入解決複雜排版、PDF 結構化抽取、成績大表統計與圖片批次處理等高階需求。現已**深度整合純 Rust 原生 `PdfCraft` (Acrobat Pro 等級引擎)**，形成「**Rust 原生高速 PDF 核心 ＋ Python 彈性資料運算**」的雙軌旗艦架構。

---

## 一、 核心架構與執行原則

1. **雙軌引擎架構 (Dual-Engine Strategy)**：
   - **PDF 結構與文件操作軌 (PdfCraft)**：凡涉及 PDF 檢視、頁面重排、旋轉、多檔合併、切頁分割、高畫質轉圖、壓印浮水印、PDF 壓縮最佳化、表單填寫、安全性防護等，**優先調用本機原生的 `pdfcraft-cli` 或 `pdfcraft` MCP 伺服器**。百毫秒級原生運算，完全保留書籤、表單、簽名與圖層，且無需啟動 Python 虛擬環境。
   - **資料統計與文件排版軌 (Python + uv)**：涉及複雜大表統計（Pandas 段考五標）、Excel 細部樣式格式化（openpyxl）、Word 講義產生修改（python-docx）、特殊表格坐標抽取（pdfplumber）、程式化生成公文通知單（reportlab）、圖片 EXIF 轉正（Pillow）時，透過 `uv` 即時載入執行。
2. **100% 本機端運算與隱私防線**：
   - 學校正式公文、考卷、段考學生成績與教師行政資料，**100% 透過本機直接在電腦硬碟運算**，絕對禁止上傳至第三方外部分析 API 或非授權雲端。
   - 學生資料處理原則：僅記錄或顯示班級代號與座號，真實姓名一律建議遮蔽或去識別化。

---

## 二、 macOS 專屬適性化配置 (macOS Adaptation)

在 macOS（包含 Apple Silicon M 系列晶片）執行文件與圖形自動化時，必須遵循以下系統適性：

| macOS 適性痛點 | 原因與影響 | 本技能解決方案 |
|---|---|---|
| **PDF 處理依賴多、速度慢** | 傳統 Python 庫依賴 Poppler、C 函式庫，安裝繁瑣且常掉格式 | 原生整合 **`PdfCraft` (Universal 二進位檔)**，系統預裝於 `~/.local/bin`，無需任何額外 C 依賴。 |
| **Python PEP 668 限制** | 系統防護禁止全域 `pip install` | Python 軌一律使用 `uv venv .venv --python 3.12` 隔離，隨選安裝使用 `uv pip install --python .venv/bin/python <pkg>`。 |
| **中文字型缺失 (ReportLab/Matplotlib)** | Linux 字型或 Windows 字型在 macOS 不存在，造成 PDF 亂碼或方塊字 | 自動指向 macOS 系統字型：`/System/Library/Fonts/PingFang.ttc` 或 `/System/Library/Fonts/Supplemental/Songti.ttc`，動態註冊中文字型；PdfCraft 則原生內建 CJK 字型引擎。 |
| **Unicode NFD 檔名分解** | macOS APFS 預設檔名編碼為 NFD，中文檔名在跨平台傳輸時常變成注音或亂碼 | 讀寫檔時以 `unicodedata.normalize('NFC', path)` 統一轉為 NFC 標準字元，PdfCraft 亦原生支援 UTF-8 NFC/NFD 自動相容。 |
| **系統垃圾檔案干擾** | 資料夾批次處理常受 `.DS_Store`、`__MACOSX`、`._` 檔案阻礙 | 批次遍歷目錄時主動過濾忽略上述隱藏與暫存檔案。 |
| **照片 EXIF 顛倒** | iPhone/iPad 拍攝之考卷或活動照片常有 EXIF 旋轉方向標記 | Pillow 處理圖片前自動調用 `ImageOps.exif_transpose` 轉正方向。 |

---

## 三、 工具分工矩陣

| 工具 | 類型 | 主要定位與任務場景 | 安裝與調用方式 |
|---|---|---|---|
| **`PdfCraft`** | **Rust 原生 (推薦首選)** | **PDF 頁面合併、分割、旋轉、高畫質轉圖、浮水印、壓縮最佳化、表單填寫、安全性移除** | 已安裝於全域 `pdfcraft-cli`，或直接使用 `pdfcraft` MCP 工具 |
| **`pdfplumber`** | Python 套件 | 精準抽取 PDF 成績單、課表、報表中的「複雜表格邊框結構」與文字坐標 | `uv pip install --python .venv/bin/python pdfplumber` |
| **`reportlab`** | Python 套件 | 程式化動態生成 PDF 格式化公文、研習證書、通知單 | `uv pip install --python .venv/bin/python reportlab` |
| **`pandas`** | Python 套件 | 高速清理、合併、樞紐分析與多維度統計大量段考成績大表 | `uv pip install --python .venv/bin/python pandas openpyxl` |
| **`openpyxl`** | Python 套件 | 讀寫 Excel 活頁簿、設定單元格顏色、公式與自適應欄寬 | `uv pip install --python .venv/bin/python openpyxl` |
| **`python-docx`** | Python 套件 | 建立與修改 Word 文件、套用標準標題階層、表格排版 | `uv pip install --python .venv/bin/python python-docx` |
| **`pillow`** | Python 套件 | 批次圖片尺寸調整、格式轉換、EXIF 修正、教材照片浮水印 | `uv pip install --python .venv/bin/python pillow` |

---

## 四、 高頻應用標準範例腳本（可直接調用）

### 1. 【PDF 高速合併、分割與旋轉】使用 `PdfCraft` (首選)
適用：多份學習單合併、旋轉方向轉正、分離章節或封面。
```bash
# A. 合併多份 PDF（完整保留書籤與表單，零損耗）
pdfcraft-cli combine "國語第一單元.pdf" "國語第二單元.pdf" "國語第三單元.pdf" --out "國語講義全冊.pdf"

# B. 頁面旋轉與挑頁刪除（旋轉第 1 頁 90 度、刪除第 3 頁、將第 5 頁移到開頭）
pdfcraft-cli edit "考卷掃描.pdf" --out "考卷轉正.pdf" --rotate 1:90 --delete 3 --move 5:1

# C. 擷取特定頁面
pdfcraft-cli extract "整本教材.pdf" --pages 1-5,10,12 --out "精選內容.pdf"

# D. 批次自動分割（每 2 頁分割為一個獨立檔案）
pdfcraft-cli split "題庫彙編.pdf" --every 2 --out-dir "./各單元考卷/"
```

---

### 2. 【PDF 高畫質頁面轉圖】使用 `PdfCraft`
適用：講義預覽圖、投影片截圖、家長通知單圖片化分享（免裝 Poppler / pdf2image）。
```bash
# 渲染第 1 頁為高品質 PNG（可調整 DPI，預設 96，出版/列印建議 150~300）
pdfcraft-cli render "學校公文.pdf" --page 1 --dpi 150 --out "公文預覽.png"
```

---

### 3. 【PDF 表格抽取】使用 `pdfplumber` 轉為 Excel
適用：段考成績 PDF、研習簽到表、課表 PDF 轉 Excel/CSV。
```python
import pdfplumber
import pandas as pd
import unicodedata

def extract_tables_from_pdf(pdf_path: str, output_excel: str):
    pdf_path = unicodedata.normalize('NFC', pdf_path)
    all_rows = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
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

### 4. 【段考大表統計】使用 `pandas` 分析成績與五標
適用：期中期末考總分、平均、排名、高低標、及格率分析。
```python
import pandas as pd
import numpy as np

def analyze_exam_scores(excel_path: str, output_path: str):
    df = pd.read_excel(excel_path)
    score_cols = [c for c in ['國文', '英文', '數學', '自然', '社會'] if c in df.columns]
    
    df['總分'] = df[score_cols].sum(axis=1)
    df['平均'] = df[score_cols].mean(axis=1).round(2)
    df['班排名'] = df.groupby('班級')['總分'].rank(ascending=False, method='min').astype(int)
    
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

### 5. 【macOS 中文字型 PDF 產出】使用 `reportlab`
適用：程式化生成無亂碼的通知單、榮譽榜、研習證書。
```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

def generate_notice_pdf(output_pdf: str, student_title: str, content: str):
    font_candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc"
    ]
    font_name = "Helvetica"
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
    print(f"✅ 已成功產生 PDF：{output_pdf}")
```

---

### 6. 【圖片批次處理與 EXIF 修正】使用 `Pillow`
適用：成果展照片壓印學校名稱、EXIF 自動轉正、批次壓縮成教材解析度。
```python
from PIL import Image, ImageDraw, ImageFont, ImageOps
from pathlib import Path
import unicodedata

def batch_process_images(input_dir: str, output_dir: str, watermark_text: str = "", max_width: int = 1600):
    in_path = Path(input_dir)
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    valid_exts = {'.jpg', '.jpeg', '.png', '.webp'}
    for file in in_path.iterdir():
        if file.name.startswith('.') or file.suffix.lower() not in valid_exts:
            continue
            
        with Image.open(file) as img:
            img = ImageOps.exif_transpose(img)
            if img.width > max_width:
                scale = max_width / float(img.width)
                img = img.resize((max_width, int(float(img.height) * scale)), Image.Resampling.LANCZOS)
                
            if watermark_text:
                draw = ImageDraw.Draw(img)
                font_path = "/System/Library/Fonts/PingFang.ttc"
                try:
                    font = ImageFont.truetype(font_path, size=max(20, int(img.width * 0.025)))
                except Exception:
                    font = ImageFont.load_default()
                bbox = draw.textbbox((0, 0), watermark_text, font=font)
                w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
                draw.text((img.width - w - 24, img.height - h - 24), watermark_text, fill=(0, 0, 0, 128), font=font)
                draw.text((img.width - w - 25, img.height - h - 25), watermark_text, fill=(255, 255, 255, 220), font=font)
                
            clean_name = unicodedata.normalize('NFC', file.stem) + ".jpg"
            img.convert('RGB').save(out_path / clean_name, 'JPEG', quality=85)
```

---

## 五、 使用情境決策與工具調用表

| 當使用者提到... | 應調用之核心工具 | 調用方式與行動要點 |
|---|---|---|
| **「把這 3 個 PDF 合併成一份，有橫向頁面幫我轉正」** | **`PdfCraft` (首選)** | 執行 `pdfcraft-cli combine ...` 與 `edit --rotate`，零損耗且秒級完成 |
| **「把這份講義第 1 頁轉成高畫質 PNG 圖片」** | **`PdfCraft` (首選)** | 執行 `pdfcraft-cli render "講義.pdf" --page 1 --dpi 150 --out "預覽.png"` |
| **「幫我壓縮最佳化這份過大的 PDF 檔案」** | **`PdfCraft` (MCP / CLI)** | 調用 `doc_optimize` 或 CLI 命令降低圖像解析度並移除冗餘資料 |
| **「幫我把成績單 PDF 的表格抓出來轉成 Excel」** | **`pdfplumber` + `openpyxl`** | 抽取精準網格坐標，按欄位重組為 DataFrame 匯出 |
| **「分析這份全學年段考成績，計算五標、排名與平均」** | **`pandas`** | 讀入 Excel 大表，進行聚合統計並生成學科統計分頁 |
| **「把活動相片縮小到 1600px，並在右下角印上校名」** | **`Pillow`** | EXIF 轉正、雙三次高品質縮放、壓印中文半透明浮水印 |
| **「自動產生研習簽到表與研習證明 PDF，中文字不要跑版」** | **`reportlab`** | 註冊 macOS 蘋方/黑體字型，組裝標題與段落流式版面 |
