# 逐頁 AI 生圖提示詞結構

每張獨立投影片使用同一套結構，再替換本頁內容。保持簡短；只補足能改善構圖、可讀性或角色一致性的資訊。

```text
Use case: productivity-visual
Asset type: standalone 16:9 horizontal educational slide image
Input images: Image 1: character identity reference; Image 2: style/layout reference (optional)
Primary request: <這一頁要讓觀眾看懂的核心訊息>
Scene/backdrop: <教室、研習場、教師桌或抽象但教育現場可理解的背景>
Subject: <教師、學生、AI 助教、教材或互動活動>
Style/medium: <clean educational technology keynote, soft glassmorphism, polished 3D cartoon or other locked style>
Composition/framing: <標題區、主視覺位置、卡片／流程／比較欄位、文字留白>
Lighting/mood: <溫暖、清楚、專業、鼓勵或提醒>
Color palette: <主色、輔色、提醒色；每頁不要彩虹化>
Text (verbatim): "<逐字繁中畫面文字>"
Constraints: <固定角色身份、16:9、文字可讀、只保留一個核心訊息>
Avoid: <錯字、filler text、pseudo-glyphs、watermark、霓虹賽博龐克、冷酷機器人、雜亂背景、密集小字>
```

## 角色身份參考的固定句

需要固定人物時加入：

```text
Image 1 is a character identity reference, not a background. Preserve the character's face, hair, outfit, outline, illustration quality, and color identity. Keep this same protagonist across the deck; vary only pose, expression, props, and scene.
```

## 參考圖的角色句

風格或排版參考只加入：

```text
Use the reference image only as a style/layout reference. Do not copy its text, logos, characters, or subject matter. Preserve the current slide's exact text and content.
```

## 文字與版型規則

- 標題最多兩行，優先使用短句。
- 比較頁用左右雙欄；流程頁用 4–7 個節點；實作頁保留任務卡與檢核空間。
- 圖像生成模型可能產生錯字；一次只修正一件事，例如「保留構圖與角色，只修正標題文字」。
- 不要為了塞入更多內容而縮小文字；內容太多就拆成下一頁。
