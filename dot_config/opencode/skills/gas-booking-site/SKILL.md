---
name: gas-booking-site
description: Use when the user asks for a Google Apps Script booking, borrowing, reservation, schedule, or class timetable website, or asks to reuse the tablet-cart booking site with different classes, weeks, periods, restrictions, content, or theme.
---

# GAS 預約網站技能

這是一套可重用的 Google Sheets + Apps Script 網頁預約骨架。未來類似需求優先沿用 `templates/Code.gs` 與 `templates/index.html`，只修改設定內容，不重新設計整套後端。

## 目前模板功能

- Google 試算表分頁：`預約`
- `Code.gs` + `index.html`，不使用 clasp
- 自訂學校週次；目前模板為第 1～21 週
- 一週顯示星期一～星期五課表
- 同一週、同一天可一次選取多個節次
- 任何一節衝突時，整批預約拒絕，不留下半批資料
- 過去週次不可新增或改期
- 可設定星期與節次的禁止預約格
- 預約單位為班級
- 用途必填
- 查詢既有預約
- 只允許修改用途；禁止取消預約
- GAS 後端使用 `LockService` 防止同時送出造成衝突
- 手機與平板使用響應式版面

## 觸發後的工作流程

1. 先讀取 `templates/CONFIG.md`，把使用者提供的內容對照到設定欄位。
2. 需求已明確時，不重新詢問已知內容；只確認會造成重做的缺口。
3. 產出檔案前確認儲存位置。若使用者未指定，先詢問，不自行決定。
4. 將兩個模板複製到使用者指定的輸出資料夾，檔名固定為 `Code.gs`、`index.html`。
5. 只修改「可替換內容」；保留鎖定、整批衝突檢查、禁止取消與資料欄位索引。
6. 說明使用者在試算表、Apps Script、授權與部署頁面上的操作。不能代替使用者操作 Google 帳號、授權或部署。
7. 改版時使用「管理部署作業 → 編輯 → 新版本 → 部署」，不要建立新部署以免網址改變。
8. 產出後檢查 `Code.gs` 與 `index.html` 的 API 名稱一致，尤其是 `submitBookings`、`getBookings`、`myBookings`、`modifyBooking`。

## 可替換內容

### 後端 `Code.gs`

- `SHEET_NAME`
- `CLASSES`
- `PERIODS`
- `BLOCKED_PERIODS`
- `SCHOOL_WEEK_START_`
- `SCHOOL_WEEK_COUNT_`
- 工作表標題列
- 送出錯誤訊息

### 前端 `index.html`

- 頁面標題與說明文字
- 班級清單與節次時間
- `SCHOOL_WEEK_START`、`SCHOOL_WEEK_COUNT`
- `BLOCKED_PERIODS`
- 海洋或其他主題色彩、背景動畫
- 用途欄位提示文字
- 是否顯示查詢與用途修改

## 不可自行改掉的安全規則

- 不把試算表 ID、帳號、密碼、部署網址或金鑰寫進模板。
- 試算表維持私有；網頁部署用「執行身分：我」。
- 保留 `LockService`。
- 批次預約必須先完整檢查所有節次，任何一節衝突就整批拒絕。
- 不收學生姓名、電話、身分證字號等不必要個資。
- 若使用者要求重新開放取消，必須同時修改前端與 `cancelBooking` 後端政策，不能只新增按鈕。
- 新增後端權限功能時，提醒使用者重新執行授權。

## 目前模板的資料欄位

工作表分頁 `預約` 第一列固定為：

```text
提交時間 | 週次 | 星期 | 節次 | 班級 | 用途
```

一個批次選取多節次會寫入多列，每列代表一個「週次＋星期＋節次」。

## 完成前檢查

- `Code.gs` 與 `index.html` 都存在。
- `index.html` 內的班級、週次、節次與後端設定一致。
- 禁止格在前端顯示「無法預約」，後端也會拒絕。
- 過去週次在前端停用，後端也會拒絕。
- 用途空白時前端與後端都拒絕。
- 多節次中任一格衝突時，整批不寫入。
- 查詢頁沒有取消按鈕，後端 `cancelBooking` 也拒絕取消。
- 行動版表格在自己的容器水平滑動，不撐破整個網頁。
- 部署網址使用 `/exec`，不是 `/dev`。

## 交付提醒

建立或修改全域技能、模板或其他 OpenCode 設定後，必須提醒使用者重新啟動 OpenCode，讓技能載入。技能檔本身不應保存任何私人部署網址或憑證。
