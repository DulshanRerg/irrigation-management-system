from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from apps.sensors.models import Sensor, SensorData
from apps.sensors.serializers import SensorSerializer, SensorDataSerializer

class SensorViewSet(viewsets.ModelViewSet):
    """ViewSet for managing sensors."""
    queryset = Sensor.objects.all().order_by('name')
    serializer_class = SensorSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET'])
    def data(self, request, pk=None):
        """Retrieve sensor data for a specific sensor."""
        sensor = get_object_or_404(Sensor, pk=pk)
        sensor_data = SensorData.objects.filter(sensor=sensor).order_by('-timestamp')
        serializer = SensorDataSerializer(sensor_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SensorDataViewSet(viewsets.ModelViewSet):
    """ViewSet for managing sensor data."""
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer
    permission_classes = [IsAuthenticated]
