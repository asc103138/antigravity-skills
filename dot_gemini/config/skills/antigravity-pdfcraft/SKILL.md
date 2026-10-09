---
name: antigravity-pdfcraft
description: 使用純 Rust 開發的高效能 PDF 工作工作台 PdfCraft (pdfcraft-cli / PdfCraft.app / MCP) 進行 PDF 檢視、合併、分割、頁面操作、文字抽取、渲染轉圖、表單填寫、註解標記、浮水印、最佳化壓縮與安全防護。當使用者提到「PdfCraft」、「PDF處理」、「PDF合併」、「PDF分割」、「PDF轉圖片」、「PDF旋轉」、「PDF表單」、「PDF浮水印」、「PDF壓縮最佳化」時載入此技能。
---

# Antigravity PdfCraft (macOS) 技能指引

PdfCraft 是以純 Rust 開發、對標 Adobe Acrobat Pro 功能的現代開源 PDF 工作工作台（Workbench）。本環境已完成 macOS 原生與 Antigravity 全面適性化整合。

---

## 🎯 核心功能與架構

1. **三合一操作模式**：
   - **桌面原生 GUI**：`/Applications/PdfCraft.app`（終端命令 `pdfcraft`），即時視覺化檢視與互動編輯。
   - **CLI 命令行**：`pdfcraft-cli`，支援高效率批次腳本與命令列處理。
   - **Antigravity 原生 MCP**：`pdfcraft` MCP 伺服器，提供 130+ 項全功能工具，可直接於 Agent 會話內精準操控 PDF。
2. **macOS 適性化特性**：
   - 支援 Apple Silicon (arm64) 與 Universal 二進位檔原生執行，啟動快、記憶體負擔極低。
   - 完整支援繁體中文與特殊檔名（UTF-8 / NFC / NFD 正規化路徑）。
   - 內建 CJK 與多國語言字型渲染支援，頁面轉圖與文字編輯不缺字。
   - 已解除 macOS Gatekeeper 隔離屬性 (`xattr -cr`)，無安全彈窗阻礙。

---

## 🛠️ CLI 常用指令速查

已於系統全域路徑配置 `pdfcraft-cli` 與 `pdfcraft`。

### 1. 文件資訊與摘要檢視
```bash
pdfcraft-cli info "文件.pdf" [--password 密碼]
```
輸出 JSON 格式的頁數、尺寸、欄位數、加密狀態、標籤與元資料。

### 2. 高畫質頁面渲染轉圖
```bash
# 渲染第 1 頁為 PNG，可自訂 DPI（預設 96）
pdfcraft-cli render "文件.pdf" --page 1 --dpi 150 --out "預覽.png"
```

### 3. 文字內容抽取
```bash
# 抽取全書或特定頁文字
pdfcraft-cli text "文件.pdf"
pdfcraft-cli text "文件.pdf" --page 2
```

### 4. 頁面旋轉、刪除與重排
```bash
# 旋轉第 1 頁 90 度、刪除第 3 頁、移動第 5 頁到第 1 頁
pdfcraft-cli edit "輸入.pdf" --out "輸出.pdf" --rotate 1:90 --delete 3 --move 5:1
```

### 5. 多檔合併 (Combine)
```bash
pdfcraft-cli combine "檔案1.pdf" "檔案2.pdf" "檔案3.pdf" --out "合併完成.pdf"
```

### 6. 擷取特定頁面 (Extract)
```bash
pdfcraft-cli extract "輸入.pdf" --pages 1,3,5-7 --out "部分頁面.pdf"
```

### 7. 自動分割 (Split)
```bash
# 每 2 頁分割為一個獨立檔案
pdfcraft-cli split "輸入.pdf" --every 2 --out-dir "./分割輸出/"

# 在第 3 頁與第 7 頁處切分
pdfcraft-cli split "輸入.pdf" --before 3,7 --out-dir "./分割輸出/"
```

---

## 🔌 Antigravity MCP 伺服器操作流程

PdfCraft 已註冊於 `~/.gemini/antigravity/mcp_config.json`：
```json
"pdfcraft": {
  "command": "pdfcraft-cli",
  "args": ["mcp"]
}
```

### 標準 MCP 工作流：
1. **開啟文件**：呼叫 `doc_open`（傳入 `path`），取得文件編號 `doc`（整數 ID）。
2. **執行操作**：
   - **檢視與分析**：`doc_info`, `page_render`, `text_paragraphs`, `text_lines`, `text_find`
   - **頁面編排**：`page_rotate`, `page_delete`, `page_move`, `page_insert_blank`, `page_insert_file`, `page_extract`
   - **文件加工**：`doc_watermark`, `doc_background`, `doc_header_footer`, `doc_optimize`, `doc_flatten`
   - **表單互動**：`form_fields`, `form_fill`, `form_reset`
   - **註解與校對**：`comment_list`, `comment_add`, `comment_reply`
   - **安全性防護**：`doc_protect`, `doc_unprotect`, `redact_mark`, `redact_apply`
3. **儲存修改**：呼叫 `doc_save`（增量寫入或另存新檔）。
4. **關閉文件**：呼叫 `doc_close` 釋放資源。

---

## 🖥️ 桌面視窗 GUI 與自動化控制

欲直接開啟圖形化視窗檢視或編輯：
```bash
pdfcraft "文件.pdf"
```

若需由 Agent 在背景控制執行中的 GUI 介面：
```bash
# 啟動並監聽控制通訊埠
pdfcraft --control /tmp/pdfcraft_ctrl.json "文件.pdf"

# 透過 CLI 發送動作、點擊按鈕或截圖
pdfcraft-cli ui --control /tmp/pdfcraft_ctrl.json inspect query=rotate
pdfcraft-cli ui --control /tmp/pdfcraft_ctrl.json screenshot --out /tmp/window.png
```
