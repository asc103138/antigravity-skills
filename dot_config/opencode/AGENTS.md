# 內部工具包常駐規則（file-toolkit，全域生效）

本機已安裝「內部工具包 三合一」（文件處理／影音／語音）。以下規則**每個工作階段自動生效**，使用者不需要再指定要用哪個技能。

## 文件處理（A 段）

- 若資料夾內有 `.venv`（尤其 `ai-agent-ep03\.venv`），所有 Python 程式一律用該直譯器：
  - Windows：`<專案>\.venv\Scripts\python.exe`
  - macOS/Linux：`.venv/bin/python`
- 禁止全域 `pip install`；套件一律裝進專案 `.venv`。
- 只裝 `requirements-core.txt` 的標配 10 項；選配套件要使用者明確點名才裝。
- 安裝或修環境後，一律跑 `verify_core.py`，看到 `CORE_OK: 10/10` 才算完成。
- 下載套件很慢（連官方 PyPI 卡住）時，改用鏡像：
  `--index-url https://mirrors.aliyun.com/pypi/simple/`
- 讀 PDF／Word／Excel／PPT 等檔案：先用 PyMuPDF／markitdown 抽內容，直接看圖失敗時改用座標抽取（pdfplumber）重建表格。

## 影音工具（B 段）

- `yt-dlp`／`ffmpeg`／`deno` 是系統工具（winget 裝），不要用 pip 裝進 `.venv`。
- yt-dlp 加 `--print` 時必須同時加 `--no-simulate`，否則不會真的下載。
- 下載前先 `yt-dlp --list-subs` 確認影片有沒有字幕。

## 語音（C 段）

- `edge-tts` 已用 `uv tool install` 安裝；指令找不到時先刷新 PATH 或改用 `python -m edge_tts`。
- 播放一律行內播放（PowerShell `System.Windows.Media.MediaPlayer`），禁止 `Start-Process` 開播放器視窗。
- 台灣中文建議聲音：`zh-TW-YunJheNeural`（男聲，唸結論）。

## 技能文件

- 完整技能說明：`C:\Users\ccps\.config\opencode\skills\opencode-file-toolkit\SKILL.md`
- 使用者說「裝內部工具包」「裝檔案處理工具」「裝影音」「裝語音」「讓 agent 會說話」等關鍵字時，載入該技能。

## 全域設定與技能同步（chezmoi，全員生效）

本機已安裝並初始化 chezmoi（dotfiles 管理工具），source 目錄：`C:\Users\ccps\.local\share\chezmoi`。**任何全域設定或技能建置前後，都要用 chezmoi 同步**：

- 修改全域設定（`opencode.json`、`~/.config/opencode/AGENTS.md`、全域 skills 等）後，立刻：
  ```powershell
  chezmoi add C:\Users\ccps\.config\opencode
  chezmoi git add -A
  chezmoi git commit -m "<說明>"
  chezmoi git push
  ```
- **每次 session 開始（開工）或處理任何與設定相關的工作時，先跑 `chezmoi update`**——把遠端最新版本拉回本地，避免多台電腦互相覆蓋。
- 遠端備份在 GitHub 私有 repo：`https://github.com/yuan0123ting/dotfiles`（origin）。
- 換新電腦搬移時：新機先裝 chezmoi → `chezmoi init --apply https://github.com/yuan0123ting/dotfiles.git` → 開新終端驗證全域設定與 skills 已就位。
- 若所在環境還沒初始化：先 `chezmoi init` 建立 source repo，再納入檔案。
- 相關工作：裝新工具、改全域設定、建置／更新技能、調整 opencode 設定時，視為「全域層級變更」，走本流程。