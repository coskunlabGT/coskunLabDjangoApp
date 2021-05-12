from rest_framework import serializers
from django import forms
from .models import GenOrderTable
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class GeneralOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenOrderTable
        fields = '__all__'