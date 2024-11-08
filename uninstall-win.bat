@echo off
REM
pipx list | findstr assistant-bot >nul
if %errorlevel% neq 0 (
    echo assistant-bot is not installed.
    pause
    exit /b
)

echo Uninstalling assistant-bot using pipx...
pipx uninstall assistant-bot

echo Uninstallation complete.
pause
