from django.urls import path

from .views import ChatIndexView, ChatRoomView


urlpatterns = [
    path("", ChatIndexView.as_view(), name="index"),
    path("<str:room_name>/", ChatRoomView.as_view(), name="room"),
]