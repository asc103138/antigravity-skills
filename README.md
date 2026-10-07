# antigravity-skills

🚀 Antigravity 全域技能與規則集中同步庫（搭配 chezmoi 實現多設備一鍵配置與適性化同步）。

---

## 📌 專案特色

1. **跨電腦隨身同步**：透過 `chezmoi` 將全套 Antigravity 教學、行政、開發技能無痛套用到任意 macOS 或 Linux 電腦。
2. **適性化配置**：支援 chezmoi 模板與一鍵安裝腳本，自動偵測環境並設定 `~/.gemini/config/skills` 與 `~/.gemini/config/rules`。
3. **安全去識別化**：所有私密 Token、個人真實手機號碼與機密設定已預先脫敏，並提供安全設定範本。

---

## 💻 快速開始：在其他電腦一鍵同步

在任何全新的電腦終端機中，只需執行以下指令：

### 1. 安裝 chezmoi（若尚未安裝）
```bash
# macOS (Homebrew)
brew install chezmoi

# 或直接使用官方一鍵腳本 (macOS / Linux 不需要 root)
sh -c "$(curl -fsLS get.chezmoi.io)" -- -b ~/.local/bin
```

### 2. 初始化並套用技能
```bash
# 初始化並套用 (將自動下載此 repo 並同步到 ~/.gemini/config/)
chezmoi init --apply asc103138/antigravity-skills
```

套用後，`~/.gemini/config/skills` 與 `~/.gemini/config/rules` 即會自動建立並放入所有技能！

---

## 🔄 本機更新與推播（維護流程）

當您在主要工作電腦上新增或修改技能後：

```bash
# 1. 執行同步腳本更新 dot_gemini
./scripts/sync_local_to_repo.sh

# 2. 提交並推送到 GitHub
git add .
git commit -m "feat: 更新全域技能與規範"
git push origin main
```

在其他電腦只需執行：
```bash
chezmoi update
```

---

## 🛠️ MCP 服務設定說明

為了安全性，本 Repo 不包含私密 Token。同步完成後，若需啟用 MCP 服務（如 Netlify, Canva, Firebase）：
1. 複製範本檔：
   ```bash
   cp ~/.gemini/config/mcp_config.json.template ~/.gemini/config/mcp_config.json
   ```
2. 填入專屬 Token 即可。
