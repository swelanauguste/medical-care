from django.urls import path

from .views import (
    MedicalCareProfileCreateView,
    MedicalCareProfileDetailView,
    MedicalCareProfileListView,
    MedicalCareProfileUpdateView,
)

urlpatterns = [
    path(
        "",
        MedicalCareProfileListView.as_view(),
        name="medical-care-profile-list",
    ),
    path(
        "create/",
        MedicalCareProfileCreateView.as_view(),
        name="medical-care-profile-create",
    ),
    path(
        "update/<slug:slug>/",
        MedicalCareProfileUpdateView.as_view(),
        name="medical-care-profile-update",
    ),
    path(
        "detail/<slug:slug>/",
        MedicalCareProfileDetailView.as_view(),
        name="medical-care-profile-detail",
    ),
]
