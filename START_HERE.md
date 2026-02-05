# 🚀 GETTING STARTED - SA-DOJ Intelligence System

## Welcome, Agent!

You've just received the **San Andreas Department of Justice Intelligence System** - a professional control panel for managing gang activity on your GTA 5 roleplay server.

---

## ⚡ Super Quick Start (Windows)

1. **Double-click** `start.bat`
2. **Select option 1** to setup
3. **Select option 3** to create admin account
4. **Select option 4** to add sample data
5. **Select option 2** to start server
6. **Select option 5** to open in browser
7. **Done!** 🎉

---

## ⚡ Super Quick Start (Linux/Mac)

1. Open Terminal in this folder
2. Run: `chmod +x start.sh && ./start.sh`
3. Select option 1 to setup
4. Select option 3 to create admin account
5. Select option 4 to add sample data
6. Select option 2 to start server
7. Select option 5 to open in browser
8. Done! 🎉

---

## 📖 What You Get

### ✅ Complete System Features

1. **Secure Login System** - DOJ-themed authentication
2. **Dashboard** - Real-time gang activity overview
3. **Gang Intelligence** - Comprehensive gang database
4. **Member Profiles** - Detailed gang member tracking
5. **Territory Map** - Gang territory visualization
6. **Incident Reports** - Crime tracking and documentation
7. **Relationships** - Inter-gang relationship tracking
8. **Case Files** - Investigation management system
9. **System Settings** - Configuration and preferences

### ✅ Professional Design

- 🎨 Dark law enforcement theme
- 📱 Fully responsive (mobile, tablet, desktop)
- ⚡ Fast and optimized
- 🔒 Secure and production-ready
- 🎯 SEO optimized

### ✅ Easy to Use

- One-click setup scripts
- Sample data generator
- Interactive launcher menu
- Comprehensive documentation
- Clean admin interface

---

## 📂 Important Files

| File | Purpose |
|------|---------|
| `start.bat` / `start.sh` | **Main launcher** - Start here! |
| `README.md` | Full documentation |
| `QUICKSTART.md` | Quick start guide |
| `PROJECT_OVERVIEW.md` | Technical overview |
| `quickstart.py` | Sample data generator |
| `requirements.txt` | Python dependencies |

---

## 🎯 First Time Setup

### Option A: Using the Launcher (Recommended)

**Windows:** Double-click `start.bat`  
**Linux/Mac:** Run `./start.sh` in terminal

Then follow the menu:
1. Setup System (first time only)
2. Create Admin Account
3. Add Sample Data (optional)
4. Start Server
5. Open in Browser

### Option B: Manual Setup

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate it
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup database
python manage.py migrate

# 5. Create your account
python manage.py createsuperuser

# 6. Add sample data (optional)
python quickstart.py

# 7. Start server
python manage.py runserver
```

---

## 🌐 Accessing the System

Once the server is running:

- **Main System:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

### Default Test Account (if you used quickstart.py)
- **Username:** agent_smith
- **Password:** password123

---

## 📚 Documentation

1. **Start Here:** `QUICKSTART.md` - Quick start guide
2. **Full Docs:** `README.md` - Complete documentation
3. **Technical:** `PROJECT_OVERVIEW.md` - Project details

---

## 🎨 Customization

### Change Gang Colors
Admin Panel → Gangs → Edit → Color field (use hex codes like #FF0000)

### Add Your Server's Gangs
Admin Panel → Gangs → Add gang

### Upload Member Photos
Admin Panel → Gang members → Edit → Photo field

### Log Incidents
Admin Panel → Incidents → Add incident

### Create Cases
Admin Panel → Case files → Add case file

---

## 🆘 Troubleshooting

### Problem: "Python not found"
**Solution:** Install Python from python.org (version 3.8+)

### Problem: Port 8000 already in use
**Solution:** Run `python manage.py runserver 8080`

### Problem: CSS not loading
**Solution:** Check that `static/css/styles.css` exists

### Problem: Database errors
**Solution:** Delete `db.sqlite3` and run `python manage.py migrate` again

---

## 🎮 Using the System

### Adding a Gang
1. Go to Admin Panel
2. Click "Gangs"
3. Click "Add gang"
4. Fill in: Name, Tag, Color, Threat Level, Territory
5. Save

### Adding a Member
1. Go to Admin Panel
2. Click "Gang members"
3. Click "Add gang member"
4. Select gang, enter name, alias, rank
5. Set status and threat level
6. Save

### Logging an Incident
1. Go to Admin Panel
2. Click "Incidents"
3. Click "Add incident"
4. Enter title, type, location
5. Select involved gangs/members
6. Set severity
7. Save

### Creating a Case
1. Go to Admin Panel
2. Click "Case files"
3. Click "Add case file"
4. Enter case number and title
5. Select involved gangs
6. Assign lead agent
7. Set priority
8. Save

---

## 🔒 Security Notes

### Development (Current)
- Debug mode: ON
- Default database: SQLite
- Access: localhost only

### Production (When Going Live)
Update `sa_doj/settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = 'your-secure-key-here'
```

Use HTTPS and a production database (PostgreSQL recommended)

---

## 📊 Sample Data

If you ran `quickstart.py`, you'll have:
- 5 gangs (Ballas, Vagos, Families, Marabunta Grande, Lost MC)
- 9 gang members with ranks and threat levels
- Gang relationships (allies, rivals, at war)
- Sample incidents
- Sample case files
- Test agent account

---

## 🚀 Next Steps

1. ✅ **Explore the sample data** to understand the system
2. ✅ **Add your server's gangs** in the admin panel
3. ✅ **Upload member photos** for better visualization
4. ✅ **Start logging incidents** as they happen
5. ✅ **Create investigation cases** for ongoing work
6. ✅ **Train your DOJ team** on using the system
7. ✅ **Customize colors and branding** to match your server

---

## 💡 Pro Tips

1. **Use descriptive gang tags** (3-5 characters)
2. **Choose distinct colors** for each gang
3. **Update threat levels** regularly
4. **Document incidents thoroughly** for better tracking
5. **Link related cases** to incidents
6. **Back up your database** regularly
7. **Use the admin panel** for bulk operations

---

## 📞 Need Help?

1. Check `QUICKSTART.md` for common solutions
2. Read `README.md` for detailed documentation
3. Review `PROJECT_OVERVIEW.md` for technical details
4. Check Django documentation at docs.djangoproject.com

---

## 🎉 You're All Set!

The SA-DOJ Intelligence System is ready to use. Your roleplay server now has a professional, secure, and feature-rich gang intelligence system.

**Happy policing, Agent!** 🚔

---

## Quick Reference Card

```
🚀 Launch:        ./start.bat or ./start.sh
🌐 Web URL:       http://127.0.0.1:8000/
⚙️  Admin:         http://127.0.0.1:8000/admin/
📊 Sample Data:   python quickstart.py
🔄 Restart:       Ctrl+C then restart server
💾 Backup:        Copy db.sqlite3 file
📝 Docs:          README.md
🆘 Help:          QUICKSTART.md
```

---

**Built with ❤️ by Bring My Brand Online**  
*For GTA 5 Roleplay Servers*

🚔 *Protect and Serve San Andreas* 🚔

