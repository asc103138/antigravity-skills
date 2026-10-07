---
name: antigravity-browser
description: 在 Antigravity 中使用瀏覽器與桌面自動化控制。當使用者提到「瀏覽器控制」、「開啟網頁」、「網頁截圖」、「Playwright MCP」、「自動填表」、「桌面自動化」時載入此技能。
---

# 瀏覽器與桌面自動化控制技能（Antigravity 版）

本技能指引如何在 Antigravity 中運用內建瀏覽器能力與外接 Playwright MCP 進行網頁自動化操作。

---

## 路線評估：依需求選擇最適方案

| 方案 | 適用情境 | 優點 |
|---|---|---|
| **路線 A：Antigravity 內建瀏覽器** | 查閱網頁、搜尋公開資訊、文檔閱讀 | 零配置，直接使用 `/browser` 指令或內建網頁讀取工具 |
| **路線 B：Playwright MCP** | 需要自動填表、點擊按鈕、爬取動態渲染內容、多頁面自動化 | 支援完整無頭瀏覽器與多步驟控制 |
| **路線 C：桌面自動化（open-computer-use）** | 需要跨應用程式點擊、控制本機視窗或桌面截圖 | 支援桌面級別操作 |

---

## 路線 A：使用 Antigravity 內建瀏覽器功能

- 針對網頁閱讀與即時資料搜尋，可直接在對話中輸入 `/browser` 或要求 Agent 讀取指定網址。
- 零設定、速度最快，無需啟動外部程序。

---

## 路線 B：配置 Playwright MCP（進階網頁控制）

若需執行自動填表、複雜點擊或動態 SPA 操作，可配置 Playwright MCP：

### 1. 編輯全域 MCP 設定檔 `~/.gemini/config/mcp_config.json`

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp"]
    }
  }
}
```

### 2. 驗證

重啟 Antigravity 或重新載入 MCP 後，請 Agent 執行驗證：
「請使用 Playwright 開啟 https://example.com 並告訴我頁面標題。」

---

## 路線 C：桌面自動化控制（open-computer-use）

若需要控制桌面應用或進行視窗級別操作：

### 1. 安裝套件

```bash
npm install -g open-computer-use
```

### 2. 加入 `~/.gemini/config/mcp_config.json`

```json
{
  "mcpServers": {
    "open-computer-use": {
      "command": "open-computer-use",
      "args": ["mcp"]
    }
  }
}
```

> [!NOTE]
> `open-computer-use` 需使用 `open-computer-use mcp` 子命令啟動以正確暴露工具。
