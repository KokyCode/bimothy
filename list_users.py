#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sa_doj.settings')
django.setup()

from django.contrib.auth.models import User

print("All users in database:")
for user in User.objects.all():
    print(f"  - Username: '{user.username}' (exact)")
    print(f"    Email: {user.email}")
    print(f"    Is superuser: {user.is_superuser}")
    print(f"    Is active: {user.is_active}")
    print(f"    Password set: {bool(user.password)}")
    print()

