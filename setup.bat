@echo off
echo ========================================
echo  SA-DOJ Intelligence System Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

echo [1/7] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo Error: Failed to create virtual environment
    pause
    exit /b 1
)

echo [2/7] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/7] Upgrading pip...
python -m pip install --upgrade pip

echo [4/7] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo [5/7] Creating database migrations...
python manage.py makemigrations
if errorlevel 1 (
    echo Error: Failed to create migrations
    pause
    exit /b 1
)

echo [6/7] Applying migrations...
python manage.py migrate
if errorlevel 1 (
    echo Error: Failed to apply migrations
    pause
    exit /b 1
)

echo [7/7] Creating static files directory...
if not exist "static\css" mkdir static\css

echo.
echo ========================================
echo  Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Create a superuser account:
echo    python manage.py createsuperuser
echo.
echo 2. Start the development server:
echo    python manage.py runserver
echo.
echo 3. Access the system at:
echo    http://127.0.0.1:8000/
echo.
echo 4. Access admin panel at:
echo    http://127.0.0.1:8000/admin/
echo.
pause

