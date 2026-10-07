---
name: antigravity-obsidian
description: 在 Antigravity 連接與管理 Obsidian 第二大腦筆記本。當使用者提到「連接 Obsidian」、「設定 Obsidian」、「第二大腦」、「每日筆記」、「專案駕駛艙」、「知識重整」時載入此技能。
---

# 連接與管理 Obsidian 第二大腦（Antigravity 版）

本技能指引如何在 Antigravity 2 中直接讀寫 Obsidian Vault，建立三層筆記結構與專案駕駛艙，無需額外安裝 MCP。

---

## 核心觀念：Antigravity 2 直接讀寫 Vault

> [!IMPORTANT]
> **Antigravity 2 不需要安裝 MCPVault**：
> Antigravity 本身具備完整且安全的原生檔案讀寫工具（`view_file`, `write_to_file`, `replace_file_content`）。Obsidian Vault 本質上就是一般的本機 Markdown 資料夾，Antigravity 可直接讀寫，既快速又不會有多餘的相依套件問題。

---

## 步驟一：確認使用者的 Obsidian Vault 路徑

常見 macOS 路徑：
- `~/Documents/<Vault名稱>`
- `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/<Vault名稱>`（iCloud 同步）
- `~/Google Drive/我的雲端硬碟/<Vault名稱>`

若不確定路徑，可透過終端機搜尋含有 `.obsidian` 設定目錄的資料夾：

```bash
find ~ -maxdepth 4 -type d -name ".obsidian" 2>/dev/null
```

確認條件：
1. 目錄存在且包含 `.obsidian/` 子資料夾。
2. 經使用者確認為主要使用的筆記本。

---

## 步驟二：建立第二大腦三層架構

在 Vault 根目錄規劃清晰的三層結構：

```
Obsidian Vault/
├── 每日筆記/           # 第一層：原始輸入（每日想法、會議紀錄、臨時靈感）
│   └── YYYY-MM-DD.md
├── 創作庫/             # 第二層：加工輸出（教學簡報草稿、專案產出、整理後筆記）
└── 知識庫/             # 第三層：知識沉澱（SOP、模板、可重複使用之知識）
    └── 專案模板/
```

| 層次 | 資料夾 | 用途 | 更新頻率 |
|---|---|---|---|
| 第一層 | `每日筆記/` | 原始想法、零散紀錄 | 每天 |
| 第二層 | `創作庫/` | 產出型內容、專案紀錄 | 每週 |
| 第三層 | `知識庫/` | 長期沉澱之知識、SOP | 每月 |

---

## 步驟三：建立專案駕駛艙

在 Vault 內為各專案建立專屬筆記：`<Vault路徑>/<專案名稱>/專案工作流程.md`。

專案駕駛艙範本：

```markdown
# <專案名稱> — 專案工作流程與進度

## 📌 目前進度
- [x] 完成基礎環境配置
- [ ] 實作核心功能

## 🧭 下一步行動
1. 

## 💡 關鍵決策與踩坑紀錄
- 決策：
- 踩坑：
```

---

## 步驟四：在專案 `AGENTS.md` 記錄關聯路徑

在專案根目錄的 `AGENTS.md` 內記錄 Vault 路徑：

```markdown
## Obsidian 關聯筆記
- Vault 路徑：~/Documents/Secondbrain
- 專案駕駛艙：~/Documents/Secondbrain/<專案名稱>/專案工作流程.md
```

> [!WARNING]
> 本機絕對路徑若含個人使用者名稱，請勿 commit 至公開 GitHub 儲存庫。

---

## 步驟五：每週知識重整流程

1. **整理每日筆記**：將本週每日筆記中具長期價值的內容提取至「創作庫」或「知識庫」。
2. **更新專案駕駛艙**：檢視各專案進度、完成項與下一步。
3. **清理封存**：將過期或已結案之臨時筆記歸檔。
