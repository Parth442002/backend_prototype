from attr import field
from django.urls import path, include
from rest_framework import serializers
from .models import Address, Customer
# Serializers define the API representation.


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
