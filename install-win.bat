@echo off
REM
where poetry >nul 2>nul
if %errorlevel% neq 0 (
    echo Poetry is not found. Please install poetry and try again.
    exit /b
)

REM
where pipx >nul 2>nul
if %errorlevel% neq 0 (
    echo pipx is not found. Please install pipx and try again.
    exit /b
)

REM
pipx list | findstr assistant-bot >nul
if %errorlevel% equ 0 (
    echo assistant-bot is already installed.
    pause
    exit /b
)

echo Building distribution package with poetry...
poetry build

echo Installing the package with pipx...
for /f %%i in ('dir /b dist\*.whl') do set WHL_FILE=%%i
pipx install dist\%WHL_FILE%

echo Installation complete. You can now run the bot with the assistant-bot command from anywhere in the system.
pause
