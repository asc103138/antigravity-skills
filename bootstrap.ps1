# ==============================================================================
# Antigravity 全域技能與環境一鍵配置腳本 (Windows PowerShell)
# Repo: https://github.com/asc103138/antigravity-skills
# 完全免登入 GitHub，一鍵安裝 chezmoi 並自動適性化套用全域技能與規則
# ==============================================================================

$ErrorActionPreference = "Stop"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "🚀 正在為 Windows 本機配置 Antigravity 全域技能與環境..." -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

# 1. 檢查或自動安裝 chezmoi
if (-not (Get-Command "chezmoi" -ErrorAction SilentlyContinue)) {
    Write-Host "📦 未偵測到 chezmoi，正在自動下載安裝..." -ForegroundColor Yellow
    
    # 優先嘗試 winget
    if (Get-Command "winget" -ErrorAction SilentlyContinue) {
        winget install twpayne.chezmoi --accept-source-agreements --accept-package-agreements
    } elseif (Get-Command "scoop" -ErrorAction SilentlyContinue) {
        scoop install chezmoi
    } else {
        # 官方免套件管理員直接下載安裝腳本
        $installScript = Invoke-RestMethod -Uri "https://get.chezmoi.io/ps1"
        Invoke-Expression $installScript
    }

    # 重新整理 PATH
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
}

Write-Host "  ✓ 偵測到 chezmoi 工具就緒" -ForegroundColor Green

# 2. 執行 chezmoi 初始化並套用 (公開 HTTPS，完全免登入)
Write-Host "🔄 正在從 GitHub 拉取技能庫並進行適性化同步..." -ForegroundColor Yellow
chezmoi init --apply https://github.com/asc103138/antigravity-skills.git --force

Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "🎉 全域技能與環境配置完成！" -ForegroundColor Green
Write-Host "📂 技能目錄：$HOME\.gemini\config\skills" -ForegroundColor Green
Write-Host "📜 全域規則：$HOME\.gemini\config\rules\curriculum-review-protocol.md" -ForegroundColor Green
Write-Host "⚙️ 平台設定：$HOME\.gemini\config\mcp_config.json (已切換為 npx.cmd)" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
