from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.sensors.views import SensorViewSet, SensorDataViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'sensors', SensorViewSet, basename='sensor')
router.register(r'sensor-data', SensorDataViewSet, basename='sensor data')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
