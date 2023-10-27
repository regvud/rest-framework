from django.urls import include, path

urlpatterns = [
    path('cars', include('apps.cars.urls')),
    path('users', include('apps.users.urls')),
    path('auth', include('apps.auth.urls')),
]
