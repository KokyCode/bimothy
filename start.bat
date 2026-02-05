@echo off
title SA-DOJ Intelligence System
color 0B

:menu
cls
echo ========================================
echo   SAN ANDREAS DOJ INTELLIGENCE SYSTEM
echo ========================================
echo.
echo   [1] Setup System (First Time)
echo   [2] Start Server
echo   [3] Create Admin Account
echo   [4] Add Sample Data
echo   [5] Open in Browser
echo   [6] Database Management
echo   [7] Exit
echo.
echo ========================================
set /p choice="Select option (1-7): "

if "%choice%"=="1" goto setup
if "%choice%"=="2" goto start
if "%choice%"=="3" goto admin
if "%choice%"=="4" goto sample
if "%choice%"=="5" goto browser
if "%choice%"=="6" goto database
if "%choice%"=="7" goto exit
goto menu

:setup
cls
echo ========================================
echo   SYSTEM SETUP
echo ========================================
echo.
call setup.bat
pause
goto menu

:start
cls
echo ========================================
echo   STARTING SERVER
echo ========================================
echo.
echo Server will start on: http://127.0.0.1:8000/
echo Press CTRL+C to stop the server
echo.
call venv\Scripts\activate.bat
python manage.py runserver
pause
goto menu

:admin
cls
echo ========================================
echo   CREATE ADMIN ACCOUNT
echo ========================================
echo.
call venv\Scripts\activate.bat
python manage.py createsuperuser
echo.
pause
goto menu

:sample
cls
echo ========================================
echo   ADD SAMPLE DATA
echo ========================================
echo.
call venv\Scripts\activate.bat
python quickstart.py
echo.
pause
goto menu

:browser
cls
echo ========================================
echo   OPENING BROWSER
echo ========================================
echo.
start http://127.0.0.1:8000/
echo Browser opened!
timeout /t 2
goto menu

:database
cls
echo ========================================
echo   DATABASE MANAGEMENT
echo ========================================
echo.
echo   [1] Run Migrations
echo   [2] Make Migrations
echo   [3] Reset Database
echo   [4] Backup Database
echo   [5] Back to Main Menu
echo.
set /p dbchoice="Select option (1-5): "

if "%dbchoice%"=="1" goto migrate
if "%dbchoice%"=="2" goto makemigrate
if "%dbchoice%"=="3" goto reset
if "%dbchoice%"=="4" goto backup
if "%dbchoice%"=="5" goto menu
goto database

:migrate
call venv\Scripts\activate.bat
python manage.py migrate
pause
goto database

:makemigrate
call venv\Scripts\activate.bat
python manage.py makemigrations
pause
goto database

:reset
echo.
echo WARNING: This will delete all data!
set /p confirm="Are you sure? (yes/no): "
if /i "%confirm%"=="yes" (
    del db.sqlite3
    call venv\Scripts\activate.bat
    python manage.py migrate
    echo Database reset complete!
)
pause
goto database

:backup
if not exist "backups" mkdir backups
set timestamp=%date:~-4%%date:~-7,2%%date:~-10,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set timestamp=%timestamp: =0%
copy db.sqlite3 backups\db_backup_%timestamp%.sqlite3
echo Backup created: backups\db_backup_%timestamp%.sqlite3
pause
goto database

:exit
cls
echo.
echo Thank you for using SA-DOJ Intelligence System!
echo Stay safe out there, agent!
echo.
timeout /t 2
exit

