from django.db import models
from apps.sensors.models import SensorData
from apps.irrigation.models import IrrigationZone

class Recommendation(models.Model):
    """
    Stores AI-generated irrigation recommendations based on sensor data analysis.
    """
    irrigation_zone = models.ForeignKey(IrrigationZone, on_delete=models.CASCADE, related_name="recommendations")
    sensor_data = models.ForeignKey(SensorData, on_delete=models.CASCADE, related_name="recommendations")
    recommendation_text = models.TextField(help_text="AI-generated irrigation advice")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Recommendation for {self.irrigation_zone} at {self.created_at}"
