from django.urls import path

from plants_base import views

app_name = "plants_base"

urlpatterns = [
    path("plants/<str:type>/", views.Plants.as_view(), name="plants_post"),
    path(
        "plants/<str:type>/<uuid:pk>/",
        views.PlantsDetail.as_view(),
        name="plants_detail",
    ),
]
