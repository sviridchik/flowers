from django.urls import path

from plants.utils import pk_reg

from . import views

# app_name = "plants_care"

urlpatterns = [
    path(r"fertilizer/", views.FertilizerList.as_view()),
    path(r"fertilizer/" + pk_reg + "$", views.FertilizerListDetail.as_view(), name="detail"),
]
