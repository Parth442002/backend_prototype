from django.urls import path, include
from .views import CustomerViewSet, AddressViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet, 'customer')
router.register(r'address', AddressViewSet, 'address')

urlpatterns = [
    path('api/', include(router.urls)),
]

