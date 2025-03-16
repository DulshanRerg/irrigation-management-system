from rest_framework import serializers
from apps.sensors.models import Sensor, SensorData

class SensorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Sensor model.
    """
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'sensor_type', 'location','created_at']

class SensorDataSerializer(serializers.ModelSerializer):
    """
    Serializer for the SensorData model.
    """
    sensor = serializers.PrimaryKeyRelatedField(queryset=Sensor.objects.all())
    
    class Meta:
        model = SensorData
        fields = ['id', 'sensor', 'value', 'timestamp']
