---
name: antigravity-open-slide
description: 使用 open-slide 工具建立與編輯現代化簡報（Slide Deck）。當使用者提到「製作簡報」、「建立投影片」、「open-slide」、「產生 Slide Deck」、「修改簡報」時載入此技能。
---

# open-slide 簡報工具技能（Antigravity 版）

`open-slide` 是專為 AI Agent 設計的簡報框架。Agent 負責編寫 React 投影片元件，`open-slide` 負責 1920 × 1080 固定畫布、縮放、導覽、熱重載（Hot Reload）、演講者模式（Presenter Mode）與靜態匯出。

---

## 快速開始

### 1. 初始化簡報專案

```bash
npx @open-slide/cli init my-slide
cd my-slide
npm install  # 或 pnpm install
npm run dev
```

---

## 簡報撰寫工作流程

當使用者要求製作簡報時，Agent 應依序執行以下流程：

### 步驟一：四個前置收斂問題（Scoping Questions）

在動手寫程式碼之前，先向使用者確認以下四個維度：

1. **主題與視覺風格（Topic & Aesthetic）**：簡報核心主題、目標聽眾、希望的色調與視覺風格（如：極簡科技、溫暖教育、商務專業）。
2. **預估頁數（Page Count）**：預計製作幾頁（例如 5~10 頁）。
3. **文字密度（Text Density）**：精煉關鍵字／標語型，抑或是完整說明文字型。
4. **動態呈現（Motion vs. Static）**：是否需要轉場動效、逐步顯現，或純靜態呈現。

---

### 步驟二：規劃大綱與結構

1. 規劃每頁的 Slide ID、主標題、內容結構與版面佈局。
2. 遵循 1920 × 1080 的固定畫布比例，注意字級大小階層（Title: 48~64px, Body: 24~32px, Caption: 16~20px）。

---

### 步驟三：編寫 React 投影片

在 `slides/<id>/index.tsx` 撰寫投影片元件：
- 使用標準 React + Tailwind CSS 撰寫。
- 利用內建的 Assets 管理器與 svgl 圖標庫引入高品質視覺元件。

---

### 步驟四：瀏覽器標記與反覆微調（In-Browser Inspector Loop）

1. 使用者在預覽頁面中點擊任何元素並新增評論（如：*「字體調大」*、*「背景改成深藍」*）。
2. 評論會以 `@slide-comment` 標記寫入原始碼。
3. Agent 讀取標記、自動套用修改並清除 `@slide-comment` 標記。

---

### 步驟五：匯出與部署

- **匯出為靜態 HTML / PDF**：
  ```bash
  npm run build
  ```
- 產出之純靜態檔案可直接部署至 GitHub Pages、Vercel、Cloudflare Pages 等靜態託管平台。
