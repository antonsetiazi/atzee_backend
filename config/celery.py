# config/celery.py

import os
from celery import Celery

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Mengambil konfigurasi dari settings.py dengan prefix 'CELERY_'
app.config_from_object('django.conf:settings', namespace='CELERY')

# Mencari file tasks.py di setiap aplikasi yang terdaftar
app.autodiscover_tasks()