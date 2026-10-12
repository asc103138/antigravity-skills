---
name: opencode-browser
description: 在 OpenCode 連接瀏覽器控制工具（Playwright MCP + open-computer-use）。說「裝瀏覽器控制」「瀏覽器自動化」「Playwright MCP」時載入。
---

# 瀏覽器控制與桌面自動化（OpenCode 版）

> 本版已由 AntiGravity 版轉為 **OpenCode 適性版**：路徑改為 `~/.config/opencode/skills/`，MCP 設定改為 `opencode.json` 的 `mcp` 區段，互動提問使用 `question` 工具。

## 說明
透過 MCP 協定為 OpenCode 連接瀏覽器與桌面操作能力：
- **Playwright MCP**：網頁導航、表單填寫、點擊與資料擷取。
- **open-computer-use**：桌面視窗控制與截圖。

---

## 步驟

### 1. 安裝套件
```powershell
npm install -g open-computer-use
```

驗證指令：
```powershell
open-computer-use --version
```

### 2. 註冊 MCP
在 OpenCode 全域設定 `~/.config/opencode/opencode.json`（`mcp` 區段）（或 workspace `opencode.json`）中加入：

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx.cmd",
      "args": ["-y", "@playwright/mcp@latest"]
    },
    "open-computer-use": {
      "command": "open-computer-use",
      "args": ["mcp"]
    }
  }
}
```

> ⚠️ Windows 環境請使用 `npx.cmd`。

### 3. 驗證
重新啟動 OpenCode 或透過 `/mcp` 重新載入後：
- 測試瀏覽器：要求代理開啟指定網址並回報標題
- 測試截圖：要求代理擷取桌面或指定視窗

---

## 輕量替代方案（Browser CLI）
若僅需簡單的網頁擷取或截圖，可使用免 MCP 的 CLI-Anything：
```powershell
pip install cli-anything-hub
cli-hub install browser
cli-anything-browser navigate https://example.com
cli-anything-browser screenshot --output page.png
```
