import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Newsportal.settings')

app = Celery('Newsportal')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'News.tasks.get_week_notification',
        'schedule': crontab(hour=8, minute=0, day_of_week='mon'),
    },
}

app.autodiscover_tasks()