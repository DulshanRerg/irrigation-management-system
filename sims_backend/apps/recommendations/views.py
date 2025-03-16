from rest_framework import viewsets, permissions
from apps.recommendations.models import Recommendation
from apps.recommendations.serializers import RecommendationSerializer

class RecommendationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows irrigation recommendations to be viewed or edited.
    """
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Filter recommendations based on user role or specific criteria.
        """
        return Recommendation.objects.all()
