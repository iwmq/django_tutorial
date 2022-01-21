import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tutorial.settings')

app = Celery('django_tutorial')
app.config_from_object('django_tutorial.celeryconfig')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

@app.task
def add(x, y):
    return x + y
