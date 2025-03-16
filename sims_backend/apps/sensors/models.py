from django.db import models
from django.utils import timezone

class Sensor(models.Model):
    """Model to store sensor information."""
    SENSOR_TYPES = [
        ('temperature', 'Temperature'),
        ('moisture', 'Moisture'),
        ('humidity', 'Humidity'),
        ('ph', 'pH'),
    ]
    
    sensor_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    sensor_type = models.CharField(max_length=50, choices=SENSOR_TYPES)
    location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.sensor_type})"

class SensorData(models.Model):
    """Model to store real-time sensor data readings."""
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='readings')
    value = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.sensor.name}: {self.value} at {self.timestamp}"
