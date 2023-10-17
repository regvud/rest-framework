from django.urls import include, path

urlpatterns = [
    path('cars/', include('apps.my_cars.urls')),
    path('parks/', include('apps.parks.urls')),
]
