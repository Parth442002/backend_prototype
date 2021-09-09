from django.urls import path, include
from rest_framework import routers
from .views import RiderViewSet, StoreViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'rider', RiderViewSet, 'rider')
router.register(r'store', StoreViewSet, 'store')
router.register(r'product', ProductViewSet, 'product')


urlpatterns = [
    path('api/', include(router.urls)),
]
