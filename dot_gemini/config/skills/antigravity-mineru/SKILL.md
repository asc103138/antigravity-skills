---
name: antigravity-mineru
description: 使用 MinerU (v4.0+) 進行高精準度多模態 PDF 與文件結構化解析（支援圖文原位對齊、表格、LaTeX公式還原與 OCR）。當使用者提到「MinerU」、「解析含圖PDF」、「考卷PDF轉檔」、「掃描版PDF轉Markdown」、「論文轉Markdown」或需要解決「PDF內圖片與文字排版錯位、表格公式辨識」時載入此技能。
---

# Antigravity MinerU 文件解析技能

## 🎯 技能定位與核心價值
MinerU（OpenDataLab 開源）為新一代專為 LLM 與 AI Agent 打造的深度學習文件解析引擎。
相較於一般的 PDF 轉文字工具（如 MarkItDown、pdfplumber），MinerU 能徹底解決以下痛點：
1. **圖文錯位問題**：透過版面佈局模型（Layout Analysis），將圖說與圖片切片原位插入在正文段落間，而非堆在文末。
2. **複雜跨頁表格**：自動辨識並還原為乾淨的 Markdown / HTML 表格結構。
3. **數學公式還原**：行內公式與區塊公式精準轉譯為標準 LaTeX。
4. **掃描件與圖中文字**：支援 OCR 模式，將插圖與掃描內容中的印刷文字轉為可讀文字層。

---

## 🛠️ CLI 常用指令範例

系統已將 MinerU 4.0 透過 `uv tool` 安裝於系統環境中（執行檔：`mineru-kit` 與 `mineru`）。

### 1. 標準解析（將 PDF 轉為含圖 Markdown）
```bash
mineru-kit parse "考卷.pdf" -o "./output"
```
- 解析完成後會在 `./output/考卷/` 產生：
  - `考卷.md`（內含圖文對齊、表格與 LaTeX 公式）
  - `images/`（切片出的所有高解析度圖片與插圖）

### 2. 指定頁碼解析
```bash
mineru-kit parse "講義.pdf" -o "./output" -p "1-3,5"
```

### 3. 強制 OCR 模式（適用掃描件或大量文字在圖裡的考卷）
```bash
mineru-kit parse "掃描考卷.pdf" -o "./output" --ocr-mode ocr
```

### 4. 檔位模式（Tier）
```bash
mineru-kit parse "論文.pdf" -o "./output" --tier basic
```
- `flash`：極速文字解析
- `basic`：版面分析 ＋ 基礎小模型
- `standard`：版面分析 ＋ VLM 視覺語言模型精準解析

---

## ⚙️ 模型權重下載說明
本地端首次執行解析時，系統會自動下載所需的視覺與版面模型權重至 `~/.mineru/models`。
若欲提前下載：
```bash
# 下載 basic 檔位模型（約數百 MB ~ 1GB）
mineru-kit models download --tier basic
```

---

## 🍎 macOS Apple Silicon 適性
- 系統已設定 `~/.mineru/config.yaml` 預設啟用 Apple Silicon MPS 硬體加速 (`device-mode: mps`)。
- 圖片檔案路徑在 macOS 上處理時，均符合 Unicode NFC 正規化標準。
