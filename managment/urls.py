from django.urls import path

from managment import views

app_name = "managment"

urlpatterns = [
    path("rooms/", views.RoomList.as_view(), name="room_list"),
    path("rooms/<uuid:pk>/", views.RoomListDetail.as_view(), name="room_detail"),
    path("users/", views.UserList.as_view(), name="user_detail"),
    path("users/<uuid:pk>/", views.UserListDetail.as_view(), name="user_detail"),
]
