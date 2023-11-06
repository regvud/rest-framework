from django.urls import include, path

urlpatterns = [
    path("cars", include("apps.cars.urls")),
    path("parks", include("apps.parks.urls")),
    path("users", include("apps.users.urls")),
    path("auth", include("apps.auth.urls")),
    path("test_email", include("apps.test_email.urls")),
]
