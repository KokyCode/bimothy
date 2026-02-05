#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sa_doj.settings')
django.setup()

from django.contrib.auth.models import User

username = 'doj_agent'
password = 'agent123'

try:
    user = User.objects.get(username=username)
    print(f"User found: {user.username}")
    print(f"Is superuser: {user.is_superuser}")
    print(f"Is staff: {user.is_staff}")
    print(f"Is active: {user.is_active}")
    print(f"Password check: {user.check_password(password)}")
    
    # Try to authenticate
    from django.contrib.auth import authenticate
    auth_user = authenticate(username=username, password=password)
    if auth_user:
        print(f"Authentication successful!")
    else:
        print(f"Authentication failed!")
        # Reset password
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print(f"Password reset and user activated!")
        
except User.DoesNotExist:
    print(f"User '{username}' does not exist!")

