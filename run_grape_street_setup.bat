@echo off
echo ========================================
echo   GRAPE STREET SYSTEM SETUP
echo ========================================
echo.

cd /d "%~dp0"

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Running Grape Street setup...
echo.

python setup_grape_street.py

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo You can now start the server with:
echo   start.bat (Option 2 - Start Server)
echo.
echo Or manually:
echo   venv\Scripts\activate.bat
echo   python manage.py runserver
echo.
pause

