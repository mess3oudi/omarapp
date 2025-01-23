from rest_framework import serializers
from .models import Accessory, Bar, RedeauAccessory

class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = ['id', 'name', 'price']

class BarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bar
        fields = ['id', 'name', 'price']

class RedeauAccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RedeauAccessory
        fields = ['id', 'name', 'price']
