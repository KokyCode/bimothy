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
    
    user, created = User.objects.get_or_create(
        username=username,
        defaults={'email': email, 'is_staff': True, 'is_superuser': True}
    )
    
    if not created:
        # User exists, update password and ensure superuser status
        user.set_password(password)
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print(f"User '{username}' password updated!")
    else:
        user.set_password(password)
        user.save()
        print(f"Superuser '{username}' created successfully!")
    
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Email: {email}")

if __name__ == '__main__':
    create_superuser()

