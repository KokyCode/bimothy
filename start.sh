#!/bin/bash

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

show_menu() {
    clear
    echo -e "${CYAN}========================================"
    echo "  SAN ANDREAS DOJ INTELLIGENCE SYSTEM"
    echo "========================================"
    echo -e "${NC}"
    echo "  [1] Setup System (First Time)"
    echo "  [2] Start Server"
    echo "  [3] Create Admin Account"
    echo "  [4] Add Sample Data"
    echo "  [5] Open in Browser"
    echo "  [6] Database Management"
    echo "  [7] Exit"
    echo ""
    echo "========================================"
    read -p "Select option (1-7): " choice
    
    case $choice in
        1) setup_system ;;
        2) start_server ;;
        3) create_admin ;;
        4) add_sample ;;
        5) open_browser ;;
        6) database_menu ;;
        7) exit_program ;;
        *) show_menu ;;
    esac
}

setup_system() {
    clear
    echo -e "${CYAN}========================================"
    echo "  SYSTEM SETUP"
    echo "========================================"
    echo -e "${NC}"
    bash setup.sh
    read -p "Press Enter to continue..."
    show_menu
}

start_server() {
    clear
    echo -e "${CYAN}========================================"
    echo "  STARTING SERVER"
    echo "========================================"
    echo -e "${NC}"
    echo "Server will start on: http://127.0.0.1:8000/"
    echo "Press CTRL+C to stop the server"
    echo ""
    source venv/bin/activate
    python manage.py runserver
    read -p "Press Enter to continue..."
    show_menu
}

create_admin() {
    clear
    echo -e "${CYAN}========================================"
    echo "  CREATE ADMIN ACCOUNT"
    echo "========================================"
    echo -e "${NC}"
    source venv/bin/activate
    python manage.py createsuperuser
    echo ""
    read -p "Press Enter to continue..."
    show_menu
}

add_sample() {
    clear
    echo -e "${CYAN}========================================"
    echo "  ADD SAMPLE DATA"
    echo "========================================"
    echo -e "${NC}"
    source venv/bin/activate
    python quickstart.py
    echo ""
    read -p "Press Enter to continue..."
    show_menu
}

open_browser() {
    clear
    echo -e "${CYAN}========================================"
    echo "  OPENING BROWSER"
    echo "========================================"
    echo -e "${NC}"
    
    if command -v xdg-open &> /dev/null; then
        xdg-open http://127.0.0.1:8000/
    elif command -v open &> /dev/null; then
        open http://127.0.0.1:8000/
    else
        echo "Please open http://127.0.0.1:8000/ in your browser"
    fi
    
    echo "Browser opened!"
    sleep 2
    show_menu
}

database_menu() {
    clear
    echo -e "${CYAN}========================================"
    echo "  DATABASE MANAGEMENT"
    echo "========================================"
    echo -e "${NC}"
    echo "  [1] Run Migrations"
    echo "  [2] Make Migrations"
    echo "  [3] Reset Database"
    echo "  [4] Backup Database"
    echo "  [5] Back to Main Menu"
    echo ""
    read -p "Select option (1-5): " dbchoice
    
    case $dbchoice in
        1) migrate_db ;;
        2) makemigrations_db ;;
        3) reset_db ;;
        4) backup_db ;;
        5) show_menu ;;
        *) database_menu ;;
    esac
}

migrate_db() {
    source venv/bin/activate
    python manage.py migrate
    read -p "Press Enter to continue..."
    database_menu
}

makemigrations_db() {
    source venv/bin/activate
    python manage.py makemigrations
    read -p "Press Enter to continue..."
    database_menu
}

reset_db() {
    echo ""
    echo -e "${RED}WARNING: This will delete all data!${NC}"
    read -p "Are you sure? (yes/no): " confirm
    
    if [ "$confirm" = "yes" ]; then
        rm db.sqlite3
        source venv/bin/activate
        python manage.py migrate
        echo -e "${GREEN}Database reset complete!${NC}"
    fi
    
    read -p "Press Enter to continue..."
    database_menu
}

backup_db() {
    mkdir -p backups
    timestamp=$(date +"%Y%m%d_%H%M%S")
    cp db.sqlite3 "backups/db_backup_$timestamp.sqlite3"
    echo -e "${GREEN}Backup created: backups/db_backup_$timestamp.sqlite3${NC}"
    read -p "Press Enter to continue..."
    database_menu
}

exit_program() {
    clear
    echo ""
    echo "Thank you for using SA-DOJ Intelligence System!"
    echo "Stay safe out there, agent!"
    echo ""
    sleep 2
    exit 0
}

# Start the menu
show_menu

