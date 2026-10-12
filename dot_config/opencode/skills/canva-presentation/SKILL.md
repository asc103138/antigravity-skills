---
name: canva-presentation
description: 自動製作符合 Canva 規範的國小教學與班務簡報：透過 Canva 官方 MCP 真連線自動建設計、放元素、匯出 PDF/PPTX，輸出卡片版型、講稿備忘錄與批次建立表格，並持續學習使用者的設計習慣。當使用者說「做簡報」「Canva」「教學簡報」「班務簡報」「國小簡報」「一頁式簡報」時載入。
---

# Canva 簡報自動生成技能（MCP 連線版）

> 使用者的 Canva 帳號為**教育版**（享 Pro 功能：resize、品牌範本可用；Enterprise 的 autofill 不可用）。
> 本技能由 RDQ 規格 `C:\opencode\rdq\RDQ-spec-Canva架接整合-20260829.md`（status: confirmed）授權執行。

---

## 0. 前置：MCP 連線與授權

- 伺服器：Canva 官方遠端 MCP `https://mcp.canva.com/mcp`（已在 `C:\Users\ccps\.config\opencode\opencode.json` 的 `mcp.canva` 掛載，`type: remote`）。
- **首次使用會先被要求 OAuth**：在瀏覽器登入 Canva、按下授權，看到「authorization successful」後回到 opencode 即完成。每台電腦、每個帳號各授權一次。
- 開工即驗證：用 `search-designs` 查「最近編輯的設計」，成功＝連線狀態正常；失敗＝走第 3 節重連線 SOP。
- 授權或連線無法恢復 → 明確告知使用者，改用第 5 節「無連線備案」並在對話中說明限制。

## 1. 主要製作流程（從需求到成品）

1. **需求確定**：沿用下方「輸出格式範本」產出卡片版型＋講稿備忘錄＋素材關鍵字（先確認大綱再動工）。
2. **找基礎**：`search-designs`（關鍵字：簡報、presentation、海報）＋ `get-design` 看既有成品是否可 `copy-design` 改版；也可 `import-design-from-url` 帶入現成模板。
3. **建設計**：用 `generate-design`（文字描述建設計）或 `create-design-from-candidate(response_id, design_id)` 採用候選；指定尺寸與方向（教學簡報一般 16:9）。
4. **逐頁編輯**：`start-editing-transaction` → 用 `perform-editing-operations`（新增/更新文字、元素、圖片；一次可塞多個 operation）→ `commit-editing-transaction`；中途要放棄改 `cancel-editing-transaction`。**先加文字骨架，後補圖與裝飾，最後調整與核對。**
   - ⚠️ **已知限制（2026-08-29 實測）**：AI 生成設計（generate-design）中的**空標題框**，`replace_text` 會回 `internal_error`（欄位是模板佔位框）。解法：生成時就在 query 裡指定標題文字，或寫入後在大綱層級用 `format_text` 調整；仍不行就 `delete_element` 後改用頁面既有文字元素。
   - ⚠️ **resize 額度**：教育版走 `resize-design` 出現 `trial_information.uses_remaining` 為試用額度，用完即需 Pro 升級（回報使用者再決定）。
5. **匯出**：`export-design` 選格式（PDF 給交付／PPTX 給可編輯）；教育版＝Pro 品質輸出。匯出後取得 URL 下載，並把設計原址（短連結 `resolve-shortlink`）一起交付。
6. **學習**：匯出後做第 4 節「學習設計習慣」一次。
7. **收尾**：把成品檔名、Canva 連結、學習記錄寫進技能目錄的 `design-guidelines.md`，並依專案約定更新 `handoff.md`。

## 2. 可用 MCP 工具速查（官方 2026 現況）

| 用途 | 工具（red = 使用者帳號不可用） |
|---|---|
| 查設計 | `search-designs`、`get-design`、`get-design-pages`、`get-design-content`、`get-presenter-notes`、`get-export-formats`、`get-design-thumbnail` |
| 建設計 | `generate-design`、`create-design-from-candidate`、`copy-design`、`import-design-from-url`、`resolve-shortlink` |
| 編輯 | `start-editing-transaction`、`perform-editing-operations`、`commit-editing-transaction`、`cancel-editing-transaction` |
| 匯出 | `export-design`（含 premium 素材時可能 `license_required` 失敗，改確認內容） |
| resize | `resize-design`（Pro+，教育版 OK） |
| 品牌模板 | `search-brand-templates`、`create-design-from-brand-template`（Pro+，OK）；`autofill-design`、`get-brand-template-dataset`（**Enterprise only，不可用**） |
| 素材 | `upload-asset-from-url`、`get-assets` |
| 資料夾 | `create-folder`、`list-folder-items`、`search-folders`、`move-item-to-folder` |
| 評論 | `comment-on-design`、`list-comments`、`list-replies`、`reply-to-comment` |

