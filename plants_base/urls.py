from django.urls import path, re_path

from plants_base import views

app_name = "plants_base"

urlpatterns = [
    re_path("plants/(?P<type>[a-zA-Z]+)/$", views.Plants.as_view(), name="plants_post"),
    re_path(
        "plants/(?P<type>[a-zA-Z]+)/(?P<pk>[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})/",
        views.PlantsDetail.as_view(),
        name="plants_detail",
    ),
    # path("succulents/<uuid:pk>/", views.SucculentsDetail.as_view(), name="fertilizer_detail"),
    # path("flowers/<uuid:pk>/", views.FlowersDetail.as_view(), name="fertilizer_detail"),
    # path("microgreen/<uuid:pk>/", views.MicrogreenDetail.as_view(), name="fertilizer_detail"),
]
