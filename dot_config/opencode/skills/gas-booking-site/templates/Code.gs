/**
 * 平板車預約 —— 後端
 * 資料欄位（分頁：預約）：
 *   A 提交時間 | B 週次 | C 星期 | D 節次 | E 班級 | F 用途
 */

const SHEET_NAME = '預約';

// ⚙️ 8 個班級代號
const CLASSES = ['四年甲班', '四年乙班', '四年丙班', '四年丁班', '四年戊班', '四年己班', '四年庚班', '四年辛班'];

// 節次（可自行增減）
const PERIODS = ['第1節', '第2節', '第3節', '第4節', '第5節', '第6節', '第7節'];
const BLOCKED_PERIODS = ['第5節', '第6節', '第7節'];
const SCHOOL_WEEK_START_ = Date.UTC(2026, 7, 30);
const SCHOOL_WEEK_COUNT_ = 21;

/** 有人打開網址 → 回傳網頁 */
function doGet(e) {
  return HtmlService.createHtmlOutputFromFile('index')
    .setTitle('平板車預約')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}

/** 回傳班級與節次，供前端使用 */
function getConfig() {
  return { classes: CLASSES, periods: PERIODS };
}

/** 星期一、星期三下午第 5～7 節無法預約 */
function isBlockedSlot_(weekday, period) {
  return (weekday === '星期一' || weekday === '星期三') &&
    BLOCKED_PERIODS.indexOf(period) !== -1;
}

function weekNumber_(week) {
  const match = /^第(\d+)週$/.exec(String(week));
  return match ? Number(match[1]) : 0;
}

function schoolWeekNumberToday_() {
  const now = new Date();
  const today = Date.UTC(now.getFullYear(), now.getMonth(), now.getDate());
  return Math.floor((today - SCHOOL_WEEK_START_) / (7 * 86400000)) + 1;
}

function isPastWeek_(week) {
  const number = weekNumber_(week);
  return number > 0 && number < schoolWeekNumberToday_();
}

/** 前端呼叫：一次寫入同一天的多個節次 */
function submitBookings(data) {
  const lock = LockService.getScriptLock();
  try { lock.waitLock(10000); } catch (err) {
    return { ok: false, error: '現在送出的人太多，請過幾秒再試' };
  }
  try {
    const week = String(data.week || '').trim();
    const weekday = String(data.weekday || '').trim();
    const inputPeriods = Array.isArray(data.periods) ? data.periods : [];
    const periods = inputPeriods.map(function (period) { return String(period).trim(); })
      .filter(function (period, index, list) { return period && list.indexOf(period) === index; });
    const className = String(data.className || '').trim();
    const purpose = String(data.purpose || '').trim().slice(0, 100);

    if (!week || !weekday || !periods.length || !className || !purpose) {
      return { ok: false, error: '週次、星期、節次、班級、用途都要填' };
    }
    if (periods.some(function (period) { return PERIODS.indexOf(period) === -1; })) {
      return { ok: false, error: '節次資料無效' };
    }
    if (weekNumber_(week) < 1 || weekNumber_(week) > SCHOOL_WEEK_COUNT_) {
      return { ok: false, error: '週次無效' };
    }
    if (isPastWeek_(week)) {
      return { ok: false, error: '已過去的週次不能預約' };
    }
    if (periods.some(function (period) { return isBlockedSlot_(weekday, period); })) {
      return { ok: false, error: '選取的節次中包含無法預約的時段' };
    }
    const sheet = getSheet_();
    // 先完整檢查，任何一節衝突就整批拒絕，避免只寫入部分節次。
    const rows = sheet.getDataRange().getValues();
    for (let p = 0; p < periods.length; p++) {
      for (let i = 1; i < rows.length; i++) {
        if (String(rows[i][1]) === week &&
            String(rows[i][2]) === weekday &&
            String(rows[i][3]) === periods[p]) {
          return { ok: false, error: periods[p] + '已被別的班級預約了，整批未送出' };
        }
      }
    }
    const timestamp = new Date();
    const values = periods.map(function (period) {
      return [timestamp, week, weekday, period, className, purpose];
    });
    sheet.getRange(sheet.getLastRow() + 1, 1, values.length, 6).setValues(values);
    return { ok: true, count: periods.length };
  } finally {
    lock.releaseLock();
  }
}

