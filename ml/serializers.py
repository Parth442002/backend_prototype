from rest_framework import serializers
from .models import PostResponse

class PostResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostResponse
        fields = ["store_delivery","rider_store",'packaging_time','rating']

