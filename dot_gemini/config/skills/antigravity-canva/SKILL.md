---
name: antigravity-canva
description: 在 Antigravity 連接 Canva 遠端 MCP 服務。當使用者提到「連接 Canva」、「設定 Canva」、「Canva MCP」、「搜尋 Canva 設計」時載入此技能。
---

# 連接 Canva（Antigravity 版）

本技能指引如何在 Antigravity 中配置 Canva 遠端 MCP（Remote MCP），讓 Agent 能搜尋並操作 Canva 設計。

---

## 服務規格

- **服務**：Canva（canva.com）
- **通道**：遠端 MCP（Remote MCP / SSE / HTTP）
- **MCP URL**：`https://mcp.canva.com/mcp`
- **驗證方式**：OAuth 2.0（Dynamic Client Registration）

---

## 步驟一：配置全域 MCP 設定

在全域 MCP 設定檔 `~/.gemini/config/mcp_config.json` 中的 `mcpServers` 區塊加入 Canva 設定：

```json
{
  "mcpServers": {
    "canva": {
      "serverUrl": "https://mcp.canva.com/mcp"
    }
  }
}
```

> [!NOTE]
> Antigravity 支援遠端 MCP 服務，使用 `serverUrl` 欄位指定端點網址。

---

## 步驟二：完成 OAuth 授權與驗證

1. 儲存 `mcp_config.json` 後，重新載入 Antigravity MCP。
2. 進入 Antigravity 的 **Settings → Customizations → MCP Servers** 或對話中觸發 Canva 工具。
3. 依畫面提示開啟瀏覽器，登入 Canva 帳號並完成 OAuth 授權。
4. 驗證連線：請 Agent 呼叫 `search-designs` 列出目前帳號下的設計。
