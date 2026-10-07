---
name: antigravity-docling
description: 使用 IBM Docling (docling-mcp / docling CLI) 進行全格式（PDF、Word、PPT、Excel、Keynote、Pages、HTML）超高速結構化解析與圖文表格原位對齊。當使用者提到「Docling」、「解析文件」、「多格式轉檔」、「Word轉Markdown」、「PPT轉Markdown」、「快速解析PDF」、「Docling MCP」時載入此技能。
---

# Antigravity Docling 文件解析技能

## 🎯 技能定位與優勢
Docling 是由 IBM Research 開源的現代化文件解析旗艦工具（MIT 授權），專為 Generative AI 與 Agent 設計：
1. **全格式支援**：原生支援 PDF、DOCX、PPTX、XLSX、Pages、Keynote、HTML、EPUB。
2. **圖文表格原位對齊**：自研 TableFormer 模型，精確解析複雜跨頁表格；圖片與圖表（長條圖/折線圖）原位標註與圖說關聯。
3. **極度輕量與高速**：對 Apple Silicon 與 CPU 高度最佳化，啟動快、記憶體負擔小，為日常文件轉換的第一首選。
4. **原生 MCP 支援**：已全域接入 `docling-mcp-server`，AI Agent 具備原生轉換工具能力。

---

## 🚀 雙軌解析策略指引
- **一級日常主力（Docling）**：處理所有一般的 PDF、行政公文、Word 講義、教學 PPT、跨格式文件轉換。
- **二級極限重裝（MinerU）**：遇到極端複雜的理化考卷（密集 LaTeX 數學公式）、低解析度掃描件、密集雙欄學術論文。

---

## 🛠️ CLI 常用指令速查

系統已透過 `uv tool` 全域安裝 `docling` 與 `docling-mcp-server`。

### 1. 單檔轉換為 Markdown
```bash
docling "講義.pdf" --to md --output "./output"
```
支援直接處理 `.docx`、`.pptx`、`.xlsx` 等格式：
```bash
docling "教學簡報.pptx" --to md --output "./output"
```

### 2. 同步匯出 JSON 結構與圖表
```bash
docling "報告.pdf" --to md --to json --output "./output"
```

### 3. 指定 OCR 語言（中英文）
```bash
docling "掃描文件.pdf" --ocr-engine rapidocr --output "./output"
```

---

## 🔌 Docling MCP Server 配置
本機 Antigravity 已在全域 `~/.gemini/antigravity/mcp_config.json` 註冊：
```json
{
  "docling": {
    "command": "docling-mcp-server",
    "args": ["--transport", "stdio", "conversion"]
  }
}
```
Agent 可在會話中直接利用 MCP 工具取得解析後結構與圖文資訊。
