"""
WSGI config for SA DOJ Control Panel project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sa_doj.settings')

application = get_wsgi_application()

