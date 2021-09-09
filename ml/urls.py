from django.urls import path,include
from .views import ml_view


urlpatterns = [
    path('api/ml',ml_view),
]
