---
name: antigravity-notebooklm
description: 在 Antigravity 連接與操作 Google Gemini Notebook（原 NotebookLM）MCP。當使用者提到「連接 NotebookLM」、「設定 NotebookLM」、「Gemini 筆記本」、「產生教學簡報」、「產生音訊概覽」、「下載筆記本資料」時載入此技能。
---

# 連接與操作 Google Gemini Notebook（Antigravity 版）

本技能指引如何在 Antigravity 中透過 `notebooklm-mcp-cli` 連接與操作 Google Gemini Notebook（原 NotebookLM），實現自動上傳資料、產生簡報、資訊圖表、音訊概覽（Podcast）等功能。

---

## 原理與架構

```
Antigravity ←(MCP 協定)→ notebooklm-mcp (翻譯官) ←(Google 登入 Session)→ Gemini Notebook
```

- **套件名稱**：PyPI 上的 `notebooklm-mcp-cli`（注意：切勿使用 npm 上的 `nlm`，那是無關套件）。
- **指令分工**：
  - `nlm`：CLI 工具（用於登入、診斷、手動檢查）。
  - `notebooklm-mcp`：MCP Server 本體（由 Antigravity 背景啟動）。

---

## 步驟一：安裝工具（macOS 建議使用 uv）

優先使用 `uv` 獨立環境安裝：

```bash
uv tool install notebooklm-mcp-cli
```

若無 `uv`，可使用 pip 安裝：

```bash
pip install notebooklm-mcp-cli
```

安裝後確認指令可用：

```bash
nlm --version
notebooklm-mcp --help
```

> [!NOTE]
> `uv tool install` 安裝於 `~/.local/bin/`。若出現 `command not found`，請確認 `~/.local/bin` 已加入 PATH（或執行 `source ~/.zshrc`）。

---

## 步驟二：登入 Google 帳號

請在獨立可見的終端機視窗中執行（不要在 Antigravity 背景執行）：

```bash
nlm login
```

1. 指令會自動開啟 Chrome/預設瀏覽器進入 Google 登入頁面。
2. 登入欲使用的 Google 帳號。
3. 登入完成後執行診斷確認：

```bash
nlm doctor
nlm list
```

---

## 步驟三：註冊 Antigravity MCP

在終端機執行 Antigravity 專屬設定指令：

```bash
nlm setup add antigravity
```

該指令會自動將 MCP 設定寫入 `~/.gemini/config/mcp_config.json` 或專案 `.agents/mcp_config.json`。

若需手動確認或填寫，請檢查 `~/.gemini/config/mcp_config.json` 是否包含：

```json
{
  "mcpServers": {
    "notebooklm": {
      "command": "notebooklm-mcp",
      "args": ["--transport", "stdio"]
    }
  }
}
```

> [!WARNING]
> 1. `command` 必須是 `notebooklm-mcp`，不能填 `nlm`。
> 2. 若已有 `notebooklm` 項目，請勿重複添加。

---

## 步驟四：建立本機產物儲存目錄

在使用者家目錄建立分類資料夾：

```bash
mkdir -p ~/Documents/"Gemini Notebook"/{slides,infographics,audio,video,docs,sheets,mindmaps,quizzes}
```

目錄功能：
- `slides/`：簡報（Slide Deck，可匯出 PPTX）
- `infographics/`：資訊圖表
- `audio/`：音訊概覽（Audio Overview / Podcast）
- `video/`：影片概覽（Video Overview）
- `docs/`：報告文件（Reports）
- `sheets/`：數據表格（Data Tables）
- `mindmaps/`：心智圖（Mind Map）
- `quizzes/`：測驗題與閃卡

---

## 步驟五：驗證連線

1. 重新載入 Antigravity MCP 或重啟 Antigravity。
2. 請 Antigravity 嘗試列出目前筆記本清單：
   「請列出我的 Gemini Notebook 筆記本數量與名稱。」
3. 成功列出（即使清單為空）即代表連線成功。

---

## 安全守則

- **保護隱私**：切勿將 `notebooks.json`、筆記本 ID 清單、個人研究報告或產出圖片 commit 到公開 Git 儲存庫。
- **憑證安全**：Session 儲存於 `~/.notebooklm-mcp-cli/`，切勿複製或外流 Cookie / Token。
