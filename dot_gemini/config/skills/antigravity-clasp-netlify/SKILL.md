---
name: antigravity-clasp-netlify
description: 使用 Clasp 雲端部署與 Netlify MCP 自動化建立「自訂前端網頁 + Google Sheets 資料庫 (GAS Web App API) + Netlify 託管」的零複製雙向閉環系統。當使用者提到「clasp 部署」、「Netlify 發佈」、「雙向閉環」、「網頁接試算表」、「clasp netlify」時載入此技能。
---

# Clasp 雲端部署 ＋ Netlify MCP 零複製雙向閉環網頁系統

本技能指引 AI Agent 如何透過 **Clasp CLI** 與 **Netlify MCP**，以純指令方式全自動建立「現代化前端網頁（Netlify 託管）＋ Google Sheets 資料庫（經由 Google Apps Script Web App API 對接）」的無伺服器完整閉環系統。

---

## 核心架構與分工

```
[使用者瀏覽器]
       │ (HTTPS Fetch / POST)
       ▼
[Netlify 託管前端網頁] (HTML / CSS / JS)
       │ (JSON 跨域請求)
       ▼
[Google Apps Script Web App] (doGet / doPost)
       │ (SpreadsheetApp 原生讀寫)
       ▼
[Google Sheets 雲端資料庫] (試算表紀錄)
```

---

## 一、 先備條件與安全注意事項

1. **環境依賴**：本機已安裝 `Node.js`、`npm`、`git` 與 `@google/clasp`（`clasp --version`）。
2. **帳號準備**：使用者擁有 Google 帳號與 Netlify 帳號。
3. **敏感資料防護（極重要）**：
   - **嚴禁**將 Netlify Personal Access Token、GitHub Token 或任何 Google OAuth 憑證硬編碼於程式碼或公開 Git Repo。
   - API 網址與專案 ID 於執行期間動態生成並注入前端。

---

## 二、 本地檔案準備規則（避坑關鍵）

在執行雲端部署前，專案目錄中必須具備以下檔案架構：

1. **`.claspignore`（第一道防線）**：
   專案根目錄必須明確排除所有前端網頁檔案，**僅允許推送後端檔案**：
   ```
   **/*
   !gas_code.js
   !appsscript.json
   ```
   > ⚠️ **避坑警示**：若前端 HTML/JS 檔案未被忽略而被推送到 GAS 雲端，GAS 伺服器會因缺少瀏覽器 DOM 環境報錯 `ReferenceError: document is not defined` 導致後端崩潰。

2. **`appsscript.json`（Manifest 配置）**：
   必須配置 `webapp` 欄位以允許公開存取：
   ```json
   {
     "timeZone": "Asia/Taipei",
     "dependencies": {},
     "exceptionLogging": "STACKDRIVER",
     "runtimeVersion": "V8",
     "webapp": {
       "executeAs": "USER_DEPLOYING",
       "access": "ANYONE_ANONYMOUS"
     }
   }
   ```
   > ⚠️ **避坑警示**：`clasp create-script` 執行時會自動生成預設的 `appsscript.json` 並覆蓋本地設定，請務必在 push 之前檢查或重新補回 `webapp` 區塊！

3. **`gas_code.js`（後端 API 主程式）**：
   負責實作 `doGet(e)` 與 `doPost(e)`，並透過 `PropertiesService` 自動記錄並綁定 Google 試算表 ID。

4. **前端網頁檔案**：
   包含 `index.html`、`css/`、`js/`。連線 JS 需留有 API 預留空字串（如 `const GAS_API_URL = "YOUR_GAS_API_URL_HERE";`），以便後續動態注入。

---

## 三、 自動化部署標準六步驟

### 步驟 1：檢查並安裝 Clasp
```bash
clasp --version || npm install -g @google/clasp
```

### 步驟 2：Google 帳號授權登入
```bash
clasp login
```
*Agent 行動*：從終端輸出抓取 `🔑 Authorize clasp by visiting this url: ...` 連結，呈現給使用者點擊進行瀏覽器授權。

### 步驟 3：創建 GAS 雲端專案
```bash
clasp create-script --title "專案資料庫名稱" --type standalone
```

### 步驟 4：強制推送與發佈 Web App
1. 確認本地 `.claspignore` 與 `appsscript.json` 包含 `webapp` 配置。
2. 強制推送到 GAS：
   ```bash
   clasp push -f
   ```
3. 發佈新版本 Web App：
   ```bash
   clasp create-deployment --description "Production Web App"
   ```

### 步驟 5：動態獲取與注入 API 網址
執行以下指令取得真實 Web App URL：
```bash
clasp open-web-app <deploymentId> --json
```
*Agent 行動*：取回傳 JSON 之 `url`（格式為 `https://script.google.com/macros/s/<deploymentId>/exec`），將該 URL 注入前端 JavaScript 的 `GAS_API_URL` 變數中。**切勿自行手動拼湊網址**。

### 步驟 6：Netlify 全自動網頁發佈
透過 Netlify MCP 執行：
1. **建立專案**：呼叫 `netlify-project-services-updater`（`create-new-project`），取得 `site_id`。
2. **上傳部署**：呼叫 `netlify-deploy-services-updater`（`deploy-site`），填入 `siteId` 與本地前端資料夾路徑。
3. **解除訪客存取限制**：若有 SSO 限制，呼叫 `netlify-project-services-updater`（`update-visitor-access-controls`），將 `requireSSOTeamLogin: false` 設為公開存取。
4. 輸出最終 Netlify 公開線上網址給使用者。

---

## 四、 六大經典踩坑與應變對策

| 踩坑情境 | 發生原因 | 解決對策 |
|---|---|---|
| **1. Apps Script API 未啟用** | Google 帳號預設關閉 API 存取 | 引導使用者至 [Apps Script 使用者設定頁面](https://script.google.com/home/usersettings)，將 **Google Apps Script API** 切換為 **開啟 (ON)**。 |
| **2. 前端檔案推送到 GAS** | 缺少 `.claspignore` 或規則錯誤 | 在 `.claspignore` 設置 `**/*` 與 `!gas_code.js`，修改後端代碼後執行 `clasp push -f` 徹底覆蓋雲端舊檔。 |
| **3. 首次執行需要存取權 (Authorization Required)** | 腳本需在擁有者雲端硬碟建立試算表 | **擁有者必須在線上編輯器手動執行一次函數**：點開編輯器 ➔ 選擇 `testAuthorization` ➔ 點擊「執行」➔ 完成「進階 ➔ 前往專案 ➔ 允許」。 |
| **4. `appsscript.json` 遺失 `webapp`** | `clasp create-script` 覆蓋了本地設定 | 建立專案後，重新寫入包含 `webapp` 的 `appsscript.json`，再執行 `clasp push -f` 與 `clasp create-deployment`。 |
| **5. Netlify 部署出現 401 驗證阻擋** | 專案預設啟用了團隊 SSO 登入 | 呼叫 `update-visitor-access-controls`，將 `requireSSOTeamLogin` 設為 `false`，即可完全公開。 |
| **6. Google 多帳號 Session 衝突** | 瀏覽器同時登入多個 Google 帳號 | 前端測試時請使用者使用**無痕視窗（Incognito）**開啟網址，即可完全避開多帳號衝突。 |
