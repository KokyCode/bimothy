#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sa_doj.settings')
django.setup()

from intelligence.models import Gang, GangMember, Incident, CaseFile
from django.db.models import Count

print("=== TESTING VIEW QUERIES ===")

# Test gang_intelligence query
print("\n1. Gang Intelligence Query:")
gangs = Gang.objects.filter(is_active=True).annotate(
    incident_count=Count('incidents')
).order_by('-threat_level', '-incident_count')
print(f"   Found {gangs.count()} active gangs")
if gangs.exists():
    for g in gangs[:3]:
        print(f"   - {g.name} (active={g.is_active}, incidents={g.incident_count})")

# Test member_profiles query
print("\n2. Member Profiles Query:")
members = GangMember.objects.filter(status='ACTIVE').select_related('gang')
print(f"   Found {members.count()} active members")
if members.exists():
    for m in members[:3]:
        print(f"   - {m.name} (status={m.status}, gang={m.gang.name})")

# Test incident_reports query
print("\n3. Incident Reports Query:")
incidents = Incident.objects.all().prefetch_related('gangs_involved', 'members_involved')
print(f"   Found {incidents.count()} total incidents")

# Test case_files query
print("\n4. Case Files Query:")
cases = CaseFile.objects.all().select_related('lead_agent')
print(f"   Found {cases.count()} total cases")
if cases.exists():
    for c in cases[:3]:
        print(f"   - {c.case_number}: {c.title} (lead={c.lead_agent})")

# Check for inactive gangs
print("\n5. Inactive Gangs:")
inactive = Gang.objects.filter(is_active=False)
print(f"   Found {inactive.count()} inactive gangs")

# Check all members regardless of status
print("\n6. All Members (any status):")
all_members = GangMember.objects.all()
print(f"   Found {all_members.count()} total members")
status_counts = {}
for m in all_members:
    status_counts[m.status] = status_counts.get(m.status, 0) + 1
print(f"   Status breakdown: {status_counts}")

