from rest_framework import serializers
from django import forms

from .models import Inventory


# transformation from model to json
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'