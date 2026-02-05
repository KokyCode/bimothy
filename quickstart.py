"""
Quick Start Script for SA-DOJ Intelligence System

This script helps you quickly set up sample data for testing the system.
Run this after completing the initial setup and creating a superuser.

Usage:
    python quickstart.py
"""

import os
import django
from datetime import datetime, timedelta
from random import choice, randint

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sa_doj.settings')
django.setup()

from django.contrib.auth.models import User
from intelligence.models import Gang, GangMember, Incident, GangRelationship, CaseFile

def create_sample_data():
    """Create sample gangs, members, and incidents for testing"""
    
    print("Creating sample data for SA-DOJ Intelligence System...\n")
    
    # Get or create a user for reports
    user, created = User.objects.get_or_create(
        username='agent_smith',
        defaults={
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'agent.smith@sa-doj.gov',
            'is_staff': True
        }
    )
    if created:
        user.set_password('password123')
        user.save()
        print(f"✓ Created user: {user.username}")
    
    # Sample gangs data
    gangs_data = [
        {
            'name': 'Los Santos Vagos',
            'tag': 'LSV',
            'color': '#FFD700',
            'threat_level': 'HIGH',
            'territory': 'East Los Santos, Rancho area, Cypress Flats',
            'member_count': 25,
            'description': 'Mexican street gang known for drug trafficking and territorial violence'
        },
        {
            'name': 'Ballas',
            'tag': 'BALLAS',
            'color': '#800080',
            'threat_level': 'CRITICAL',
            'territory': 'South Los Santos, Grove Street area, Davis',
            'member_count': 35,
            'description': 'One of the most dangerous gangs in LS, involved in weapons trafficking'
        },
        {
            'name': 'The Families',
            'tag': 'FAM',
            'color': '#00FF00',
            'threat_level': 'HIGH',
            'territory': 'Chamberlain Hills, Strawberry, Forum Drive',
            'member_count': 30,
            'description': 'Organized street gang with strong community ties'
        },
        {
            'name': 'Marabunta Grande',
            'tag': 'MRB',
            'color': '#00BFFF',
            'threat_level': 'MEDIUM',
            'territory': 'El Burro Heights, Cypress Flats',
            'member_count': 20,
            'description': 'Salvadoran gang focused on extortion and robbery'
        },
        {
            'name': 'Lost MC',
            'tag': 'LOST',
            'color': '#FF0000',
            'threat_level': 'HIGH',
            'territory': 'Sandy Shores, Grapeseed, Paleto Bay',
            'member_count': 18,
            'description': 'Outlaw motorcycle club involved in weapons and drug trade'
        }
    ]
    
    print("\nCreating gangs...")
    gangs = []
    for gang_data in gangs_data:
        gang, created = Gang.objects.get_or_create(
            name=gang_data['name'],
            defaults=gang_data
        )
        gangs.append(gang)
        status = "✓ Created" if created else "- Already exists"
        print(f"{status}: {gang.name} ({gang.tag})")
    
    # Sample members data
    members_data = [
        {'name': 'Carlos "Loco" Rodriguez', 'gang': 'Los Santos Vagos', 'rank': 'Lieutenant', 'threat': 'HIGH'},
        {'name': 'Miguel "Flaco" Santos', 'gang': 'Los Santos Vagos', 'rank': 'Soldier', 'threat': 'MEDIUM'},
        {'name': 'DeShawn "Big D" Williams', 'gang': 'Ballas', 'rank': 'OG', 'threat': 'CRITICAL'},
        {'name': 'Marcus "Smoke" Johnson', 'gang': 'Ballas', 'rank': 'Lieutenant', 'threat': 'HIGH'},
        {'name': 'Jamal "CJ" Davis', 'gang': 'The Families', 'rank': 'OG', 'threat': 'HIGH'},
        {'name': 'Sweet Williams', 'gang': 'The Families', 'rank': 'Leader', 'threat': 'HIGH'},
        {'name': 'Jose "Diablo" Martinez', 'gang': 'Marabunta Grande', 'rank': 'Enforcer', 'threat': 'MEDIUM'},
        {'name': 'Johnny Klebitz', 'gang': 'Lost MC', 'rank': 'President', 'threat': 'HIGH'},
        {'name': 'Terry Thorpe', 'gang': 'Lost MC', 'rank': 'Road Captain', 'threat': 'MEDIUM'},
    ]
    
    print("\nCreating gang members...")
    members = []
    for member_data in members_data:
        gang = Gang.objects.get(name=member_data['gang'])
        parts = member_data['name'].split('"')
        if len(parts) == 3:
            first_name = parts[0].strip()
            alias = parts[1]
            last_name = parts[2].strip()
        else:
            first_name = member_data['name']
            alias = ''
            last_name = ''
        
        member, created = GangMember.objects.get_or_create(
            name=member_data['name'],
            gang=gang,
            defaults={
                'alias': alias,
                'rank': member_data['rank'],
                'threat_level': member_data['threat'],
                'status': 'ACTIVE',
                'criminal_record': f'Multiple arrests for gang-related activities'
            }
        )
        members.append(member)
        status = "✓ Created" if created else "- Already exists"
        print(f"{status}: {member.name} - {gang.tag}")
    
    # Create gang relationships
    print("\nCreating gang relationships...")
    relationships_data = [
        ('Ballas', 'The Families', 'WAR'),
        ('Los Santos Vagos', 'Marabunta Grande', 'RIVAL'),
        ('Los Santos Vagos', 'Ballas', 'ALLIED'),
        ('The Families', 'Los Santos Vagos', 'RIVAL'),
        ('Lost MC', 'Ballas', 'NEUTRAL'),
    ]
    
    for gang1_name, gang2_name, rel_type in relationships_data:
        gang1 = Gang.objects.get(name=gang1_name)
        gang2 = Gang.objects.get(name=gang2_name)
        rel, created = GangRelationship.objects.get_or_create(
            gang_1=gang1,
            gang_2=gang2,
            defaults={
                'relationship_type': rel_type,
                'notes': f'{gang1.name} and {gang2.name} have been {rel_type.lower()} for several months'
            }
        )
        status = "✓ Created" if created else "- Already exists"
        print(f"{status}: {gang1.tag} - {rel_type} - {gang2.tag}")
    
    # Create sample incidents
    print("\nCreating incidents...")
    incidents_data = [
        {
            'title': 'Drive-by shooting on Grove Street',
            'type': 'ASSAULT',
            'severity': 'CRITICAL',
            'location': 'Grove Street, Davis',
            'gangs': ['Ballas'],
            'description': 'Multiple shots fired from a purple sedan. Two civilians injured.'
        },
        {
            'title': 'Drug deal interrupted at the docks',
            'type': 'DRUG_TRAFFICKING',
            'severity': 'HIGH',
            'location': 'Terminal Docks',
            'gangs': ['Los Santos Vagos', 'Lost MC'],
            'description': 'Large quantity of narcotics seized. Multiple suspects fled the scene.'
        },
        {
            'title': 'Territory dispute in Cypress Flats',
            'type': 'TERRITORY_DISPUTE',
            'severity': 'HIGH',
            'location': 'Cypress Flats',
            'gangs': ['Los Santos Vagos', 'Marabunta Grande'],
            'description': 'Violent confrontation between rival gangs over territory control.'
        },
    ]
    
    for incident_data in incidents_data:
        incident, created = Incident.objects.get_or_create(
            title=incident_data['title'],
            defaults={
                'incident_type': incident_data['type'],
                'severity': incident_data['severity'],
                'location': incident_data['location'],
                'description': incident_data['description'],
                'status': 'INVESTIGATING',
                'reported_by': user,
                'date_time': datetime.now() - timedelta(days=randint(1, 30))
            }
        )
        if created:
            for gang_name in incident_data['gangs']:
                gang = Gang.objects.get(name=gang_name)
                incident.gangs_involved.add(gang)
        status = "✓ Created" if created else "- Already exists"
        print(f"{status}: {incident.title}")
    
    # Create sample cases
    print("\nCreating case files...")
    cases_data = [
        {
            'case_number': 'SA-DOJ-2026-001',
            'title': 'Operation Clean Streets',
            'priority': 'URGENT',
            'gangs': ['Ballas', 'The Families'],
            'description': 'Major investigation into gang warfare in South Los Santos'
        },
        {
            'case_number': 'SA-DOJ-2026-002',
            'title': 'Drug Trafficking Ring Investigation',
            'priority': 'HIGH',
            'gangs': ['Los Santos Vagos', 'Lost MC'],
            'description': 'Multi-agency investigation into drug distribution network'
        },
    ]
    
    for case_data in cases_data:
        case, created = CaseFile.objects.get_or_create(
            case_number=case_data['case_number'],
            defaults={
                'title': case_data['title'],
                'priority': case_data['priority'],
                'description': case_data['description'],
                'status': 'ACTIVE',
                'lead_agent': user,
            }
        )
        if created:
            for gang_name in case_data['gangs']:
                gang = Gang.objects.get(name=gang_name)
                case.gangs.add(gang)
        status = "✓ Created" if created else "- Already exists"
        print(f"{status}: {case.case_number} - {case.title}")
    
    print("\n" + "="*50)
    print("✓ Sample data creation complete!")
    print("="*50)
    print("\nSummary:")
    print(f"  Gangs: {Gang.objects.count()}")
    print(f"  Members: {GangMember.objects.count()}")
    print(f"  Incidents: {Incident.objects.count()}")
    print(f"  Relationships: {GangRelationship.objects.count()}")
    print(f"  Cases: {CaseFile.objects.count()}")
    print("\nYou can now log in to the system and explore the data!")
    print("Default test user: agent_smith / password123")
    print()

if __name__ == '__main__':
    try:
        create_sample_data()
    except Exception as e:
        print(f"\n✗ Error: {e}")
        print("\nMake sure you've run migrations first:")
        print("  python manage.py migrate")

