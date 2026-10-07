---
name: antigravity-github
description: 在 Antigravity 連接與操作 GitHub CLI 與 Git 工作流程。當使用者提到「連接 GitHub」、「設定 GitHub」、「登入 GitHub」、「git 設定」、「建立 GitHub repo」時載入此技能。
---

# 連接與操作 GitHub（Antigravity 版）

本技能指引如何在 Antigravity 中配置 GitHub CLI（`gh`）與 Git 環境，支援版本控制、建立儲存庫、Push/Commit 與 GitHub Pages 設定。

---

## 步驟一：檢查 Git 與 GitHub CLI

在終端機中檢查工具是否已安裝：

```bash
git --version
gh --version
```

若未安裝：
- macOS：`brew install git gh`

---

## 步驟二：登入 GitHub CLI

檢查目前的登入狀態：

```bash
gh auth status
```

若尚未登入，執行網頁授權登入：

```bash
gh auth login --web --git-protocol https
```

1. 終端機會顯示 8 碼一次性驗證碼。
2. 瀏覽器自動開啟（或手動開啟 `https://github.com/login/device`）。
3. 輸入驗證碼並確認授權。
4. 回到終端機再次執行 `gh auth status` 確認登入成功。

---

## 步驟三：設定 Git 全域使用者資訊

檢查現有設定：

```bash
git config --global user.name
git config --global user.email
```

若未設定或需變更：

```bash
git config --global user.name "你的名字"
git config --global user.email "your-email@example.com"
```

> [!TIP]
> 若不想在公開 Commit 中暴露私人 Email，可使用 GitHub 提供之 `用戶ID+用戶名@users.noreply.github.com`。

---

## 步驟四：驗證流程（可選測試 Repo）

若需驗證完整的 Commit 與 Push 流程：

```bash
mkdir -p ~/Documents/antigravity-github-test
cd ~/Documents/antigravity-github-test
git init
echo "# Antigravity GitHub 測試" > README.md
git add README.md
git commit -m "建立 Antigravity GitHub 測試"
gh repo create antigravity-github-test --private --source=. --push
```

驗證後如欲清理測試 Repo：

```bash
gh repo delete antigravity-github-test --yes
rm -rf ~/Documents/antigravity-github-test
```

---

## 安全守則

- **不要外流 Token**：切勿將 GitHub Personal Access Token (PAT) 或任何憑證寫入 `AGENTS.md`、`SKILL.md` 或程式碼中。
- **審慎提交**：在 Commit 前務必先檢視 `git status` 與 `git diff`，禁止無差別執行 `git add .`。
