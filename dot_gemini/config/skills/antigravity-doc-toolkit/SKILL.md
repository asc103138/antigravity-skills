---
name: antigravity-doc-toolkit
description: 教學檔案處理核心工具包（Word、Excel、PowerPoint、PDF、圖片、QR Code、教材轉 Markdown）。當使用者提到「檔案處理」、「PDF 轉 Markdown」、「產生 Word」、「產生 PPT」、「合併 PDF」、「產生 QR Code」、「MarkItDown」時載入此技能。
---

# 教學檔案處理核心工具包（Antigravity 版）

本技能指引如何在專案中快速建立 Python 虛擬環境，並配置教學與行政常見之文件處理（Word、Excel、PowerPoint、PDF、圖表、QR Code 與格式轉換）核心工具。

---

## Agent 必要守則

1. **獨立虛擬環境**：套件安裝至專案本機之 `.venv` 中，避免污染全域 Python 環境。
2. **核心優先**：預設僅安裝經篩選的 10 項核心必裝套件，非必要工具不主動安裝。
3. **使用 uv 管理**：優先使用 `uv` 建立虛擬環境與安裝相依，速度快且相容性高。

---

## 核心必裝套件清單

| 套件 | 用途 |
|---|---|
| `python-docx` | 讀寫、產生與格式化 Word 文件 |
| `openpyxl` | 讀寫與樣式化 Excel 試算表 |
| `python-pptx` | 產生與修改 PowerPoint 簡報 |
| `pypdf` | PDF 檔案合併、分割、旋轉與浮水印 |
| `PyMuPDF` | 高效 PDF 抽文字、抽頁、轉高解析圖片 |
| `reportlab` | 程式化生成 PDF 文件與浮水印圖層 |
| `pillow` | 圖片裁切、縮放、格式轉換與圖層合成 |
| `matplotlib` | 繪製統計圖表並匯出為高解析圖片 |
| `qrcode[pil]` | 產生自訂大小與顏色的 QR Code 圖片 |
| `markitdown[pdf,docx,pptx,xlsx]` | 將各類教學檔案精準轉成 Markdown 文本 |

---

## macOS 安裝流程（使用 uv）

在專案目錄下執行：

```bash
# 1. 建立 Python 3.12 虛擬環境
uv venv .venv --python 3.12

# 2. 安裝核心套件
uv pip install --python .venv/bin/python \
  python-docx openpyxl python-pptx pypdf PyMuPDF reportlab pillow matplotlib "qrcode[pil]" "markitdown[pdf,docx,pptx,xlsx]"
```

---

## 驗證腳本

執行單行指令驗證 10 個核心套件皆可正確匯入：

```bash
.venv/bin/python -c "
mods = ['docx', 'openpyxl', 'pptx', 'pypdf', 'fitz', 'reportlab', 'PIL', 'matplotlib', 'qrcode', 'markitdown']
for m in mods:
    __import__(m)
print('✅ 核心套件 10/10 匯入成功！')
"
```

---

## 常用功能範例指令

### 1. 教材轉換為 Markdown（MarkItDown）
```bash
.venv/bin/python -c "
from markitdown import MarkItDown
md = MarkItDown()
result = md.convert('input.pdf')
print(result.text_content)
"
```

### 2. 產生 QR Code
```bash
.venv/bin/python -c "
import qrcode
img = qrcode.make('https://example.com')
img.save('qrcode.png')
print('✅ QR Code 已儲存為 qrcode.png')
"
```
