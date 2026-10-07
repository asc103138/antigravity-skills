#!/usr/bin/env bash
set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_SKILLS="$HOME/.gemini/config/skills"
SOURCE_RULES="$HOME/.gemini/config/rules"

TARGET_SKILLS="$REPO_ROOT/dot_gemini/config/skills"
TARGET_RULES="$REPO_ROOT/dot_gemini/config/rules"

echo "==> 同步本機技能與規則到 chezmoi 目錄..."
mkdir -p "$TARGET_SKILLS" "$TARGET_RULES"

# 複製技能與規則
cp -R "$SOURCE_SKILLS"/* "$TARGET_SKILLS/"
if [ -d "$SOURCE_RULES" ]; then
    cp -R "$SOURCE_RULES"/* "$TARGET_RULES/"
fi

# 排除大檔案或暫存
rm -rf "$TARGET_SKILLS/steam-community-docs/references/templates/成果表_2欄排版範本.docx" 2>/dev/null || true

# 脫敏處理：過濾個人私密聯絡電話
python3 -c "
files = [
  '$TARGET_SKILLS/steam-community-docs/references/members.json',
  '$TARGET_SKILLS/steam-community-docs/scripts/members.json',
  '$TARGET_SKILLS/steam-community-docs/SKILL.md',
  '$TARGET_SKILLS/steam-community-docs/scripts/generate_docs.py'
]
for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()
        c = c.replace('0981455340', '0900000000')
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
    except Exception:
        pass
print('  ✓ 機敏個資脫敏完成')
"

echo "==> 同步完成！您可執行 git status 與 git commit 推送更新。"
