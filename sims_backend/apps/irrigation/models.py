from django.db import models
from apps.sensors.models import Sensor

class IrrigationZone(models.Model):
    """
    Represents an irrigation zone, linked to specific sensors.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    sensors = models.ManyToManyField(Sensor, related_name="irrigation_zones")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class IrrigationSchedule(models.Model):
    """
    Defines irrigation schedules for different zones.
    """
    zone = models.ForeignKey(IrrigationZone, on_delete=models.CASCADE, related_name="schedules")
    start_time = models.TimeField()
    end_time = models.TimeField()
    frequency = models.CharField(
        max_length=50,
        choices=[
            ("daily", "Daily"),
            ("weekly", "Weekly"),
            ("custom", "Custom"),
        ],
        default="daily",
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.zone.name} - {self.start_time} to {self.end_time}"

class AutomatedIrrigation(models.Model):
    """
    Stores rules for automatic irrigation based on sensor readings.
    """
    zone = models.ForeignKey(IrrigationZone, on_delete=models.CASCADE, related_name="automations")
    threshold_value = models.FloatField(help_text="Trigger irrigation if sensor value falls below this threshold.")
    sensor_type = models.CharField(
        max_length=50,
        choices=[
            ("moisture", "Soil Moisture"),
            ("temperature", "Temperature"),
            ("humidity", "Humidity"),
        ]
    )
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"Auto {self.zone.name} - {self.sensor_type} < {self.threshold_value}"
