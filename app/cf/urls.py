from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from users.views import HomeView

urlpatterns = [
    path("", include("work.urls")),
    path("home/", HomeView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("profiles/", include("users.urls")),
    path("med_care/", include("med_care.urls")),
    path("applications/", include("applications.urls")),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
