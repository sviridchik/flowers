from django.urls import path

from plants_base import views

app_name = "plants_care"

urlpatterns = [
    path("plants/", views.Plants.as_view(), name="plants_post"),
    # path("plants/<uuid:pk>/", views.FertilizerListDetail.as_view(), name="fertilizer_detail"),

]
