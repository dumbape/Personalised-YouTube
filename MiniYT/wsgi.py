"""
WSGI config for MiniYT project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, json, threading
from django.core.wsgi import get_wsgi_application
from data.fetchData import startFetchingData

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MiniYT.settings')

application = get_wsgi_application()

startFetchingData()

