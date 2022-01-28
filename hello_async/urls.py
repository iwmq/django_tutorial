from django.urls import path

from .views import index, async_view, sync_view, smoke_some_meats


urlpatterns = [
    path("async/", async_view),
    path("sync/", sync_view),
    path("smoke_some_meats/", smoke_some_meats),
    path("", index),
]