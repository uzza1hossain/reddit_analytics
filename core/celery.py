from __future__ import absolute_import, unicode_literals # for python2

import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
# this is also used in manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


## Get the base REDIS URL, default to redis' default
BASE_REDIS_URL = os.environ.get('REDIS_URL')

app = Celery('core')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# app.conf.broker_url = BASE_REDIS_URL
# CELERY_BROKER_URL = BASE_REDIS_URL

# this allows you to schedule items in the Django admin.
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'




app.conf.beat_schedule = {
    'add-every-15-minutes-contrab': {
        'task': 'scrape_submissions',
        'schedule': crontab(minute='*/15')
    },
    'add-every-15-minute-contrab': {
        'task': 'scrape_comments',
        'schedule': crontab(minute='*/15')
    },
    'add-every-3-hours-contrab': {
        'task': 'scrape_submissions',
        'schedule': crontab(minute=0, hour='*/3')
    },
    'add-every-3-hour-contrab': {
        'task': 'scrape_comments',
        'schedule': crontab(minute=0, hour='*/3')
    },
}