"""
ASGI config for SA DOJ Control Panel project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sa_doj.settings')

application = get_asgi_application()

