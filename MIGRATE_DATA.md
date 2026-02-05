# Data Migration Guide

## Export Data from Local Database

1. Run the export script locally:
   ```bash
   python export_data.py
   ```

This creates `data_export.json` with all your data.

## Import Data to Railway Production

### Option 1: Using Railway CLI (Recommended)

1. Make sure `data_export.json` is committed and pushed to git
2. Wait for Railway to deploy
3. Run the import command:
   ```bash
   railway run --service grapestreetcripsdoj python import_data.py
   ```

### Option 2: Using Railway Dashboard

1. Go to your Railway project
2. Click on your service
3. Go to "Deployments" tab
4. Click on the latest deployment
5. Click "Run Command"
6. Enter: `python import_data.py`
7. Click "Run"

### Option 3: One-time Command

1. In Railway dashboard, go to your service
2. Settings → Deploy
3. Add a one-time command: `python import_data.py`

## What Gets Migrated

- All Gangs (26)
- All Gang Members (12)
- All Incidents (11)
- All Gang Relationships (46)
- All Case Files (27)
- All Users (7)

## Notes

- The import will skip objects that already exist (based on primary keys)
- User accounts will be imported but passwords will need to be reset
- Images/media files need to be uploaded separately if needed

