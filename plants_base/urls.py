from django.urls import path

from plants_base import views

app_name = "plants_care"

urlpatterns = [
    path("plants/", views.Plants.as_view(), name="plants_post"),
    path("succulents/<uuid:pk>/", views.SucculentsDetail.as_view(), name="fertilizer_detail"),
    path("flowers/<uuid:pk>/", views.FlowersDetail.as_view(), name="fertilizer_detail"),
    path("microgreen/<uuid:pk>/", views.MicrogreenDetail.as_view(), name="fertilizer_detail"),
]
