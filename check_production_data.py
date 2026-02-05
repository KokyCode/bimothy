#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sa_doj.settings')
django.setup()

from intelligence.models import Gang, GangMember, Incident, GangRelationship, CaseFile
from django.contrib.auth.models import User

print("=== PRODUCTION DATABASE CHECK ===")
print(f"Gangs: {Gang.objects.count()}")
print(f"Gang Members: {GangMember.objects.count()}")
print(f"Incidents: {Incident.objects.count()}")
print(f"Gang Relationships: {GangRelationship.objects.count()}")
print(f"Case Files: {CaseFile.objects.count()}")
print(f"Users: {User.objects.count()}")

if Gang.objects.count() > 0:
    print("\nSample Gang:")
    gang = Gang.objects.first()
    print(f"  - {gang.name} ({gang.tag})")
    
if CaseFile.objects.count() > 0:
    print("\nSample Case File:")
    case = CaseFile.objects.first()
    print(f"  - {case.case_number}: {case.title}")

