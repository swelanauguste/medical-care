from django.urls import path

from .views import (
    MedicalCareProfileCreateView,
    MedicalCareProfileUpdateView,
)

urlpatterns = [
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
]
