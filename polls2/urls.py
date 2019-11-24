from django.urls import path

from . import views

app_name ='polls2'

urlpatterns = [
    path("", views.index, name="index")
]