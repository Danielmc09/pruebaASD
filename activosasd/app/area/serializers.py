from rest_framework import serializers

from .models import Area


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        exclude = ['created', 'update']
