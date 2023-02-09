from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login",views.login,name="mylogin"),
    path("userlist/showall",views.fetchusers,name="userlist"),
    path("room/createroom",views.RoomCreateView.as_view(),name="createroom"),
    path("room/fetchmessages",views.FetchMessage.as_view(),name="fetchmessages"),
    path("<str:room_name>/", views.room, name="room"),
    path("room/seen_image/<str:room_id>/<str:receiver>/<str:sender>/<str:message_id>",views.MessageSeenView.as_view(),name="message_seen")
]