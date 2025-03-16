import random
from datetime import datetime
from apps.sensors.models import SensorData
from apps.recommendations.models import Recommendation

def generate_irrigation_recommendation(sensor):
    """
    AI-driven function to generate irrigation recommendations based on sensor data.
    """
    latest_data = SensorData.objects.filter(sensor=sensor).order_by('-timestamp').first()

    if not latest_data:
        return "No recent sensor data available."

    moisture = latest_data.value
    timestamp = latest_data.timestamp

    if moisture < 30:
        recommendation_text = "Soil moisture is low. Start irrigation."
    elif 30 <= moisture < 60:
        recommendation_text = "Soil moisture is moderate. Monitor conditions."
    else:
        recommendation_text = "Soil moisture is sufficient. No irrigation needed."

    # Save recommendation to DB
    recommendation = Recommendation.objects.create(
        irrigation_zone=sensor.zone,
        sensor_data=latest_data,
        recommendation_text=recommendation_text,
        created_at=datetime.now()
    )

    return recommendation_text