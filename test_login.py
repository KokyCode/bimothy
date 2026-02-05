#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sa_doj.settings')
django.setup()

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Test all possible usernames
test_credentials = [
    ('doj_agent', 'agent123'),
    ('k0ky', 'agent123'),
    ('agent', 'agent123'),
]

print("Testing authentication:")
for username, password in test_credentials:
    user = authenticate(username=username, password=password)
    if user:
        print(f"OK: {username} / {password} - AUTHENTICATED")
    else:
        print(f"FAIL: {username} / {password} - FAILED")
        # Try to reset password
        try:
            u = User.objects.get(username=username)
            u.set_password(password)
            u.save()
            print(f"  -> Password reset for {username}")
            # Test again
            user = authenticate(username=username, password=password)
            if user:
                print(f"  -> Now works!")
        except User.DoesNotExist:
            print(f"  → User doesn't exist")

