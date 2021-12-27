from django.urls import path

from plants_care import views

app_name = "plants_care"

urlpatterns = [
    path("fertilizer/", views.FertilizerList.as_view(), name="fertilizer_list"),
    path("fertilizer/<uuid:pk>/", views.FertilizerListDetail.as_view(), name="fertilizer_detail"),
    path("watering/", views.WateringList.as_view(), name="watering_list"),
    path("watering/<uuid:pk>/", views.WateringListDetail.as_view(), name="watering_detail"),
    path("solutions/", views.SolutionsList.as_view(), name="solutions_list"),
    path("solutions/<uuid:pk>/", views.SolutionsListDetail.as_view(), name="solutions_detail"),
    path("regimes/", views.RegimeList.as_view(), name="regimes_list"),
    path("regimes/<uuid:pk>/", views.RegimeListDetail.as_view(), name="regimes_detail"),
    path("problems/", views.ProblemList.as_view(), name="problems_list"),
    path("problems/<uuid:pk>/", views.ProblemListDetail.as_view(), name="problems_detail"),
]
