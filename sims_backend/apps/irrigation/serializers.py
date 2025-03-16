from rest_framework import serializers
from apps.irrigation.models import IrrigationZone, IrrigationSchedule, AutomatedIrrigation

class IrrigationZoneSerializer(serializers.ModelSerializer):
    """
    Serializer for IrrigationZone model.
    """
    class Meta:
        model = IrrigationZone
        fields = '__all__'


class IrrigationScheduleSerializer(serializers.ModelSerializer):
    """
    Serializer for IrrigationSchedule model.
    """
    zone = IrrigationZoneSerializer(read_only=True)

    class Meta:
        model = IrrigationSchedule
        fields = '__all__'


class AutomatedIrrigationSerializer(serializers.ModelSerializer):
    """
    Serializer for AutomatedIrrigation model.
    """
    zone = IrrigationZoneSerializer(read_only=True)

    class Meta:
        model = AutomatedIrrigation
        fields = '__all__'
