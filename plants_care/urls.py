from django.urls import path

from plants.utils import pk_reg

from . import views

# app_name = "plants_care"

urlpatterns = [
    path(r"fertilizer/", views.FertilizerList.as_view(), name="fertilizer_list"),
    path(r"fertilizer/" + pk_reg + "$", views.FertilizerListDetail.as_view(), name="fertilizer_detail"),
    path(r"watering/", views.WateringList.as_view(), name="watering_list"),
    path(r"watering/" + pk_reg + "$", views.WateringListDetail.as_view(), name="watering_detail"),
    path(r"solutions/", views.SolutionsList.as_view(), name="solutions_list"),
    path(r"solutions/" + pk_reg + "$", views.SolutionsListDetail.as_view(), name="solutions_detail"),
    path(r"regimes/", views.RegimeList.as_view(), name="regimes_list"),
    path(r"regimes/" + pk_reg + "$", views.RegimeListDetail.as_view(), name="regimes_detail"),
]
