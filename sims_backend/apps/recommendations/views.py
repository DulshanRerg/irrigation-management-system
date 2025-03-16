from rest_framework.response import Response
from rest_framework.decorators import action
from apps.sensors.models import Sensor
from apps.recommendations.utils import generate_irrigation_recommendation
from apps.recommendations.models import Recommendation
from rest_framework import viewsets, permissions
from apps.recommendations.serializers import RecommendationSerializer

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def generate(self, request, pk=None):
        """
        Generate an AI-powered irrigation recommendation for a specific sensor.
        """
        try:
            sensor = Sensor.objects.get(pk=pk)
            recommendation_text = generate_irrigation_recommendation(sensor)
            return Response({"message": recommendation_text})
        except Sensor.DoesNotExist:
            return Response({"error": "Sensor not found"}, status=404)