- 單次設計請控制在合理呼叫量（匯出 20 req/min、generate 20 req/min、編輯交易 20 req/min、其他讀取 100 req/min）。
- 素材圖片：先 `upload-asset-from-url`（30 req/min）再引用；圖片素材關鍵字建議中英並列。

## 3. 重連線 SOP（OAuth）

| 症狀 | 處理 |
|---|---|
| 工具回 401／authorization 錯誤／mcp.canva.com 連不上 | ①檢查 `opencode.json` 的 `canva` 區塊仍在且 `enabled: true`；②重啟 opencode；③重跑 OAuth（opencode 的 remote MCP 連線畫面重試授權），重整 opencode 後提示「重新認證」 |
| 瀏覽器授權完成但 opencode 沒感應 | 重啟 opencode 再試一次；仍失敗→檢查 token 存放（opencode 本機快取）後清除重授 |
| 換電腦 | 新機同 config，首次使用重新 OAuth 一次即可（每帳號每機一次） |
| 帳號升級／改用其他 Canva 帳號 | 清除本機授權重新登入；確認登入的是**教育版**帳號 |
| 一切正常但工具回「plan 限制」 | 對照第 2 節速查——紅字就是該帳號不可用，改走可用路線 |

無法修復時：明確告知改用第 5 節無連線備案，不要把失敗留到「播放前一晚」。

## 4. 學習使用者的設計習慣（真的做，不掛名）

- **每次完成**：用 `get-design`（含 `get-design-content`／`get-presenter-notes`）讀自製成品，把以下觀察記進 `C:\Users\ccps\.config\opencode\skills\canva-presentation\design-guidelines.md`：
  - 慣用配色（含 hex、對比設定）、字體偏好（中文標楷/黑體傾向）、版面模型（3 欄卡片/流程步驟/對比圖/大字卡）、常用素材類型、頁面密度與行數上限、講稿語氣。
- **每次開工前**：先讀 `design-guidelines.md`，把使用者慣用樣式應用到新簡報，再問「這次有沒有要改的新習慣」。
- **防跑偏**：設計習慣是參考不是規則——使用者本次明說「這次風格換一下」時，以本次指示為準；事後把顯著偏離寫回筆記。
- 筆記格式精簡即可（每次 3–5 行），過 30 次做一次整理。

## 5. 無連線備案（既有功能，維持但不強化）

MCP 不可用時：僅輸出「輸出格式範本」的卡片版型＋「🛠️ Canva 一鍵批次套版資料」CSV 表格，請使用者複製貼入 Canva 的批次建立（Bulk Create）功能。此路徑只做表格與規格輸出，**不做**自動連線、自動學習。

---

## 輸出格式範本

### 投影片 1：[頁面標題]
- **頁面核心觀點**：[一句話總結這頁要學什麼]
- **版面模型**：[3欄卡片 / 流程步驟 / 對比圖 / 重點大字卡]
- **卡片內容**：
  1. **[關鍵詞1]**：[精簡說明，15字內]
  2. **[關鍵詞2]**：[精簡說明，15字內]
  3. **[動腦想一想]**：[引導學生思考的互動提問]
- **Canva 素材關鍵字**：`[素材1英文/中文]`, `[素材2英文/中文]`
- **講者備忘錄（講稿）**：*「[2~3句老師上課現場說的話術]」*

*(重複上述結構直到所有頁面完成)*

### 🛠️ Canva 一鍵批次套版資料（直接複製使用）

請將以下表格內容複製，貼入 Canva 的「批次建立 (Bulk Create)」功能中（連線版可改為透過 MCP 自動建設計）：

| 頁碼 | 頁面標題 | 核心重點 | 卡片內容1 | 卡片內容2 | 互動提問 | 講者備忘錄 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P01 | ... | ... | ... | ... | ... | ... |
| P02 | ... | ... | ... | ... | ... | ... |
