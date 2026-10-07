---
name: antigravity-draw
description: 在 Antigravity 中進行 AI 生圖與視覺素材產出。當使用者提到「生圖」、「畫圖」、「產生圖片」、「繪圖」、「圖片生成」、「插圖」時載入此技能。
---

# AI 生圖技能（Antigravity 版）

本技能指引如何在 Antigravity 中產出高品質視覺素材、教學插圖與簡報配圖。

---

## 兩條生圖路線

| 路線 | 說明 | 需求 |
|---|---|---|
| **路線 A：Antigravity 內建生圖（推薦）** | 使用 Antigravity 原生生圖工具直接產圖，支援多種長寬比（1:1, 16:9, 4:3 等） | **無需任何外部 API Key** |
| **路線 B：OpenAI API 路線（備用）** | 使用 OpenAI `gpt-image-2` 模型或 `draw.py` 腳本批次生成 | 需設定 `OPENAI_API_KEY` |

---

## 路線 A：使用 Antigravity 內建生圖（優先使用）

直接在對話中描述圖片需求，Agent 會呼叫 `generate_image` 工具產出圖片：
- 支援長寬比：`1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `9:16`, `16:9`。
- 圖片產出後會儲存在專案或 Artifacts 目錄中。

---

## 路線 B：OpenAI API 路線

若需使用 OpenAI 進行進階生圖：

1. **設定 API Key**：
   在 `~/.openai.env` 儲存金鑰（切勿 commit 到 Git）：
   ```bash
   echo "OPENAI_API_KEY=sk-proj-你的金鑰" > ~/.openai.env
   ```
2. **安裝 openai 套件**：
   ```bash
   pip install openai
   ```
3. **執行生圖腳本**：
   可指定品質等級（`low`, `medium`, `high`，一般簡報或配圖預設使用 `low` 即可）。

---

## 結構化生圖提示詞範本（Prompt Template）

為了獲得最精準的圖片品質，建議依照以下格式提供或建構提示詞：

```text
生成一張圖片：
- 用途：教學簡報封面 / 概念插圖 / 網頁橫幅
- 尺寸比例：16:9（簡報） / 1:1（方形） / 4:3
- 主題：AI 代理與人類協同工作
- 畫面內容：一個溫馨的現代教室，老師與學生正在和發光的友善機器人討論程式碼
- 風格：扁平插畫風 / 水彩風 / 3D 渲染風 / 黑板粉筆風
- 色彩：明亮、溫暖的藍橘色調
- 文字：無文字（重要中文文字建議後製）
- 限制：避免複雜文字、畫面乾淨無雜訊
- 輸出位置：assets/cover.png
```

---

## 注意事項與安全原則

1. **中文文字處理**：生圖模型常出現文字拼寫或字形錯誤，重要文字建議由 Agent 產出無文字底圖後自行排版或後製。
2. **素材存放**：專案圖片建議統整存放於專案 `assets/` 目錄或 Obsidian 附件夾中。
3. **金鑰安全**：絕不將 API Key 寫入 Markdown、程式碼或 public repo。
