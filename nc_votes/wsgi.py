#!/usr/bin/env python3
"""
WSGI config for nc_votes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nc_votes.settings")

application = get_wsgi_application()

