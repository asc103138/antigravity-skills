---
name: antigravity-external-tools
description: Antigravity 外部工具與服務連接決策指南。當使用者提到「連接外部工具」、「接外部服務」、「外部工具指南」、「怎麼接 API」、「MCP 怎麼設定」時載入此技能。
---

# 外部工具連接決策指南（Antigravity 2 版）

本技能為 Antigravity 2 連接各類外部服務（雲端硬碟、筆記、資料庫、教學平台等）提供完整的訪談流程、決策判路與設定指引。

---

## 核心觀念：通道與鑰匙

- **通道（怎麼接）**：
  - 內建連接器 / 工具（最推薦、零設定）
  - MCP（Model Context Protocol，標準擴充協定）
  - CLI（命令列工具）
  - 畫面操控（Browser / Computer Use，備用手段）
- **鑰匙（怎麼授權）**：
  - 免鑰匙（本地資料夾如 Obsidian）
  - API Key / Token（貼入本機設定檔或 `.env`）
  - OAuth 2.0（瀏覽器授權登入）

---

## 連接四步決策流程

當使用者想接上某個外部服務時，Agent 應依序執行：

### 第一步：訪談（確認需求）
1. **要接哪個服務？**（例如 Google Drive、Obsidian、Firebase、Canva…）
2. **要「讀」還是「寫」？**（只讀權限較安全；寫入權限需更謹慎）
3. **確認環境**：本機環境（macOS）、基礎工具（Node.js / Python / uv / Git）是否完備。

### 第二步：判路（選擇最佳路徑）
1. **是 Google 個人個資服務（Drive / Gmail / 行事曆）嗎？**
   - 優先評估內建連接或唯讀匯出；切勿使用單一 API Key 嘗試存取 Google 個人個資。
2. **Antigravity 有內建或 MCP Store 支援嗎？**
   - 在 Antigravity 中開啟 **Settings → Customizations → MCP Store**，搜尋服務名稱。有現成者優先透過介面安裝。
3. **社群有成熟的 MCP Server 或官方 CLI 嗎？**
   - 有 MCP：加入 `~/.gemini/config/mcp_config.json`，完成後重啟 Antigravity。
   - 有 CLI：安裝後執行登入指令（如 `gh auth login`, `nlm login`）。
4. **都沒有？**
   - 最後手段：使用 `/browser` 或 Playwright MCP 借用使用者已登入之瀏覽器狀態。

---

## Antigravity 2 設定入口一覽

| 方式 | 設定位置 | 說明 |
|---|---|---|
| **MCP Store（優先）** | `Settings → Customizations` | 搜尋服務名、按 Install、填入必要參數 |
| **手動全域 MCP** | `~/.gemini/config/mcp_config.json` | 支援 `command` (stdio) 與 `serverUrl` (SSE/HTTP) |
| **手動專案 MCP** | 專案目錄 `.agents/mcp_config.json` | 僅對該專案生效 |
| **內建瀏覽器** | `/browser` 斜線指令 | 直接瀏覽與擷取公開網頁內容 |

---

## 常見服務快查表

| 服務 | 推薦通道 | 鑰匙 | 具體做法 |
|---|---|---|---|
| **Obsidian** | 本地檔案讀寫 | 免鑰匙 | **Antigravity 2 直接讀寫 Vault**，無需裝 MCPVault |
| **NotebookLM** | CLI / MCP | 獨立 Session | 裝 `notebooklm-mcp-cli` → `nlm login` → `nlm setup add antigravity` |
| **GitHub** | CLI (`gh`) | OAuth | `brew install gh` → `gh auth login` |
| **Canva** | 遠端 MCP | OAuth | `mcp_config.json` 設定 `serverUrl: "https://mcp.canva.com/mcp"` |
| **Firebase** | CLI / MCP | 服務金鑰 / 帳號 | `npx -y firebase-tools@latest login`，MCP 註冊至 `mcp_config.json` |
| **Supabase** | MCP | API Key | 官方 Supabase MCP 搭配專案金鑰 |
| **Google Sheets** | GAS Web App | Google 帳號 | 使用 `antigravity-sheets-gas` 技能，免安裝部署 |

---

## 安全守則

1. **能用 OAuth 就別用 API Key**；能用本地檔案讀寫（如 Obsidian）就別繞道 MCP。
2. **金鑰僅存於本機設定檔或 `.env`**，絕不寫入程式碼或 commit 至 Git。
3. **學生資料去識別化**：僅儲存代號與座號，嚴禁儲存真名與聯絡方式。
4. **授權前充分告知**：說明要連接之權限範圍並取得使用者核准。
