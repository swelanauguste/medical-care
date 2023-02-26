from django.urls import path

from .views import ApplicationDetail, ApplicationListView, create_application_view

urlpatterns = [
    path("", ApplicationListView.as_view(), name="application-list"),
    path("detail/<int:pk>/", ApplicationDetail.as_view(), name="application-detail"),
    path("create/application/<int:work_id>/", create_application_view, name="apply"),
]
