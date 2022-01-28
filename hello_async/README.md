Try to run background jobs via async views.

See https://testdriven.io/blog/django-async-views/


Install requirements:
```
pip install -U httpx uvicorn
```

Integrate URLs:
```
    path("hello_async", include("hello_async.urls"))
```

Run:
```
    uvicorn django_tutorial.asgi:application --reload
```