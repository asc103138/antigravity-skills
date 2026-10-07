---
name: antigravity-firebase
description: 在 Antigravity 連接與操作 Firebase CLI 及 Firebase MCP。當使用者提到「連接 Firebase」、「設定 Firebase」、「Firebase MCP」、「Firestore」、「部署 Firebase」時載入此技能。
---

# 連接 Firebase（Antigravity 版）

本技能指引如何在 Antigravity 中配置 Firebase CLI 與 Firebase MCP Server，支援 Firestore 資料庫操作、專案管理與雲端部署。

---

## 步驟一：安裝與登入 Firebase CLI

在終端機中透過 `npx` 執行最新版 `firebase-tools`：

```bash
npx -y firebase-tools@latest --version
npx -y firebase-tools@latest login
npx -y firebase-tools@latest projects:list
```

> [!NOTE]
> `firebase login` 需要透過瀏覽器進行互動式 Google 帳號授權，請在一般終端機中完成。

---

## 步驟二：註冊 Firebase MCP

在全域 MCP 設定檔 `~/.gemini/config/mcp_config.json` 加入 Firebase MCP：

```json
{
  "mcpServers": {
    "firebase": {
      "command": "npx",
      "args": ["-y", "firebase-tools@latest", "mcp"]
    }
  }
}
```

完成後重啟 Antigravity 或使用 `/mcp` 重新載入，即可使用 Firebase 相關工具查詢專案與 Firestore 集合。

---

## 安全守則

- **憑證安全**：Firebase 前端 Config（`apiKey`, `projectId`）可公開於前端，但 **Firebase Admin SDK 服務帳戶私密金鑰（Service Account JSON）絕對不可公開或 commit 到 Git**。
- **學生隱私保護**：Firestore 儲存之學生資料嚴禁使用真名與身分證字號，僅使用班級代號與座號。
- **防止專案外洩**：`.firebaserc` 若含敏感之私人專案 ID，公開發布前應審慎評估。
