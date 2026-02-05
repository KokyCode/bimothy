"""
Custom Gang Setup for Grape Street
Automatically creates Grape Street and all their allies/enemies
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sa_doj.settings')
django.setup()

from django.contrib.auth.models import User
from intelligence.models import Gang, GangMember, GangRelationship, Incident, CaseFile
from datetime import datetime, timedelta
from random import randint

def setup_grape_street_system():
    """Setup Grape Street gang structure"""
    
    print("="*60)
    print("  GRAPE STREET GANG INTELLIGENCE SYSTEM SETUP")
    print("="*60)
    print()
    
    # Create DOJ agent if doesn't exist
    print("[1/5] Setting up DOJ agent account...")
    agent, created = User.objects.get_or_create(
        username='doj_agent',
        defaults={
            'first_name': 'DOJ',
            'last_name': 'Agent',
            'email': 'agent@sa-doj.gov',
            'is_staff': True,
            'is_superuser': False
        }
    )
    if created:
        agent.set_password('agent123')
        agent.save()
        print(f"✓ Created DOJ agent account")
    else:
        print(f"✓ DOJ agent account already exists")
    
    print("\n[2/5] Creating gangs...")
    
    # Gang data with colors and threat levels
    gangs_data = [
        # Primary gang
        {
            'name': 'Grape Street',
            'tag': 'GSC, RCG',
            'color': '#8B00FF',  # Purple/Grape color
            'threat_level': 'CRITICAL',
            'territory': 'South Central Los Santos, Grape Street area, Jordan Downs housing projects',
            'member_count': 45,
            'description': 'Primary Crip gang operating in South Central. Known for drug trafficking and territorial control.',
            'is_active': True
        },
        
        # Allies
        {
            'name': 'Hoover Criminals',
            'tag': 'HCG',
            'color': '#FF8C00',  # Orange
            'threat_level': 'HIGH',
            'territory': 'West Adams, Mid-City Los Santos',
            'member_count': 38,
            'description': 'Allied Crip gang. Strategic partnership with Grape Street.',
            'is_active': True
        },
        {
            'name': 'Black P Stones',
            'tag': 'BPS',
            'color': '#8B0000',  # Dark Red
            'threat_level': 'HIGH',
            'territory': 'Baldwin Village, Crenshaw District',
            'member_count': 42,
            'description': 'Blood gang allied with Grape Street. Known for organized crime activities.',
            'is_active': True
        },
        {
            'name': 'Playboy Gangster Crip',
            'tag': 'PBGC',
            'color': '#0000CD',  # Medium Blue
            'threat_level': 'MEDIUM',
            'territory': 'West Los Santos, Venice area',
            'member_count': 28,
            'description': 'Crip ally of Grape Street. Focuses on westside operations.',
            'is_active': True
        },
        
        # Enemies
        {
            'name': 'PJ Rancho Crip',
            'tag': 'PJRC',
            'color': '#1E90FF',  # Dodger Blue
            'threat_level': 'HIGH',
            'territory': 'Rancho area, East Los Santos',
            'member_count': 32,
            'description': 'Rival Crip gang. Frequent conflicts with Grape Street over territory.',
            'is_active': True
        },
        {
            'name': 'Bounty Hunter Rancho Bloods',
            'tag': 'BHRB',
            'color': '#DC143C',  # Crimson
            'threat_level': 'CRITICAL',
            'territory': 'Rancho, Nickerson Gardens projects',
            'member_count': 40,
            'description': 'Major Blood rival. Active warfare with Grape Street.',
            'is_active': True
        },
        {
            'name': 'Hacienda Village Bloods',
            'tag': 'HVB',
            'color': '#B22222',  # Fire Brick Red
            'threat_level': 'HIGH',
            'territory': 'Hacienda Heights, East Los Santos',
            'member_count': 35,
            'description': 'Blood gang enemy. Territorial disputes ongoing.',
            'is_active': True
        },
        {
            'name': 'East Coast Crips',
            'tag': 'ECC',
            'color': '#4169E1',  # Royal Blue
            'threat_level': 'HIGH',
            'territory': 'East Los Santos, Vernon area',
            'member_count': 36,
            'description': 'Rival Crip faction. Long-standing feud with Grape Street.',
            'is_active': True
        },
        {
            'name': 'Florencia 13',
            'tag': 'F13',
            'color': '#228B22',  # Forest Green
            'threat_level': 'CRITICAL',
            'territory': 'Florence-Firestone, South Central',
            'member_count': 50,
            'description': 'Major Mexican Mafia-affiliated gang. Active conflict with Grape Street.',
            'is_active': True
        }
    ]
    
    # Create gangs
    gangs = {}
    for gang_data in gangs_data:
        gang, created = Gang.objects.get_or_create(
            name=gang_data['name'],
            defaults=gang_data
        )
        gangs[gang_data['name']] = gang
        status = "✓" if created else "→"
        print(f"{status} {gang.name} ({gang.tag}) - {gang.threat_level}")
    
    print(f"\n[3/5] Setting up gang relationships...")
    
    # Define relationships
    relationships = [
        # Grape Street allies
        ('Grape Street', 'Hoover Criminals', 'ALLIED', 'Strategic alliance for mutual protection and business operations'),
        ('Grape Street', 'Black P Stones', 'ALLIED', 'Cross-set alliance despite Crip/Blood division'),
        ('Grape Street', 'Playboy Gangster Crip', 'ALLIED', 'Crip alliance for westside operations'),
        
        # Grape Street enemies
        ('Grape Street', 'PJ Rancho Crip', 'RIVAL', 'Ongoing territorial disputes and internal Crip rivalry'),
        ('Grape Street', 'Bounty Hunter Rancho Bloods', 'WAR', 'Active warfare - multiple shootings and casualties'),
        ('Grape Street', 'Hacienda Village Bloods', 'RIVAL', 'Blood rivalry with territorial conflicts'),
        ('Grape Street', 'East Coast Crips', 'RIVAL', 'Long-standing Crip-on-Crip violence'),
        ('Grape Street', 'Florencia 13', 'WAR', 'Major conflict - ethnic and territorial warfare'),
        
        # Inter-enemy relationships
        ('Bounty Hunter Rancho Bloods', 'Hacienda Village Bloods', 'ALLIED', 'Blood alliance against common enemies'),
        ('PJ Rancho Crip', 'East Coast Crips', 'ALLIED', 'United against Grape Street'),
        ('Hoover Criminals', 'Playboy Gangster Crip', 'ALLIED', 'Crip cooperation'),
    ]
    
    for gang1_name, gang2_name, rel_type, notes in relationships:
        gang1 = gangs[gang1_name]
        gang2 = gangs[gang2_name]
        
        rel, created = GangRelationship.objects.get_or_create(
            gang_1=gang1,
            gang_2=gang2,
            defaults={
                'relationship_type': rel_type,
                'notes': notes
            }
        )
        status = "✓" if created else "→"
        print(f"{status} {gang1.tag} <{rel_type}> {gang2.tag}")
    
    print(f"\n[4/5] Creating sample gang members...")
    
    # Sample members for Grape Street
    grape_members = [
        {'name': 'Marcus "Big Grape" Johnson', 'rank': 'OG', 'threat': 'CRITICAL', 'status': 'WANTED'},
        {'name': 'Tyrone "T-Bone" Williams', 'rank': 'Shot Caller', 'threat': 'HIGH', 'status': 'ACTIVE'},
        {'name': 'DeAndre "Lil Loc" Davis', 'rank': 'Soldier', 'threat': 'MEDIUM', 'status': 'ACTIVE'},
        {'name': 'Jamal "Grape" Thompson', 'rank': 'Enforcer', 'threat': 'HIGH', 'status': 'ACTIVE'},
        {'name': 'Kevin "K-Dog" Brown', 'rank': 'Soldier', 'threat': 'MEDIUM', 'status': 'INCARCERATED'},
    ]
    
    grape_street_gang = gangs['Grape Street']
    
    for member_data in grape_members:
        parts = member_data['name'].split('"')
        if len(parts) == 3:
            alias = parts[1]
        else:
            alias = ''
        
        member, created = GangMember.objects.get_or_create(
            name=member_data['name'],
            gang=grape_street_gang,
            defaults={
                'alias': alias,
                'rank': member_data['rank'],
                'threat_level': member_data['threat'],
                'status': member_data['status'],
                'criminal_record': f"Multiple arrests for gang-related activities. Known {member_data['rank']} of Grape Street."
            }
        )
        status = "✓" if created else "→"
        print(f"{status} {member.name} - {member_data['rank']}")
    
    print(f"\n[5/5] Creating recent incidents...")
    
    # Sample incidents
    incidents_data = [
        {
            'title': 'Drive-by shooting on Grape Street',
            'type': 'ASSAULT',
            'severity': 'CRITICAL',
            'location': 'Grape Street, Jordan Downs area',
            'gangs': ['Bounty Hunter Rancho Bloods', 'Grape Street'],
            'description': 'Suspected BHRB members conducted drive-by targeting Grape Street territory. Multiple shots fired, 2 civilians injured.',
            'days_ago': 2
        },
        {
            'title': 'Narcotics seizure at Rancho',
            'type': 'DRUG_TRAFFICKING',
            'severity': 'HIGH',
            'location': 'Rancho district, East LS',
            'gangs': ['Grape Street', 'PJ Rancho Crip'],
            'description': 'Large drug operation interrupted. GSC and PJRC members present, territorial dispute over distribution.',
            'days_ago': 5
        },
        {
            'title': 'Gang-related homicide - Florence area',
            'type': 'MURDER',
            'severity': 'CRITICAL',
            'location': 'Florence Avenue, South Central',
            'gangs': ['Grape Street', 'Florencia 13'],
            'description': 'Suspected GSC member killed in F13 territory. Retaliation expected.',
            'days_ago': 7
        },
        {
            'title': 'Weapons trafficking operation',
            'type': 'WEAPONS',
            'severity': 'HIGH',
            'location': 'Industrial district',
            'gangs': ['Grape Street', 'Hoover Criminals'],
            'description': 'Intelligence suggests GSC and HCG coordinating weapons acquisition. Investigation ongoing.',
            'days_ago': 10
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
                'reported_by': agent,
                'date_time': datetime.now() - timedelta(days=incident_data['days_ago'])
            }
        )
        
        if created:
            for gang_name in incident_data['gangs']:
                if gang_name in gangs:
                    incident.gangs_involved.add(gangs[gang_name])
        
        status = "✓" if created else "→"
        print(f"{status} {incident.title}")
    
    # Create multiple case files
    print(f"\n[6/6] Creating active case files...")
    
    cases_data = [
        {
            'case_number': 'SA-DOJ-2026-GSC-001',
            'title': 'Operation Grape Harvest - GSC, RCG Investigation',
            'priority': 'URGENT',
            'description': 'Comprehensive investigation into Grape Street Crip operations, focusing on narcotics distribution network and violent conflicts with rival gangs, particularly BHRB and F13.',
            'status': 'ACTIVE',
            'gangs': ['Grape Street', 'Bounty Hunter Rancho Bloods', 'Florencia 13']
        },
        {
            'case_number': 'SA-DOJ-2026-GANG-002',
            'title': 'Blood vs Crip Territory War - South Central',
            'priority': 'URGENT',
            'description': 'Escalating violence between Blood and Crip factions in South Central. Multiple shootings and retaliations documented. Focus on BHRB and GSC conflict.',
            'status': 'ACTIVE',
            'gangs': ['Grape Street', 'Bounty Hunter Rancho Bloods', 'Black P Stones']
        },
        {
            'case_number': 'SA-DOJ-2026-NARC-003',
            'title': 'Multi-Gang Narcotics Distribution Network',
            'priority': 'HIGH',
            'description': 'Investigation into coordinated drug trafficking operation involving GSC, HCG, and PBGC. Interstate distribution suspected.',
            'status': 'ACTIVE',
            'gangs': ['Grape Street', 'Hoover Criminals', 'Playboy Gangster Crip']
        },
        {
            'case_number': 'SA-DOJ-2026-HOM-004',
            'title': 'Gang-Related Homicides - Rancho District',
            'priority': 'HIGH',
            'description': 'String of murders linked to ongoing feud between GSC and PJRC over Rancho territory. 5 victims in past 3 months.',
            'status': 'INVESTIGATING',
            'gangs': ['Grape Street', 'PJ Rancho Crip']
        },
        {
            'case_number': 'SA-DOJ-2026-WEAP-005',
            'title': 'Illegal Weapons Trafficking Ring',
            'priority': 'HIGH',
            'description': 'Intelligence suggests large-scale weapons importation and distribution. GSC and allied gangs suspected of coordinating purchases.',
            'status': 'ACTIVE',
            'gangs': ['Grape Street', 'Hoover Criminals', 'Black P Stones']
        },
        {
            'case_number': 'SA-DOJ-2026-EXT-006',
            'title': 'Organized Crime - Extortion and Racketeering',
            'priority': 'MEDIUM',
            'description': 'Local businesses reporting systematic extortion by gang members. Pattern suggests organized operation across multiple territories.',
            'status': 'OPEN',
            'gangs': ['Grape Street', 'Florencia 13', 'East Coast Crips']
        },
        {
            'case_number': 'SA-DOJ-2026-RIOT-007',
            'title': 'Gang Summit Intelligence - Potential Conflict',
            'priority': 'URGENT',
            'description': 'Intercepted communications suggest planned confrontation between allied and rival factions. High risk of major violence.',
            'status': 'ACTIVE',
            'gangs': ['Grape Street', 'Bounty Hunter Rancho Bloods', 'Hoover Criminals', 'PJ Rancho Crip']
        },
        {
            'case_number': 'SA-DOJ-2026-COLD-008',
            'title': 'Cold Case Review - 2024 Jordan Downs Shooting',
            'priority': 'MEDIUM',
            'description': 'Re-opening investigation into mass shooting at Jordan Downs. New evidence suggests GSC involvement and BHRB retaliation.',
            'status': 'PENDING',
            'gangs': ['Grape Street', 'Bounty Hunter Rancho Bloods']
        },
        {
            'case_number': 'SA-DOJ-2026-JUVE-009',
            'title': 'Juvenile Gang Recruitment Investigation',
            'priority': 'HIGH',
            'description': 'Increased gang recruitment activity targeting minors. Multiple gangs competing for young members in South Central schools.',
            'status': 'ACTIVE',
            'gangs': ['Grape Street', 'East Coast Crips', 'Hacienda Village Bloods']
        },
        {
            'case_number': 'SA-DOJ-2026-INTEL-010',
            'title': 'Cross-Gang Alliance Monitoring',
            'priority': 'MEDIUM',
            'description': 'Unusual alliance patterns observed. Blood-Crip cooperation between GSC and BPS requires surveillance and analysis.',
            'status': 'ACTIVE',
            'gangs': ['Grape Street', 'Black P Stones', 'Playboy Gangster Crip']
        },
        {
            'case_number': 'SA-DOJ-2026-ASSAULT-011',
            'title': 'Drive-By Shooting Series - Florence Corridor',
            'priority': 'CRITICAL',
            'description': 'Series of coordinated drive-by shootings along Florence Avenue. F13 and GSC engaging in active warfare.',
            'status': 'INVESTIGATING',
            'gangs': ['Grape Street', 'Florencia 13']
        },
        {
            'case_number': 'SA-DOJ-2026-MONEY-012',
            'title': 'Money Laundering Operation - Front Businesses',
            'priority': 'HIGH',
            'description': 'Several businesses suspected of being gang fronts for money laundering. Financial crimes unit investigating GSC connections.',
            'status': 'ACTIVE',
            'gangs': ['Grape Street', 'Hoover Criminals']
        }
    ]
    
    for case_data in cases_data:
        case, created = CaseFile.objects.get_or_create(
            case_number=case_data['case_number'],
            defaults={
                'title': case_data['title'],
                'priority': case_data['priority'],
                'description': case_data['description'],
                'status': case_data['status'],
                'lead_agent': agent,
            }
        )
        
        if created:
            for gang_name in case_data['gangs']:
                if gang_name in gangs:
                    case.gangs.add(gangs[gang_name])
        
        status = "✓" if created else "→"
        print(f"{status} {case.case_number} - {case.title}")
    
    print("\n" + "="*60)
    print("  ✓ GRAPE STREET SYSTEM SETUP COMPLETE!")
    print("="*60)
    print("\nSystem Summary:")
    print(f"  • Primary Gang: Grape Street (GSC, RCG)")
    print(f"  • Allied Gangs: 3 (Hoover Criminals, Black P Stones, PBGC)")
    print(f"  • Enemy Gangs: 5 (PJRC, BHRB, HVB, ECC, F13)")
    print(f"  • Total Gangs: {Gang.objects.count()}")
    print(f"  • Gang Members: {GangMember.objects.count()}")
    print(f"  • Relationships: {GangRelationship.objects.count()}")
    print(f"  • Incidents: {Incident.objects.count()}")
    print(f"  • Case Files: {CaseFile.objects.count()}")
    print("\nYou can now access the system!")
    print("DOJ Agent credentials:")
    print("  Username: doj_agent")
    print("  Password: agent123")
    print("\n")

if __name__ == '__main__':
    try:
        setup_grape_street_system()
    except Exception as e:
        print(f"\n✗ Error: {e}")
        print("\nMake sure you've run migrations first:")
        print("  python manage.py migrate")

