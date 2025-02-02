import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dealhawk.settings')

# Create the Celery app
app = Celery('dealhawk')

# Load the Celery settings from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks in all installed apps
app.autodiscover_tasks()