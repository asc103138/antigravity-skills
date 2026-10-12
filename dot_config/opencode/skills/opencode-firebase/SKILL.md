---
name: opencode-firebase
description: 在 OpenCode 連接 Firebase MCP。說「連接 Firebase」「設定 Firebase」時載入。
---

# 連接 Firebase（OpenCode 版）

> 本版已由 AntiGravity 版轉為 **OpenCode 適性版**：路徑改為 `~/.config/opencode/skills/`，MCP 設定改為 `opencode.json` 的 `mcp` 區段，互動提問使用 `question` 工具。

## 步驟

### 1. 安裝與登入
```bash
npx.cmd -y firebase-tools@latest --version
npx.cmd -y firebase-tools@latest login
npx.cmd -y firebase-tools@latest projects:list
```

### 2. 註冊 MCP
寫進 OpenCode 的 MCP 設定檔（專案 `.opencode/` 或全域 `~/.config/opencode/opencode.json` 的 `mcp` 區段），修改前先取得確認：
```json
{
  "mcpServers": {
    "firebase": {
      "command": "npx.cmd",
      "args": ["-y", "firebase-tools@latest", "mcp"]
    }
  }
}
```
完成後重新啟動 OpenCode 使 MCP 生效。

### 3. 安全規則
- Admin SDK 憑證不可公開
- 學生資料只存班級代號與座號
