#!/usr/bin/env python
"""
Verify data is accessible via the same queries views use
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sa_doj.settings')
django.setup()

from intelligence.models import Gang, GangMember, Incident, CaseFile
from django.db.models import Count

print("=== VERIFYING DATA FOR VIEWS ===\n")

# Gang Intelligence View
print("1. Gang Intelligence (is_active=True):")
gangs = Gang.objects.filter(is_active=True).annotate(incident_count=Count('incidents'))
print(f"   Count: {gangs.count()}")
for g in gangs[:5]:
    print(f"   - {g.name} (active={g.is_active})")

# Member Profiles View  
print("\n2. Member Profiles (status='ACTIVE'):")
members = GangMember.objects.filter(status='ACTIVE')
print(f"   Count: {members.count()}")
for m in members[:5]:
    print(f"   - {m.name} (status={m.status})")

# Incident Reports View
print("\n3. Incident Reports (all):")
incidents = Incident.objects.all()
print(f"   Count: {incidents.count()}")
for i in incidents[:5]:
    print(f"   - {i.title}")

# Case Files View
print("\n4. Case Files (all):")
cases = CaseFile.objects.all()
print(f"   Count: {cases.count()}")
for c in cases[:5]:
    print(f"   - {c.case_number}: {c.title}")

print("\n=== DATA VERIFICATION COMPLETE ===")

