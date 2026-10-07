# 班親會設計室｜Parent Meeting Studio

這是一套用於「班親會簡報＋班親會網站」的 Agent Skill。

## 核心特色

- 先訪談，不直接套模板
- 最多兩輪主動需求討論
- 使用者確認方向後，全自動完成
- 支援 Subagent 分工
- 逐頁 16:9 AI 圖像簡報
- 每頁 Speaker Notes
- 同視覺系統 Responsive Website
- 內建內容、語言、視覺、教育與網站 QA

## 檔案

- `SKILL.md`：主 Skill 指令
- `references/visual-bible.md`：全套視覺一致性規則
- `schemas/content-plan.yaml`：班親會內容母稿結構
- `schemas/render-brief.yaml`：逐頁生圖規格
- `examples/sample-input.md`：簡單使用範例

## 建議工作流

Discovery → Content Strategy → Subagents → Visual Bible → Slides → Speaker Notes → Website → QA → Delivery

最重要的行為規則：進入 Production Mode 後，不逐頁要求使用者確認。
