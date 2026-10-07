---
name: antigravity-lazy-packs
description: Antigravity 全域技能總覽與懶人包索引。當使用者說「Antigravity 懶人包」、「全域技能清單」、「有哪些技能可以用」時載入此技能。
---

# Antigravity 全域技能懶人包總覽

本索引列出已安裝在 `~/.gemini/config/skills/` 的全域技能。在任何專案中，你可以直接透過自然語言觸發，或輸入斜線指令（如 `/<skill-name>`）調用特定技能。

---

## 已安裝之全域技能清單

| 編號 | 技能名稱 | 主要功能 | 觸發關鍵字範例 |
|---|---|---|---|
| 01 | `antigravity-notebooklm` | 連接與操作 Google Gemini Notebook（NotebookLM）MCP | 「連接 NotebookLM」、「產生教學簡報」 |
| 02 | `antigravity-github` | GitHub CLI 登入、Git 設定與安全推送流程 | 「連接 GitHub」、「設定 git」 |
| 03 | `antigravity-canva` | Canva 遠端 MCP 連接與設計搜尋 | 「連接 Canva」、「Canva MCP」 |
| 04 | `antigravity-obsidian` | Obsidian 第二大腦三層架構與專案駕駛艙（原生讀寫） | 「連接 Obsidian」、「第二大腦」、「每日筆記」 |
| 05 | `antigravity-open-slide` | 現代化 React 簡報生成（1920x1080 畫布）與回饋微調 | 「製作簡報」、「open-slide」 |
| 06 | `antigravity-sheets-gas` | Google 試算表資料庫 ＋ Apps Script 網頁應用程式 | 「用試算表存資料」、「GAS 後端」 |
| 07 | `antigravity-browser` | 瀏覽器控制（內建 `/browser` 與 Playwright MCP） | 「瀏覽器控制」、「網頁截圖」 |
| 08 | `antigravity-draw` | AI 圖片生成指引（內建生圖與 OpenAI 雙路線） | 「生圖」、「畫圖」、「產生圖片」 |
| 09 | `antigravity-firebase` | Firebase CLI 與 Firebase MCP 連接與管理 | 「連接 Firebase」、「Firestore」 |
| 10 | `antigravity-workflow` | 開工、收工與新專案初始化標準生命週期 | 「開工」、「收工」、「初始化專案」 |
| 11 | `antigravity-doc-toolkit` | 教學檔案處理（Word、Excel、PPT、PDF、QR Code） | 「檔案處理」、「PDF 轉 Markdown」 |
| 12 | `antigravity-external-tools` | 外部工具與服務連接決策地圖（通道與鑰匙） | 「連接外部工具」、「外部工具指南」 |
| 13 | `antigravity-clasp-netlify` | Clasp 雲端部署 ＋ Netlify MCP 零複製雙向閉環網頁系統 | 「clasp 部署」、「Netlify 發佈」、「雙向閉環」、「網頁接試算表」 |
| 14 | `antigravity-exam-win-converter` | Mac 考卷轉 Windows 完美相容轉檔（字型替換、行距鎖定、雙欄排版、選項對齊） | 「考卷轉檔」、「Mac考卷轉Windows」、「考卷跑版」、「考卷排版修復」 |
| 15 | `funfun-edu-gem-hub` | 172 款 Gemini Gems 全能教育 AI 助理與智慧調度中樞（特教、教案、作文、命題、繪圖等） | 「教育Gem」、「方方老師」、「特教教材」、「作文批改」、「素養教案」 |
| 16 | `teacher-course-assignment-skill` | 國中小教師配課、排課、鐘點試算與雙重會計檢查 | 「配課」、「排課」、「減課」、「教師任課」 |
| 17 | `teacher-slide-image-workshop` | 教學簡報與工作坊 16:9 逐頁 AI 圖像簡報製作 | 「教學投影片生成」、「簡報繪圖」、「逐頁簡報」 |
| 18 | `parent-meeting-studio` | 班親會、家長日企劃、簡報、講者備註與響應式網站設計 | 「班親會」、「家長日」、「親師座談會」 |
| 19 | `antigravity-advanced-doc-toolkit` | 教學行政進階文件與資料處理（macOS適性、PDF表格抽取、合併分割、Pandas大表統計、圖片批次浮水印） | 「進階文件處理」、「PDF表格擷取」、「段考成績分析」、「圖片批次浮水印」 |
| 20 | `g4-curriculum-review` | 全域教材與試題三階審查中樞（強制約束：所有考卷、學習單、教學簡報、各類教材生成前必審，南一數/翰林國/康軒社/海線情境） | 「生成教材」、「出考卷」、「做學習單」、「教學簡報」、「審教材」、「四年級審查」、「三階漏斗審查」 |

---

## 使用方式

1. **自然語言觸發**：在任何對話中說出與該技能相關的關鍵字或任務描述，Antigravity 會自動動態載入相應技能。
2. **斜線指令（Slash Commands）**：直接在輸入框輸入 `/<技能名稱>`（例如 `/antigravity-workflow` 或 `/antigravity-notebooklm`）。
3. **專案客製化覆蓋**：若特定專案需要客製化版本，可在該專案根目錄建立 `.agents/skills/<技能名稱>/SKILL.md`，專案級設定將優先於此全域設定。
