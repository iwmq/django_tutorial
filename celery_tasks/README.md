This is my test app for integrating Celery with Django.


How to use?
----
1. Open one terminal, run celery worker:
 ```
    celery -A django_tutorial worker --loglevel=INFO
```

2. Open another terminal, run Django shell:
```
    python manage.py shell
```

3. Run the simple `add` task:
```
    from celery_tasks.tasks import add
    result = add.delay(3,4)
    print(result.get())
```