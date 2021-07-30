from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id', 'targetPrice', 'status']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class AlertDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id', 'status']
        extra_kwargs = {
            'id': {'read_only': True},
        }