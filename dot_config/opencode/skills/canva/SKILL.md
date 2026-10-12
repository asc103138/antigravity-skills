---
name: canva
description: 連接 Canva 與 OpenCode，讓 Agent 用你的 Canva 帳號建立設計、填寫範本、搜尋與匯出設計。說「用 Canva」「Canva 做設計」「連接 Canva」「讓 Canva 做圖」「Canva 建海報」時載入。
---

# OpenCode 技能：Canva

> 📌 本技能可獨立執行：會自動檢查設定、OAuth、連線並完成驗證。

## 這個技能做什麼

讓 OpenCode 透過 **Canva 官方 MCP**（`https://mcp.canva.com/mcp`）操作你的 Canva 帳號：

- 建立設計（海報、教材圖、小卡、簡報…）
- 自動填寫範本（Brand Template autofill）
- 列出／搜尋現有設計、整理資料夾
- 匯出成 PDF／PNG／JPG 到電腦

## 原理

```
OpenCode ←(MCP remote + OAuth)→ mcp.canva.com ←(Canva Connect API v1)→ Canva 帳號
```

官方 AI 連接工具。不需要 API key、不需要自建 App。

## 先備條件

- [ ] Node.js **22.16+**（Windows 11 本機 v24.19.0 ✅）
- [ ] Canva 方案：官方資格為 Pro／團隊版／商用版／非營利組織；**教育版（學校免費帳號）實測可行**——本機已於 2026-08-29 以教育版授權成功
- [ ] 有網路連線

## 建置步驟（已完成的直接跳到 ⑧ 驗證）

1. **沒設定就先加**：編輯 `C:\Users\ccps\.config\opencode\opencode.json`，在頂層 `mcp` 區塊插入（command 陣列、timeout 必填）：

```json
"canva": {
  "type": "remote",
  "url": "https://mcp.canva.com/mcp",
  "enabled": true,
  "timeout": 300000
}
```

2. **檢查**：`opencode mcp list` → 應顯示 `canva needs authentication` 或 `✓ connected`
3. **授權**：`opencode mcp auth canva` → 瀏覽器打開 Canva 授權頁，登入你的 Canva 帳號按下「允許」
4. **驗證**：`opencode mcp list` → `✓ canva connected`
5. 完全關閉 OpenCode 後重開（MCP 已連線但工具清單要重啟才載入）
6. 對 OpenCode 說「**列出我 Canva 的設計**」或「**用 Canva 幫我做一張海報**」實測

## 產出資料夾結構（本機已建）

```
Documents\Canva\
  ├── designs/      ← 設計檔與原稿
  ├── exports/      ← 匯出的 PDF／PNG／JPG
  └── templates/    ← 拿來套用的範本檔案
```

> Agent 匯出設計時，一律放進 `exports\`；新建立的設計檔（JSON 等）放 `designs\`。

## 排障守則（依症狀查下表）

| 症狀 | 原因 | 處置 |
|---|---|---|
| `opencode mcp list` 顯示 `needs authentication` | 尚未 OAuth | `opencode mcp auth canva`，再 `opencode mcp list` |
| 工具呼叫前報 schema 錯誤 `enum[0]: cannot be empty` 或 `$ref` 解析失敗 | **OpenCode 已知 bug**（issue **#33316**／**#29220**）：Canva 的 `perform-editing-operations` 工具 schema 與 OpenCode／Google provider 不相容 | ①更新 OpenCode 版本看是否已修 ②換模型 provider 方向試 ③改用「列設計／建立簡單設計」等不碰該工具的動作 ④仍不行 → 改用 Canva 網頁搭配本機 `speak`／`audiovisual` 思路手動處理 |
| `HTTP 401 invalid_token` | 存取權杖過期或撤銷 | 重新 `opencode mcp auth canva`（令牌 4 小時，refresh token 自動續） |
| 大工作被逾時中斷 | timeout 太短 | 本技能已設 `300000`；再加大 `experimental.mcp_timeout` |
| 授權卡在「此方案不支援」 | 教育版被管理員停用第三方整合，或帳號非合格方案 | 回報 Canva 說明中心檢查方案資格與管理員設定；**不要自行改走開發者 App／Composio 路線**（這是本機使用者明確排除的備案） |
| 權杖要換帳號 | 想換另一個 Canva 帳號 | `opencode mcp auth canva` 重新授權會取代舊權杖 |

## 安全提醒

- OAuth 權杖由 OpenCode 存在 `~/.local/share/opencode/mcp-auth.json`，不要把這檔複製到 repo
- 學生資料僅可使用 Canva 匯出成品時已遮蔽的內容，沿用「只做不說話」原則：不出姓名、學號等個資進設計

## 相關技能

- `opencode-notebooklm` — 另一條產生簡報／圖片的路線（產出後可比對擇優）
- `audio-notes` — 把影片／錄音變逐字稿再喂進設計
- 懶人包 `04-obsidian` — 把 Canva 成品收進第二大腦
