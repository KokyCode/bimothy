#!/usr/bin/env python
"""
Export all data from local database to JSON fixtures
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sa_doj.settings')
django.setup()

from django.core.management import call_command
import json

# Export all data
print("Exporting data from local database...")

# Export all models
fixtures = [
    'intelligence.Gang',
    'intelligence.GangMember',
    'intelligence.Incident',
    'intelligence.GangRelationship',
    'intelligence.CaseFile',
    'auth.User',  # Export users too
    'auth.Group',  # Export groups if any
    'contenttypes.ContentType',  # Needed for relationships
]

try:
    with open('data_export.json', 'w', encoding='utf-8') as f:
        call_command('dumpdata', *fixtures, natural_foreign=True, natural_primary=True, stdout=f, indent=2)
    
    print("Data exported to data_export.json")
    
    # Check file size
    file_size = os.path.getsize('data_export.json')
    print(f"Export file size: {file_size / 1024:.2f} KB")
    
    # Count records
    with open('data_export.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(f"Total records exported: {len(data)}")
        
        # Count by model
        counts = {}
        for item in data:
            model = item['model']
            counts[model] = counts.get(model, 0) + 1
        
        print("\nRecord counts by model:")
        for model, count in sorted(counts.items()):
            print(f"  {model}: {count}")
            
except Exception as e:
    print(f"Error exporting data: {e}")
    import traceback
    traceback.print_exc()

