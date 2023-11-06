from django.urls import include, path

urlpatterns = [
    path("api/cars", include("apps.cars.urls")),
    path("api/parks", include("apps.parks.urls")),
    path("api/users", include("apps.users.urls")),
    path("api/auth", include("apps.auth.urls")),
    path("api/test_email", include("apps.test_email.urls")),
]
