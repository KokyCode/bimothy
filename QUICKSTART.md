# 🚀 Quick Start Guide - SA-DOJ Intelligence System

## For Windows Users

### Step 1: Automatic Setup

Double-click `setup.bat` or run in PowerShell:

```powershell
.\setup.bat
```

This will:
- Create a virtual environment
- Install all dependencies
- Set up the database
- Create necessary folders

### Step 2: Create Your Admin Account

```bash
python manage.py createsuperuser
```

Enter your details:
- **Username:** Your DOJ Agent ID (e.g., agent_007)
- **Email:** Your email address
- **Password:** Choose a secure password

### Step 3: Add Sample Data (Optional)

```bash
python quickstart.py
```

This creates sample gangs, members, incidents, and cases for testing.

### Step 4: Start the Server

```bash
python manage.py runserver
```

### Step 5: Access the System

Open your browser and go to:
- **Main System:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

---

## For Linux/Mac Users

### Step 1: Make Setup Script Executable

```bash
chmod +x setup.sh
```

### Step 2: Run Setup

```bash
./setup.sh
```

### Step 3: Create Your Admin Account

```bash
python manage.py createsuperuser
```

### Step 4: Add Sample Data (Optional)

```bash
python quickstart.py
```

### Step 5: Start the Server

```bash
python manage.py runserver
```

### Step 6: Access the System

- **Main System:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

---

## Manual Setup (If Automated Setup Fails)

### 1. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
```

### 5. Run Server

```bash
python manage.py runserver
```

---

## First Time Login

1. Navigate to http://127.0.0.1:8000/
2. You'll see the **SAN ANDREAS DOJ** login screen
3. Enter your credentials:
   - **DOJ AGENT ID:** Your username
   - **SECURITY PASSCODE:** Your password
4. Click **ACCESS SYSTEM**

---

## Adding Your Own Data

### Via Admin Panel (Easiest Method)

1. Go to http://127.0.0.1:8000/admin/
2. Log in with your superuser account
3. Click on any section to add data:
   - **Gangs** - Add gang organizations
   - **Gang Members** - Add individual gang members
   - **Incidents** - Report new incidents
   - **Gang Relationships** - Define relationships between gangs
   - **Case Files** - Create investigation cases

### Via Django Shell (Advanced)

```bash
python manage.py shell
```

```python
from intelligence.models import Gang, GangMember

# Create a gang
gang = Gang.objects.create(
    name="Your Gang Name",
    tag="TAG",
    color="#FF0000",
    threat_level="HIGH",
    member_count=10,
    territory="Territory description"
)

# Create a member
member = GangMember.objects.create(
    gang=gang,
    name="Member Name",
    alias="Nickname",
    rank="Rank",
    status="ACTIVE",
    threat_level="MEDIUM"
)
```

---

## Troubleshooting

### Problem: "python is not recognized"

**Solution:** Install Python from [python.org](https://python.org) and make sure to check "Add Python to PATH" during installation.

### Problem: Port 8000 is already in use

**Solution:** Use a different port:
```bash
python manage.py runserver 8080
```

### Problem: CSS not loading

**Solution:** Make sure the `static/css/` folder exists and contains `styles.css`

### Problem: Permission errors on Linux/Mac

**Solution:** 
```bash
chmod +x setup.sh
chmod +x manage.py
```

### Problem: Database errors

**Solution:** Delete `db.sqlite3` and run migrations again:
```bash
rm db.sqlite3  # or del db.sqlite3 on Windows
python manage.py migrate
python manage.py createsuperuser
```

---

## System Features Overview

### 📊 **Dashboard**
- Real-time statistics
- Recent incidents
- Priority cases
- Critical gangs
- System activity

### 🎯 **Gang Intelligence**
- View all active gangs
- Threat level indicators
- Member counts
- Territory information
- Incident tracking

### 👤 **Member Profiles**
- Detailed member information
- Photos and aliases
- Criminal records
- Status tracking
- Threat assessments

### 🗺️ **Territory Map**
- Gang territories
- Color-coded zones
- Territory descriptions

### 📋 **Incident Reports**
- Log new incidents
- Track investigations
- Severity levels
- Gang involvement
- Evidence documentation

### 🔗 **Relationships**
- Allied gangs
- Rival gangs
- At war status
- Neutral relationships

### 📁 **Case Files**
- Investigation management
- Priority tracking
- Agent assignments
- Case documentation

### ⚙️ **System Settings**
- User preferences
- System information
- Security settings

---

## Tips for Best Experience

1. **Use Chrome or Firefox** for best compatibility
2. **Add realistic data** for better roleplay experience
3. **Keep threat levels updated** to prioritize activities
4. **Document incidents thoroughly** for better tracking
5. **Update gang relationships** as situations change
6. **Use the admin panel** for bulk data management
7. **Regular backups** - copy your `db.sqlite3` file

---

## Default Test Account (if you used quickstart.py)

- **Username:** agent_smith
- **Password:** password123

**Remember to change this password in production!**

---

## Next Steps

1. ✅ Customize gang colors and information
2. ✅ Add your server's specific gangs
3. ✅ Upload member photos
4. ✅ Start logging incidents
5. ✅ Create investigation cases
6. ✅ Define gang relationships
7. ✅ Train your DOJ team on the system

---

## Need Help?

1. Check the main `README.md` for detailed documentation
2. Review Django's official documentation
3. Check the code comments for implementation details
4. Test features in the admin panel first

---

**Welcome to the SA-DOJ Intelligence System!**

*Protect and Serve San Andreas* 🚔

