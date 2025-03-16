from rest_framework import serializers
from apps.recommendations.models import Recommendation

class RecommendationSerializer(serializers.ModelSerializer):
    """
    Serializer for AI-generated irrigation recommendations.
    """
    class Meta:
        model = Recommendation
        fields = ['id', 'irrigation_zone', 'sensor_data', 'recommendation_text', 'created_at']