from rest_framework import serializers

from .models import Event


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ['user']
