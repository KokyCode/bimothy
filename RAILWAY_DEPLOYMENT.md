# Railway Deployment Guide

This guide will help you deploy the SA-DOJ Intelligence System to Railway.

## Prerequisites

1. A Railway account (sign up at https://railway.app)
2. Git repository (GitHub, GitLab, or Bitbucket)
3. Your code pushed to the repository

## Step 1: Create a New Project on Railway

1. Go to https://railway.app and sign in
2. Click "New Project"
3. Select "Deploy from GitHub repo" (or your Git provider)
4. Choose your repository

## Step 2: Configure Environment Variables

In your Railway project dashboard, go to the "Variables" tab and add the following environment variables:

### Required Variables:

```
SECRET_KEY=your-secret-key-here-generate-a-random-one
DEBUG=False
ALLOWED_HOSTS=your-app-name.railway.app,*.railway.app
CSRF_TRUSTED_ORIGINS=https://your-app-name.railway.app
```

**Important:** Replace `your-app-name.railway.app` with your actual Railway domain. You can find this in your Railway project settings under "Domains" or in the service URL.

### Optional Variables:

```
SECURE_SSL_REDIRECT=True
```

### Generate a Secret Key:

You can generate a secure secret key using Python:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Or use this command:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Step 3: Add PostgreSQL Database (Recommended)

1. In your Railway project, click "New"
2. Select "Database" → "PostgreSQL"
3. Railway will automatically set the `DATABASE_URL` environment variable
4. The app will automatically use PostgreSQL when `DATABASE_URL` is set

## Step 4: Add Volume for Media Files (Optional but Recommended)

For persistent storage of uploaded images:

1. In your Railway project, click "New"
2. Select "Volume"
3. Name it "media" or similar
4. Add environment variable: `RAILWAY_VOLUME_MOUNT_PATH=/path/to/volume`

## Step 5: Deploy

Railway will automatically:
1. Detect your Django project
2. Install dependencies from `requirements.txt`
3. Run migrations
4. Collect static files
5. Start the application with Gunicorn

## Step 6: Create Admin User

After deployment, you'll need to create a superuser. You can do this via Railway's CLI or by adding a one-time command:

1. In Railway dashboard, go to your service
2. Click on "Settings" → "Deploy"
3. Add a one-time command: `python manage.py createsuperuser`
4. Or use Railway CLI: `railway run python manage.py createsuperuser`

## Step 7: Access Your Application

1. Railway will provide a URL like: `https://your-app-name.railway.app`
2. Visit the URL to access your application
3. Log in with the admin credentials you created

## Important Notes

### Static Files
- Static files are automatically collected and served via WhiteNoise
- No additional configuration needed

### Media Files
- If you added a volume, media files will persist
- Without a volume, media files will be lost on redeploy
- Consider using Railway's volume or an external storage service (S3, etc.) for production

### Database
- SQLite is used locally for development
- PostgreSQL is automatically used on Railway when `DATABASE_URL` is set
- Make sure to run migrations after deployment

### Security
- Never commit `SECRET_KEY` to your repository
- Always set `DEBUG=False` in production
- Use environment variables for sensitive data

## Troubleshooting

### Application won't start
- Check Railway logs for errors
- Verify all environment variables are set
- Ensure `requirements.txt` is up to date

### Static files not loading
- Check that `collectstatic` ran successfully
- Verify `STATIC_ROOT` is set correctly
- Check WhiteNoise middleware is in `MIDDLEWARE`

### Database errors
- Ensure PostgreSQL service is running
- Check `DATABASE_URL` is set correctly
- Run migrations: `railway run python manage.py migrate`

### Media files not saving
- Check volume is mounted correctly
- Verify `MEDIA_ROOT` path
- Check file permissions

## Railway CLI (Optional)

Install Railway CLI for easier management:
```bash
npm i -g @railway/cli
railway login
railway link
railway up
```

## Support

For Railway-specific issues, check:
- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway

For application issues, check the logs in Railway dashboard.

