# 🚔 San Andreas DOJ Intelligence System

A professional Django-based control panel for managing gang intelligence on a GTA 5 roleplay server. Designed specifically for the San Andreas Department of Justice to monitor gang activity, track incidents, and manage investigations.

![Version](https://img.shields.io/badge/version-2.5-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## ✨ Features

### 🔐 Secure Login System
- DOJ agent authentication
- Restricted access control
- Session management with automatic timeout
- Professional law enforcement themed interface

### 📊 Dashboard
- Real-time statistics overview
- Active gang monitoring
- Recent incident tracking
- Priority case management
- System activity logs

### 🎯 Gang Intelligence
- Comprehensive gang database
- Threat level classification (Low, Medium, High, Critical)
- Member count tracking
- Territory information
- Color-coded gang identification
- Incident correlation

### 👤 Member Profiles
- Detailed gang member profiles
- Alias and rank tracking
- Photo management
- Criminal record documentation
- Known associates linking
- Status tracking (Active, Inactive, Wanted, Incarcerated, Deceased)
- Threat level assessment

### 🗺️ Territory Map
- Gang territory visualization
- Interactive mapping (framework ready)
- Color-coded territories
- Territory conflict tracking

### 📋 Incident Reports
- Comprehensive incident logging
- Severity classification
- Gang involvement tracking
- Location and time documentation
- Status management (Open, Investigating, Closed)
- Evidence documentation

### 🔗 Gang Relationships
- Inter-gang relationship tracking
- Relationship types: Allied, Neutral, Rival, At War
- Network visualization (framework ready)
- Historical relationship notes

### 📁 Case Files
- Investigation case management
- Case number tracking
- Priority system (Low, Medium, High, Urgent)
- Lead agent assignment
- Team collaboration features
- Multi-gang case support

### ⚙️ System Settings
- User preferences
- System information
- Security settings
- Data management tools

## 🛠️ Technology Stack

- **Backend:** Django 4.2
- **Database:** SQLite (development) / PostgreSQL (production ready)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Design:** Custom law enforcement theme with dark UI
- **Responsive:** Mobile, tablet, and desktop optimized

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone or Download

```bash
cd Bim
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create your DOJ agent account.

### Step 7: Run Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## 🎮 Usage

### First Login

1. Navigate to `http://127.0.0.1:8000/`
2. Enter your DOJ Agent ID (username)
3. Enter your Security Passcode (password)
4. Click "ACCESS SYSTEM"

### Adding Data

#### Via Admin Panel (Recommended for Initial Setup)

1. Navigate to `http://127.0.0.1:8000/admin/`
2. Log in with your superuser credentials
3. Add gangs, members, incidents, relationships, and cases

#### Via Django Shell (Advanced)

```bash
python manage.py shell
```

```python
from intelligence.models import Gang, GangMember

# Create a gang
gang = Gang.objects.create(
    name="Los Santos Vagos",
    tag="LSV",
    color="#FFD700",
    threat_level="HIGH",
    member_count=15,
    territory="East Los Santos, Rancho area"
)

# Create a gang member
member = GangMember.objects.create(
    gang=gang,
    name="Carlos Rodriguez",
    alias="Loco",
    rank="Lieutenant",
    status="ACTIVE",
    threat_level="HIGH"
)
```

## 🎨 Design Features

### Color Scheme
- **Primary Background:** Dark navy (#0a0e1a)
- **Secondary Background:** Darker slate (#141822)
- **Accent Colors:** Cyan (#00d4ff), Blue (#3498db)
- **Status Colors:**
  - Critical: Red (#c0392b)
  - High: Orange (#e67e22)
  - Medium: Gold (#f39c12)
  - Low: Green (#27ae60)

### Responsive Design
- Mobile-first approach
- Breakpoints: 480px, 768px, 1200px
- Touch-friendly interface
- Collapsible sidebar on mobile

### UI Components
- Animated login screen
- Real-time clock display
- Status indicators
- Color-coded threat levels
- Interactive cards with hover effects
- Professional badges and tags

## 📊 Database Models

### Gang
- Name, tag, color
- Threat level
- Territory information
- Member count
- Founded date
- Activity status

### GangMember
- Personal information
- Gang affiliation
- Criminal record
- Known associates
- Status tracking
- Threat assessment

### Incident
- Title and description
- Type classification
- Severity level
- Location and timestamp
- Gang/member involvement
- Status tracking
- Evidence documentation

### GangRelationship
- Inter-gang relationships
- Relationship types
- Historical notes

### CaseFile
- Case management
- Priority levels
- Agent assignments
- Investigation tracking
- Multi-gang support

## 🔒 Security Features

- Django's built-in authentication
- CSRF protection
- Password hashing
- Session timeout (1 hour)
- Login required decorators
- Secure admin panel

## 🚀 Deployment

### Railway Deployment (Recommended)

This application is configured for easy deployment on Railway. See `RAILWAY_DEPLOYMENT.md` for detailed instructions.

**Quick Start:**
1. Push your code to GitHub/GitLab
2. Create a new project on Railway
3. Connect your repository
4. Add environment variables (see `RAILWAY_DEPLOYMENT.md`)
5. Add PostgreSQL database service
6. Deploy!

Railway will automatically:
- Install dependencies
- Run migrations
- Collect static files
- Start the application

### Other Deployment Options

#### For Production (Manual)

1. **Update settings.py:**
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`
   - Use strong `SECRET_KEY` (via environment variable)
   - Configure database (PostgreSQL recommended)

2. **Static Files:**
   ```bash
   python manage.py collectstatic
   ```

3. **Use HTTPS:**
   - Obtain SSL certificate
   - Configure reverse proxy (Nginx/Apache)

4. **Database:**
   - Switch to PostgreSQL or MySQL
   - Regular backups
   - Database optimization

5. **Server:**
   - Use Gunicorn or uWSGI
   - Set up supervisor for process management
   - Configure firewall

## 📱 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🛣️ Future Enhancements

- [ ] Interactive territory map with real GTA 5 locations
- [ ] Real-time notifications
- [ ] Advanced search and filtering
- [ ] Export reports (PDF/Excel)
- [ ] API for external integrations
- [ ] Activity timeline visualization
- [ ] Advanced analytics dashboard
- [ ] Multi-user chat/notes system
- [ ] Document upload for evidence
- [ ] Integration with Discord bot

## 📝 License

This project is created for roleplay purposes on GTA 5 servers. Feel free to modify and use for your own server.

## 🤝 Support

For issues or questions:
1. Check the Django documentation
2. Review the code comments
3. Test in the admin panel first
4. Check browser console for errors

## 👨‍💻 Development

### Project Structure

```
Bim/
├── manage.py
├── requirements.txt
├── README.md
├── sa_doj/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── intelligence/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/
│   └── intelligence/
│       ├── base.html
│       ├── login.html
│       ├── dashboard.html
│       ├── gang_intelligence.html
│       ├── member_profiles.html
│       ├── territory_map.html
│       ├── incident_reports.html
│       ├── relationships.html
│       ├── case_files.html
│       ├── system_settings.html
│       └── includes/
│           ├── sidebar.html
│           └── topbar.html
└── static/
    └── css/
        └── styles.css
```

### Adding New Features

1. Create models in `intelligence/models.py`
2. Create views in `intelligence/views.py`
3. Add URL patterns in `intelligence/urls.py`
4. Create templates in `templates/intelligence/`
5. Add styling in `static/css/styles.css`
6. Run migrations

### Custom Management Commands

```bash
# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Open Django shell
python manage.py shell
```

## 🎯 SEO Optimization

The application includes:
- Semantic HTML5 structure
- Meta tags ready for implementation
- Fast loading times
- Mobile optimization
- Clean URL structure
- Accessible navigation

## ⚡ Performance

- Optimized database queries with `select_related()` and `prefetch_related()`
- CSS animations using GPU acceleration
- Minimal JavaScript dependencies
- Efficient template rendering
- Static file caching

## 🎨 Customization

### Changing Colors

Edit `static/css/styles.css` in the `:root` section:

```css
:root {
    --primary-bg: #0a0e1a;
    --accent-cyan: #00d4ff;
    /* Add your custom colors */
}
```

### Adding New Pages

1. Create view in `intelligence/views.py`
2. Add URL in `intelligence/urls.py`
3. Create template in `templates/intelligence/`
4. Add navigation link in `sidebar.html`

---

**Developed for San Andreas DOJ Roleplay Server**

*Stay safe out there, agents.* 🚔

