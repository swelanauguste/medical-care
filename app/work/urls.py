from django.urls import path

from .views import WorkListView, WorkDetailView

urlpatterns = [
    path("", WorkListView.as_view(), name="work-list"),
    path("detail/<int:pk>/", WorkDetailView.as_view(), name="work-detail"),
]
