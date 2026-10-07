# antigravity-skills

🚀 Antigravity 全域技能與規則集中同步庫（搭配 chezmoi 實現 Mac / Windows 多設備自動偵測與適性化同步）。

---

## 📌 跨平台適性化特色 (macOS & Windows)

本儲存庫透過 `chezmoi` 模板引擎（Template Engine），在不同作業系統下套用時會**自動偵測並調適環境**：

| 適性化維度 | 🍎 macOS (Darwin) | 🪟 Windows |
|---|---|---|
| **MCP 指令調用** | `npx` / 原生 Binary | `npx.cmd` 自動切換 |
| **Python 環境** | 優先偵測 `python3` / `uv` | 自動對齊 Windows `python` |
| **中文字型與排版** | 標楷體、蘋方、黑體（NFC 字串防錯） | 標楷體、微軟正黑體（Win 考卷格式防跑版）|
| **路徑處理** | POSIX 標準路徑 (`/`) | Windows 路徑相容處理 |
| **終端編碼** | 原生 UTF-8 | 自動引導切換 UTF-8 (`chcp 65001`) |

---

## 💻 快速開始：在各平台一鍵同步

在目標電腦打開終端機（macOS 使用 Terminal，Windows 使用 PowerShell 或 Windows Terminal）：

### 🍎 在 macOS 上的安裝與同步步驟

```bash
# 1. 安裝 chezmoi（若尚未安裝）
brew install chezmoi
# 或使用免 root 腳本：
sh -c "$(curl -fsLS get.chezmoi.io)" -- -b ~/.local/bin

# 2. 一鍵初始化並套用所有技能
chezmoi init --apply asc103138/antigravity-skills
```

---

### 🪟 在 Windows 上的安裝與同步步驟

```powershell
# 1. 安裝 chezmoi（以 winget 或 scoop）
winget install twpayne.chezmoi
# 或使用 scoop：
scoop install chezmoi

# 2. 一鍵初始化並套用所有技能
chezmoi init --apply asc103138/antigravity-skills
```

> [!NOTE]
> 套用完成後，chezmoi 會自動產生適合當前作業系統的 `~/.gemini/config/mcp_config.json` 與適性化指引文件 `~/.gemini/config/README_PLATFORM.md`！

---

## 🔄 本機更新與維護流程

當您在主要開發電腦修改或新增技能後：

```bash
# 1. 執行同步腳本（自動過濾私密個資並更新 chezmoi 來源）
./scripts/sync_local_to_repo.sh

# 2. 提交並推送到 GitHub
git add .
git commit -m "feat: 更新全域技能與跨平台適性化設定"
git push origin main
```

在其他任何電腦（Mac 或 Windows）只需執行：
```bash
chezmoi update
```

---

## 🛠️ MCP 服務設定與金鑰補齊

1. 套用完成後，`~/.gemini/config/mcp_config.json` 已經根據您的 OS（Windows 自動使用 `npx.cmd`，macOS 使用 `npx`）就緒。
2. 若需啟用需 Token 認證的 MCP 服務（例如 Netlify）：
   - 開啟 `~/.gemini/config/mcp_config.json`，在該服務區塊補上自己的 API Token 即可。
