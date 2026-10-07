---
name: antigravity-exam-win-converter
description: 將 Mac 上製作的考卷（Word .docx、Pages 匯出檔、段考題庫）無損轉為 Windows 學校與教務處相容格式。當使用者提到「考卷轉檔」、「Mac考卷轉Windows」、「考卷跑版」、「考卷排版修復」、「考卷雙欄」、「出考卷」時載入此技能。
---

# Mac 考卷轉 Windows 完美相容轉檔技能（Antigravity 版）

解決教師在 Mac（Word for Mac / Pages / Google Docs）出題後，傳到學校 Windows 電腦或送印時發生的「**字型遺失、行距暴增、整頁溢出爆頁、公式亂碼、選擇題對不齊**」五大經典痛點。

---

## 核心解決之跨平台災難

| 痛點 | Mac 原生現象 | Windows 學校端災難 | 轉檔技能解法 |
|---|---|---|---|
| **1. 字型替換** | 蘋方 (PingFang)、黑體 (Heiti)、楷體-繁 | 找不到字型，強制 fallback 導致字距字形跑掉 | 自動深入 XML 替換為標準「標楷體」或「新細明體」，英數鎖定「Times New Roman」。 |
| **2. 格線陷阱** | 預設開啟 `snapToGrid`（貼齊格線） | Windows Word 網格計算不同，行距暴增 1.5~2 倍（2頁變4頁） | 強制注入 `w:snapToGrid="0"`，取消網格貼齊。 |
| **3. 行距鎖定** | 單行行距隨字體浮動 | 換電腦後每一題高度略變，最後一題被擠到次頁 | 強制段落為「固定行高」（Exact 18pt），段前段後留白歸零。 |
| **4. 版面規格** | A4 預設邊界較寬（2.54cm） | 試卷容題量不足、雙欄分隔線失蹤 | 支援標準 **A4 直式雙欄**（加分隔線、1.5cm緊湊邊界）與 **B4/A3 橫式雙折**。 |
| **5. 選項對齊** | 用多個「空白鍵」手動對齊 (A)(B)(C)(D) | Windows 字型等寬性不同，選項參差不齊歪七扭八 | 自動將連續空白轉換為標準製表定位點 (Tab stops)。 |
| **6. 暫存檔污染** | 壓縮包常夾帶 `__MACOSX`、`.DS_Store`、NFD | Windows 打開解壓出現幽靈檔案或檔名分解亂碼 | 清除 Mac 垃圾 metadata，檔名進行 Unicode NFC 正規化。 |

---

## 快速使用指令

工具腳本路徑：
`python <skill路徑>/scripts/exam_win_converter.py`

### 1. 單一考卷轉檔修復
```bash
python scripts/exam_win_converter.py convert \
  --input "未命名考卷_mac.docx" \
  --output "113-1_段考數學試卷_windows相容.docx" \
  --font-zh "標楷體" \
  --font-en "Times New Roman" \
  --line-spacing 18.0
```

### 2. 資料夾內全部考卷批次轉檔
```bash
python scripts/exam_win_converter.py batch \
  --input-dir "./mac_exams" \
  --output-dir "./win_exams" \
  --font-zh "標楷體"
```

### 3. 一鍵生成 Windows 標準雙欄考卷空白樣板
```bash
# 產生 A4 直式雙欄（最常見段考規格）
python scripts/exam_win_converter.py scaffold \
  --output "期末考卷_範本.docx" \
  --layout a4-double \
  --title "113學年度第一學期 第二次定期評量 數學科試卷" \
  --school "市立國民中學"

# 產生 B4 橫向雙折（大張雙折考卷）
python scripts/exam_win_converter.py scaffold \
  --output "B4雙折考卷_範本.docx" \
  --layout b4-double
```

---

## 參數說明

- `--font-zh`：中文主要字型（學校預設為 `標楷體`，若為理化/科技考卷可選 `新細明體` 或 `微軟正黑體`）。
- `--font-en`：英文與數字字型（預設 `Times New Roman`）。
- `--line-spacing`：固定行高 pt 值（考卷緊湊排版推薦 `17.0` ~ `19.0` pt，預設 `18.0` pt）。
- `--layout`：版面配置，可選 `a4-double`（A4 雙欄）、`b4-double`（B4 雙折）、`a4-single`（單欄隨堂測驗）。
- `--no-fix-tabs`：保留原始空白，不自動將選擇題選項空白轉為 Tab。
