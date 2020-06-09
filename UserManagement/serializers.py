from rest_framework import serializers

from django import forms

from .models import User
from .models import Research
from .models import Dashboard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = '__all__'

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = '__all__'
