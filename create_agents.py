#!/usr/bin/env python
"""
Create 5 DOJ agent accounts
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sa_doj.settings')
django.setup()

from django.contrib.auth.models import User

agents = [
    {'username': 'doj_agent', 'password': 'agent123', 'email': 'agent1@doj.com'},
    {'username': 'doj_agent2', 'password': 'agent123', 'email': 'agent2@doj.com'},
    {'username': 'doj_agent3', 'password': 'agent123', 'email': 'agent3@doj.com'},
    {'username': 'doj_agent4', 'password': 'agent123', 'email': 'agent4@doj.com'},
    {'username': 'doj_agent5', 'password': 'agent123', 'email': 'agent5@doj.com'},
]

print("Creating DOJ agent accounts...")
for agent in agents:
    user, created = User.objects.get_or_create(
        username=agent['username'],
        defaults={
            'email': agent['email'],
            'is_staff': True,
            'is_superuser': True,
            'is_active': True
        }
    )
    
    # Always update password and ensure permissions
    user.set_password(agent['password'])
    user.email = agent['email']
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.save()
    
    if created:
        print(f"Created: {agent['username']} / {agent['password']}")
    else:
        print(f"Updated: {agent['username']} / {agent['password']}")

print("\nAll 5 agent accounts ready!")
print("Usernames: doj_agent, doj_agent2, doj_agent3, doj_agent4, doj_agent5")
print("Password for all: agent123")

