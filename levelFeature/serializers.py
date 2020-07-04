from rest_framework import serializers
from .models import LevelReading


class LevelReadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = LevelReading
        fields = '__all__'
