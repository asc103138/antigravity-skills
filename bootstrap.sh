#!/usr/bin/env bash
set -e

# ==============================================================================
# Antigravity 全域技能與環境一鍵配置腳本 (macOS / Linux)
# Repo: https://github.com/asc103138/antigravity-skills
# 完全免登入 GitHub，一鍵安裝 chezmoi 並自動適性化套用全域技能與規則
# ==============================================================================

echo "============================================================"
echo "🚀 正在為本機配置 Antigravity 全域技能與環境..."
echo "============================================================"

# 1. 確保 ~/.local/bin 存在並加入目前 PATH
mkdir -p "$HOME/.local/bin"
export PATH="$HOME/.local/bin:/opt/homebrew/bin:$PATH"

# 2. 檢查或自動安裝 chezmoi
if ! command -v chezmoi >/dev/null 2>&1; then
    echo "📦 未偵測到 chezmoi，正在自動下載安裝..."
    if command -v brew >/dev/null 2>&1; then
        brew install chezmoi
    else
        sh -c "$(curl -fsLS get.chezmoi.io)" -- -b "$HOME/.local/bin"
    fi
    echo "  ✓ chezmoi 安裝完成"
else
    echo "  ✓ 偵測到既有 chezmoi: $(chezmoi --version | head -n 1)"
fi

# 3. 確保 shell 設定檔 (zshrc / bashrc) 包含 ~/.local/bin
SHELL_RC=""
if [ -n "$ZSH_VERSION" ] || [ -f "$HOME/.zshrc" ]; then
    SHELL_RC="$HOME/.zshrc"
elif [ -f "$HOME/.bashrc" ]; then
    SHELL_RC="$HOME/.bashrc"
fi

if [ -n "$SHELL_RC" ]; then
    if ! grep -q 'HOME/.local/bin' "$SHELL_RC" 2>/dev/null; then
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_RC"
    fi
fi

# 4. 執行 chezmoi 初始化並套用 (公開 HTTPS，完全免登入)
echo "🔄 正在從 GitHub 拉取技能庫並進行適性化同步..."
chezmoi init --apply https://github.com/asc103138/antigravity-skills.git --force

echo ""
echo "============================================================"
echo "🎉 全域技能與環境配置完成！"
echo "📂 技能目錄：$HOME/.gemini/config/skills"
echo "📜 全域規則：$HOME/.gemini/config/rules/curriculum-review-protocol.md"
echo "⚙️ 平台設定：$HOME/.gemini/config/mcp_config.json"
echo "============================================================"
