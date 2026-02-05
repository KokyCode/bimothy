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

print("Importing data into production database...")

try:
    # Load the data
    call_command('loaddata', 'data_export.json', verbosity=2)
    print("\nData import completed successfully!")
    
except Exception as e:
    print(f"Error importing data: {e}")
    import traceback
    traceback.print_exc()

