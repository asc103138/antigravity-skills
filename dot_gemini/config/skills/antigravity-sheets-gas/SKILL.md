---
name: antigravity-sheets-gas
description: 用 Google 試算表當資料庫、Apps Script 網頁應用程式當後端，建立具有資料持久化能力的客製化網頁。當使用者提到「用試算表存資料」、「GAS 後端」、「表單收資料」、「讓網頁能存東西」、「課堂回饋牆」、「線上報名表」時載入此技能。
---

# Google Sheets ＋ Apps Script 網頁應用程式技能（Antigravity 版）

本技能指引如何以 Google 試算表作為資料庫、Google Apps Script (GAS) 網頁應用程式（Web App）同時作為後端與前端，打造**關掉網頁後依然記得資料**的互動應用。

---

## 核心優勢：為什麼走 Web App 路線而非 clasp / GitHub Pages

1. **全程零安裝**：無需安裝 Node.js、clasp 或任何本地工具，在任何電腦皆可執行。
2. **避免 CORS 跨域問題**：前端與後端整合在同一個 Apps Script 專案中，透過 `google.script.run` 進行內部通訊，完全不觸發瀏覽器 CORS 預檢。
3. **學校與教育帳號友善**：不依賴第三方應用程式授權，避免學校網管的 `admin_policy_enforced` 限制。
4. **改版網址不變**：部署更新時選擇「新版本」，公開網址與 QR Code 完全維持不變。

---

## 動手前先確認：你真的需要寫程式嗎？

當使用者表示想做「收資料的網頁」時，Agent **應先確認以下三題**：

| 情境 | 建議方向 |
|---|---|
| 僅需要基本問卷、報名表、收集意見，無需自訂複雜介面 | **直接使用 Google 表單**，零程式碼，回覆自動進試算表。 |
| 需要數十人「即時同步」搶答、即時跳動排行榜、即時文字雲 | GAS 無法支援高併發 WebSocket 即時同步，建議改走 Firebase 或 Supabase。 |
| 需要自訂網頁 UI、按鈕互動、且填寫資料需妥善儲存以供日後查詢 | ✅ **適用本技能（Sheets + GAS）**。 |

---

## 標準開發與部署流程

### 步驟一：建立資料庫試算表

1. 開啟 [Google Sheets](https://sheets.google.com)，新增一份試算表（例如「課堂回饋資料庫」）。
2. 將工作表分頁命名為 **`回覆`**。
3. 在第一列建立欄位標題，第一欄務必保留為時間戳記：
   `時間`、`暱稱`、`內容`

---

### 步驟二：開啟 Apps Script 編輯器

在該試算表中點選功能表：**擴充功能 → Apps Script**（此為容器綁定腳本，程式碼可直接存取本試算表，無需額外填寫試算表 ID）。

---

### 步驟三：提供後端程式碼 `Code.gs`

由 Agent 產出並提供使用者貼入編輯器中：

```javascript
/**
 * 試算表 Web App 後端
 */
function doGet(e) {
  return HtmlService.createHtmlOutputFromFile('index')
    .setTitle('課堂回饋系統')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}

function submitData(payload) {
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName('回覆') || ss.getActiveSheet();
    var timestamp = new Date();
    sheet.appendRow([timestamp, payload.nickname || '匿名', payload.content || '']);
    return { success: true };
  } catch (err) {
    return { success: false, error: err.toString() };
  }
}
```

---

### 步驟四：提供前端程式碼 `index.html`

在 Apps Script 編輯器中新增 HTML 檔案，命名為 `index`：

```html
<!DOCTYPE html>
<html>
<head>
  <base target="_top">
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 min-h-screen p-6 flex flex-col items-center">
  <div class="max-w-md w-full bg-white rounded-xl shadow-md p-6">
    <h1 class="text-xl font-bold text-gray-800 mb-4">課堂回饋牆</h1>
    <form id="feedbackForm" class="space-y-4" onsubmit="handleSend(event)">
      <div>
        <label class="block text-sm font-medium text-gray-700">暱稱 / 座號</label>
        <input type="text" id="nickname" required class="w-full mt-1 p-2 border rounded-lg focus:ring-2 focus:ring-blue-500">
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700">回饋內容</label>
        <textarea id="content" required rows="3" class="w-full mt-1 p-2 border rounded-lg focus:ring-2 focus:ring-blue-500"></textarea>
      </div>
      <button type="submit" id="submitBtn" class="w-full bg-blue-600 text-white py-2 rounded-lg font-medium hover:bg-blue-700">送出回饋</button>
    </form>
    <div id="statusMsg" class="mt-4 text-center text-sm font-medium hidden"></div>
  </div>

  <script>
    function handleSend(e) {
      e.preventDefault();
      const btn = document.getElementById('submitBtn');
      const msg = document.getElementById('statusMsg');
      btn.disabled = true;
      btn.innerText = '傳送中...';
      
      const payload = {
        nickname: document.getElementById('nickname').value,
        content: document.getElementById('content').value
      };

      google.script.run
        .withSuccessHandler(function(res) {
          btn.disabled = false;
          btn.innerText = '送出回饋';
          msg.classList.remove('hidden', 'text-red-600');
          msg.classList.add('text-green-600');
          msg.innerText = '✅ 送出成功！';
          document.getElementById('feedbackForm').reset();
        })
        .withFailureHandler(function(err) {
          btn.disabled = false;
          btn.innerText = '送出回饋';
          msg.classList.remove('hidden', 'text-green-600');
          msg.classList.add('text-red-600');
          msg.innerText = '❌ 發生錯誤：' + err;
        })
        .submitData(payload);
    }
  </script>
</body>
</html>
```

---

### 步驟五：部署為網頁應用程式（重要設定）

1. 點擊編輯器右上角 **部署 → 新增部署作業**。
2. 種類選擇 **網頁應用程式**。
3. 設定：
   - **執行身分**：`我（你的 Google 帳號）`
   - **誰可以存取**：`所有人（包括匿名者）`（確保學生或填表人無需登入即可開啟）。
4. 授權存取：依畫面指示核准權限。
5. 取得 `/exec` 結尾的網址，即可公開分享或產生 QR Code。

> [!IMPORTANT]
> **更新程式碼時**：點擊「部署 → 管理部署作業 → 編輯（筆的圖示） → 版本選擇【新版本】 → 部署」，網址永遠保持相同！

---

## 安全守則

- **個資去識別化**：表單僅收集暱稱、班級代號或座號，嚴禁收集學生身分證字號、真名或家長聯絡電話。
- **防止洩漏**：切勿將包含私人試算表 ID 的程式碼直接公開上傳。
