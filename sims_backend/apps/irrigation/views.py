from rest_framework import viewsets, permissions
from apps.irrigation.models import IrrigationZone, IrrigationSchedule, AutomatedIrrigation
from apps.irrigation.serializers import (
    IrrigationZoneSerializer,
    IrrigationScheduleSerializer,
    AutomatedIrrigationSerializer
)

class IrrigationZoneViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing irrigation zones.
    """
    queryset = IrrigationZone.objects.all()
    serializer_class = IrrigationZoneSerializer
    permission_classes = [permissions.IsAuthenticated]


class IrrigationScheduleViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing irrigation schedules.
    """
    queryset = IrrigationSchedule.objects.all()
    serializer_class = IrrigationScheduleSerializer
    permission_classes = [permissions.IsAuthenticated]


class AutomatedIrrigationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing automated irrigation settings.
    """
    queryset = AutomatedIrrigation.objects.all()
    serializer_class = AutomatedIrrigationSerializer
    permission_classes = [permissions.IsAuthenticated]
