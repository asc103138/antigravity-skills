---
name: handdrawn-timetable
description: 手繪風課表生成器（仿「那隻水母」課表風格）。說「課表手繪風」「那隻水母風格」「小朋友課表」時載入。讀取課表 PDF（每格一行文字），生成果奶油底＋手繪格線＋塗鴉的高解析 PNG。
---

# 手繪風課表生成器（那隻水母風格）

複製 2026-08-25 為「一年庚班課表」自製的生成流程。成品範例：
`C:\Users\ccps\Desktop\一年庚班課表_115上_手繪風.png`

## 風格要素

- 奶油底 `#F6EEDA`＋棕色墨線 `#6C5F52`（3.5px、圓角 10px）
- 抖動濾鏡：SVG `feTurbulence`＋`feDisplacementMap scale=4.5`，掛在表格容器 → 手繪感
- TIMETABLE 氣泡標題（信號：`border:5px solid`、`border-radius:70px`）
- 塗鴉：水母（頭部圓頂＋波浪裙擺＋三根觸手）、星星（帶笑臉）、四角星火花、愛心、笑臉、`(◕‿◕)`
- 上午白格、下午米格 `#EBDCC4`、BREAK TIME 午休帶
- 字型：`fonts/ZCOOLKuaiLe-Regular.ttf`＋`fonts/MaShanZheng-Regular.ttf`（Google Fonts，license：OFL）

## 使用步驟

1. 先檢查課表 PDF 是「每格一行」格式（`pymupdf` `get_text().splitlines()`）
2. 執行 `gen2.py`（編輯檔頭 `PDF`、`OUT` 路徑；`SUBJECTS`/`TEACHERS` 集合依各校課表調整）
3. Chrome headless 渲染（2x 高解析）：

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 --window-size=1180,2000 --screenshot="<out.png>" "file:///.../schedule2.html"
```

4. Pillow 裁切白邊＋輸出桌面

## 已知陷阱

- 午休 row 佔一個 index：節次編號用 `idx+1 if idx<4 else idx`，否則午休後會 6/7/8 跳號
- 空格的塗鴉（笑臉）與課程格（愛心）要錨定在正確的 matrix index（break=4，P5=5）
- raw.githubusercontent 下載字型很慢，timeout 開 150s 以上
- Chrome 固定以 body 寬度對齊視窗，左右會留白邊，截圖後用 `ImageChops.difference().getbbox()` 自動裁

## 輸出規格

- PNG：window-size × 2（deviceScaleFactor）為單位，最後 bbox 裁切
- Obsidian 歸檔：`C:\opencode\Obsidian vault\創作庫\<檔名>.png`＋更新 `115上_一年庚班課表_海報.md`
