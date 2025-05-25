# django_project/celery.py

import os
from celery import Celery

# Django settings faylini tanlash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

app = Celery('django_project')

# Django config'dan CELERY_ prefiksi bilan boshlanadigan sozlamalarni o'qish
app.config_from_object('django.conf:settings', namespace='CELERY')

# Hammasini avtomatik yuklash
app.autodiscover_tasks()
