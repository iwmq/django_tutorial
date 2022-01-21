from django_tutorial.celery import app

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

@app.task
def add(x, y):
    return x + y
