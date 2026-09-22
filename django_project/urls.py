from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("posts.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/dj_rest_auth/", include("dj_rest_auth.urls")),
    path(
        "api/v1/dj_rest_auth/registration/", include("dj_rest_auth.registration.urls")
    ),
]
