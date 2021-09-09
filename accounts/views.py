from django.urls import path, include
from .models import Customer, Address
from .serializers import CustomerSerializer, AddressSerializer
from rest_framework import routers, serializers, viewsets


# ViewSets define the view behavior.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
