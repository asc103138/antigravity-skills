---
name: antigravity-workflow
description: Antigravity 開工、收工與新專案初始化標準工作流程。當使用者說「開工」、「收工」、「初始化專案」、「新專案」時載入此技能。
---

# 開工 / 收工 / 新專案初始化技能（Antigravity 2 版）

本技能規範 Antigravity 2 下的標準專案生命週期管理。Antigravity 2 以專案根目錄之 `AGENTS.md` 作為核心規則入口，`ANTIGRAVITY.md` 作為精簡引導入口，`handoff.md` 作為多 Agent 交接紀錄，進度細節則記錄於 Obsidian 專案駕駛艙。

---

## 一、開工流程（當使用者說「開工」）

當使用者發出「開工」指令時，Agent 依序執行以下 5 個步驟：

1. **讀取專案規則檔**：
   - 讀取專案根目錄的 `AGENTS.md`（若存在 `ANTIGRAVITY.md` 與 `handoff.md` 一併讀取）。
2. **讀取專案筆記**：
   - 讀取對應的 Obsidian 專案駕駛艙（如 `<Vault>/<專案>/專案工作流程.md`）。
3. **檢查版本控制狀態**：
   - 執行 `git status` 與 `git log -n 3` 檢視最近變更。
4. **回報現況與建議**：
   - 彙整目前進度、待辦項目，並提出建議之「下一步行動」。
5. **安全限制**：
   - 未經使用者確認，**不自動執行** pull、commit 或 push。

---

## 二、收工流程（當使用者說「收工」）

當使用者發出「收工」指令時，Agent 依序執行以下 7 個步驟：

1. **敏感資料與資安掃描**：
   - 檢查變更檔案中是否意外夾帶 API Key、Token、密碼、Firebase Admin 憑證、NotebookLM 個人筆記清單或學生真名。
2. **更新 Obsidian 專案駕駛艙**：
   - 記錄今日完成事項、下一步待辦、以及踩坑與決策。
3. **維護規則檔**：
   - 僅在專案長期固定規則或路徑發生改變時才更新 `AGENTS.md`；階段性進度與 Agent 交接資訊記錄於 `handoff.md`。
4. **檢視 Git 變更**：
   - 執行 `git status` 與 `git diff`。
5. **精準 Stage**：
   - 只加入本次相關檔案，**嚴格禁止無差別執行 `git add .`**。
6. **Commit 與 Push**：
   - 產生清晰之 Commit Message，經使用者確認後進行 commit 與 push。
7. **回報同步結果**：
   - 回報 Obsidian、GitHub 與專案檔案之同步狀態。

---

## 三、新專案初始化流程（當使用者說「新專案初始化」）

### 1. 訪談與需求確認
- 專案名稱與核心用途
- 本機主要工作目錄
- 是否建立 GitHub Repo（公開 / 私有）
- 是否需要部署（GitHub Pages / Firebase / Vercel）
- Obsidian Vault 與專案駕駛艙位置

### 2. 建立或補齊專案檔案
- `AGENTS.md`（依下方範本）
- `ANTIGRAVITY.md`（指向 AGENTS.md 的精簡入口）
- `README.md`
- `.gitignore`（自動忽略 `.env`、`node_modules/`、`__pycache__/`、敏感金鑰等）
- 初始化本機 Git Repo 並關聯遠端 GitHub Repo
- 在 Obsidian Vault 建立專案工作流程駕駛艙

> [!NOTE]
> 若目標目錄已是既有專案，先盤點「已存在 / 缺失」清單，僅補足缺口，絕不擅自覆蓋既有設定。

---

## 建議的 AGENTS.md 範本

```markdown
# <專案名稱> - AGENTS.md

## 專案資訊
- 專案名稱：
- 專案用途：
- 主要工作目錄：
- GitHub Repo：

## Obsidian 關聯筆記
- Vault 路徑：
- 專案駕駛艙：

## 工作與安全規則
- 回應使用繁體中文（台灣）。
- 開工時讀本檔、讀 Obsidian 駕駛艙、檢查 Git 狀態。
- 收工時更新 Obsidian，檢查 diff 後只提交本次相關檔案。
- 絕不 commit API Key、Token、密碼或個人隱私資料。
- 學生資料僅記錄班級代號與座號，不儲存真名。
- **全域教材審查規範**：凡涉及生成考卷、學習單、教學簡報或教材，必須嚴格落實三階審查（第一階課綱版本門檻、第二階CLT與退回確認、第三階迷思診斷），通過自我檢測並隨附審查報告後始得輸出交付。
```
