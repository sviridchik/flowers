from django.urls import path

from plants.utils import pk_reg

from . import views

app_name = "plants_care"

urlpatterns = [
    path(r"fertilizer/", views.FertilizerList.as_view(), name="fertilizer_list"),
    path(r"fertilizer/<uuid:pk>/", views.FertilizerListDetail.as_view(), name="fertilizer_detail"),
    path(r"watering/", views.WateringList.as_view(), name="watering_list"),
    path(r"watering/<uuid:pk>/", views.WateringListDetail.as_view(), name="watering_detail"),
    path(r"solutions/", views.SolutionsList.as_view(), name="solutions_list"),
    path(r"solutions/<uuid:pk>/", views.SolutionsListDetail.as_view(), name="solutions_detail"),
    path(r"regimes/", views.RegimeList.as_view(), name="regimes_list"),
    path(r"regimes/<uuid:pk>/", views.RegimeListDetail.as_view(), name="regimes_detail"),
    path(r"problems/", views.ProblemList.as_view(), name="problems_list"),
    path(r"problems/<uuid:pk>/", views.ProblemListDetail.as_view(), name="problems_detail"),
]
