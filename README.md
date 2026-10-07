# antigravity-skills

🚀 Antigravity 全域技能與規則集中同步庫（搭配 chezmoi 實現 Mac / Windows 多設備一鍵全自動偵測與適性化同步）。

---

## ⚡ 極速開始：在其他電腦「只要一行指令」！

在全新的電腦終端機貼上下列**單一指令**，腳本將自動：
1. **自動偵測並安裝 `chezmoi`**（無需手動下載或安裝 Homebrew）。
2. **免登入 GitHub** 直接拉取本公開 Repo。
3. **依作業系統自動適性化**配置 `mcp_config.json`（Windows 自動切換 `npx.cmd`，Mac 自動切換 `npx`）。
4. **自動同步**全套 26 個教學與開發技能至 `~/.gemini/config/skills`。

---

### 🍎 在 macOS 電腦（開啟 Terminal 貼上此行）：

```bash
curl -fsSL https://raw.githubusercontent.com/asc103138/antigravity-skills/main/bootstrap.sh | bash
```

---

### 🪟 在 Windows 電腦（開啟 PowerShell 貼上此行）：

```powershell
irm https://raw.githubusercontent.com/asc103138/antigravity-skills/main/bootstrap.ps1 | iex
```

---

## 📌 跨平台適性化對照表

本儲存庫透過 `chezmoi` 模板引擎，套用時會自動調適環境：

| 適性化維度 | 🍎 macOS (Darwin) | 🪟 Windows |
|---|---|---|
| **一鍵指令** | `curl ... bootstrap.sh \| bash` | `irm ... bootstrap.ps1 \| iex` |
| **MCP 指令** | `npx` / 原生 Binary | `npx.cmd` 自動切換 |
| **字型與排版** | 標楷體、蘋方、黑體（NFC 字串防錯） | 標楷體、微軟正黑體（Win 考卷格式防跑版）|
| **終端編碼** | 原生 UTF-8 | 自動引導切換 UTF-8 (`chcp 65001`) |

---

## 🔄 本機更新與維護流程

當您在主要開發電腦修改或新增技能後：

```bash
# 1. 執行同步腳本（自動過濾私密個資並更新 chezmoi 來源）
./scripts/sync_local_to_repo.sh

# 2. 提交並推送到 GitHub
git add .
git commit -m "feat: 更新技能"
git push origin main
```

在其他任何電腦（Mac 或 Windows）只需執行：
```bash
chezmoi update
```

---

## 🛠️ MCP 服務設定與金鑰補齊

1. 套用完成後，`~/.gemini/config/mcp_config.json` 已經根據您的 OS 就緒。
2. 若需啟用需 Token 認證的 MCP 服務（例如 Netlify）：
   - 開啟 `~/.gemini/config/mcp_config.json`，在該服務區塊補上自己的 API Token 即可。
