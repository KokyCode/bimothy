#!/usr/bin/env python
"""
Import data from JSON fixture into production database
Run this on Railway after uploading data_export.json
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sa_doj.settings')
django.setup()

from django.core.management import call_command
from intelligence.models import Gang

print("Importing data into production database...")

# Check if data already exists
existing_gangs = Gang.objects.count()
if existing_gangs > 0:
    print(f"Database already has {existing_gangs} gangs. Skipping import to avoid duplicates.")
    print("If you want to re-import, clear the database first.")
else:
    try:
        # Load the data
        call_command('loaddata', 'data_export.json', verbosity=2)
        print("\nData import completed successfully!")
        
        # Verify
        gangs = Gang.objects.count()
        print(f"Verification: {gangs} gangs now in database")
        
    except Exception as e:
        print(f"Error importing data: {e}")
        import traceback
        traceback.print_exc()