/** 前端呼叫：查詢某週的已預約清單 */
function getBookings(week) {
  const sheet = getSheet_();
  const rows = sheet.getDataRange().getValues();
  const out = [];
  for (let i = 1; i < rows.length; i++) {
    if (week && String(rows[i][1]) !== week) continue;
    out.push({
      week: String(rows[i][1]),
      weekday: String(rows[i][2]),
      period: String(rows[i][3]),
      className: String(rows[i][4]),
      purpose: String(rows[i][5])
    });
  }
  // 依節次排序
  out.sort(function (a, b) {
    return (PERIODS.indexOf(a.period) - PERIODS.indexOf(b.period));
  });
  return out;
}

/** 前端呼叫：依班級列出我的預約 */
function myBookings(className) {
  const sheet = getSheet_();
  const rows = sheet.getDataRange().getValues();
  const out = [];
  for (let i = 1; i < rows.length; i++) {
    if (String(rows[i][4]) === String(className)) {
      out.push({
        week: String(rows[i][1]),
        weekday: String(rows[i][2]),
        period: String(rows[i][3]),
        className: String(rows[i][4]),
        purpose: String(rows[i][5])
      });
    }
  }
  out.sort(function (a, b) {
    if (a.week !== b.week) return a.week < b.week ? -1 : 1;
    const weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五'];
    return weekdays.indexOf(a.weekday) - weekdays.indexOf(b.weekday);
  });
  return out;
}

/** 取消功能已關閉，保留函式以拒絕舊版前端或外部請求 */
function cancelBooking(className, week, weekday, period) {
  return { ok: false, error: '目前不開放取消預約，請聯絡管理者' };
}

/** 前端呼叫：只修改用途，不修改預約時段 */
function modifyBooking(data) {
  const lock = LockService.getScriptLock();
  try { lock.waitLock(10000); } catch (err) {
    return { ok: false, error: '現在送出的人太多，請過幾秒再試' };
  }
  try {
    const className = String(data.className || '');
    const week = String(data.week || '').trim();
    const weekday = String(data.weekday || '').trim();
    const period = String(data.period || '').trim();
    const purpose = String(data.purpose || '').trim().slice(0, 100);
    if (!className || !week || !weekday || !period || !purpose) {
      return { ok: false, error: '資料不完整' };
    }
    const sheet = getSheet_();
    const rows = sheet.getDataRange().getValues();
    let targetRow = -1;
    for (let i = 1; i < rows.length; i++) {
      if (String(rows[i][4]) === className &&
          String(rows[i][1]) === week &&
          String(rows[i][2]) === weekday &&
          String(rows[i][3]) === period) { targetRow = i + 1; break; }
    }
    if (targetRow === -1) return { ok: false, error: '找不到這筆預約' };
    sheet.getRange(targetRow, 6).setValue(purpose);
    return { ok: true };
  } finally {
    lock.releaseLock();
  }
}

/** 內部用：拿到工作表，沒有就自動建一個並補上標題列 */
function getSheet_() {
  // 路線 A（從試算表的「擴充功能」開的）用這行：
  const ss = SpreadsheetApp.getActiveSpreadsheet();

  // 路線 B（從 script.google.com 開的獨立腳本）改成這行，並填入你的試算表 ID：
  // const ss = SpreadsheetApp.openById('把試算表 ID 貼在這裡');

  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    sheet.appendRow(['提交時間', '週次', '星期', '節次', '班級', '用途']);
  } else if (sheet.getLastRow() <= 1) {
    // 新表尚無資料時，將舊版標題更新成週次格式。
    sheet.getRange(1, 1, 1, 6).setValues([['提交時間', '週次', '星期', '節次', '班級', '用途']]);
  }
  return sheet;
}

/** 只給老師手動執行一次，用來觸發授權畫面（見步驟五） */
function 一鍵授權() {
  const sheet = getSheet_();
  Logger.log('工作表就緒：' + sheet.getName() + '，目前有 ' + (sheet.getLastRow() - 1) + ' 筆資料');
}
