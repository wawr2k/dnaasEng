@echo OFF
setlocal

:: Clean old build files
echo [INFO] Cleaning old build files...
IF EXIST "dist" rd /s /q "dist" 2>nul
IF EXIST "build" rd /s /q "build" 2>nul

:: Check if py command is available
where py >nul 2>&1
if errorlevel 1 (
    echo Python launcher (py) not found. Please ensure Python is installed.
    pause
    exit /b 1
)

echo Installing requirements...
py -m pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install requirements.
    pause
    exit /b 1
)

:: Generate timestamp (format: yyyyMMddHHmm)
for /f %%i in ('powershell -Command "Get-Date -Format 'yyyyMMddHHmm'"') do set timestamp=%%i

:: Build and add timestamp to filename
echo Building executable...
py -m PyInstaller --onedir --add-data "resources;resources/" src/main.py -n dnaas

if errorlevel 1 (
    echo Failed to run PyInstaller.
    pause
    exit /b 1
)

copy CHANGES_LOG.md dist\dnaas\

if errorlevel 1 (
    echo Failed to copy CHANGES_LOG.md
    pause
    exit /b 1
)

:: Package dist/dnaas into zip file
powershell -Command "Compress-Archive -Path 'dist\dnaas' -DestinationPath 'dist\dnaas_%timestamp%.zip' -Force"

if errorlevel 1 (
    echo Failed to create zip file
    pause
    exit /b 1
)

echo Successfully created dist\dnaas_%timestamp%.zip

echo Script finished.
pause
endlocal