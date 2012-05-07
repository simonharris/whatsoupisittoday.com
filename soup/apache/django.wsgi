import os, sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))
PROJECT_DIR = os.path.abspath(os.path.join(APP_DIR, '..'))

sys.path.append(PROJECT_DIR)
sys.path.append(APP_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'soup.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
