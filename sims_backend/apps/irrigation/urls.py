from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IrrigationScheduleViewSet, AutomatedIrrigationViewSet, IrrigationZoneViewSet

router = DefaultRouter()
router.register(r'irrigation-schedules', IrrigationScheduleViewSet, basename='schedule')
router.register(r'automated-irrigation', AutomatedIrrigationViewSet, basename='auto-irrigation')
router.register(r'irrigation-zones', IrrigationZoneViewSet, basename='zones')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]