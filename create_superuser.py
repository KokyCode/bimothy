#!/usr/bin/env python
"""
Script to create a superuser for SA-DOJ Intelligence System
Run this via Railway one-time command or locally
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sa_doj.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    username = os.environ.get('ADMIN_USERNAME', 'admin')
    email = os.environ.get('ADMIN_EMAIL', 'admin@example.com')
    password = os.environ.get('ADMIN_PASSWORD', 'admin123')
    
    if User.objects.filter(username=username).exists():
        print(f"User '{username}' already exists!")
        return
    
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print(f"Superuser '{username}' created successfully!")
    print(f"Username: {username}")
    print(f"Password: {password}")

if __name__ == '__main__':
    create_superuser()

