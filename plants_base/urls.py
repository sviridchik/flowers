from django.urls import path, re_path

from plants_base import views

app_name = "plants_base"

urlpatterns = [
    re_path("plants/(?P<type>[a-zA-Z]+)/$", views.Plants.as_view(), name="plants_post"),
    path(
        "plants/<str:type>/<uuid:pk>/",
        views.PlantsDetail.as_view(),
        name="plants_detail",
    ),
]
