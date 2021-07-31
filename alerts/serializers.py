from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id', 'targetPrice', 'created', 'deleted', 'triggered']
        extra_kwargs = {
            'id': {'read_only': True},
            'triggered': {'read_only': True},
        }


class TriggerSerializer(serializers.Serializer):
    currentPrice = serializers.IntegerField()