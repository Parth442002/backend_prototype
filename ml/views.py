from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .models import PostResponse
from .serializers import PostResponseSerializer
import pickle

def prediction_model(store_delivery,rider_store,packaging_time,rating):
    x = [[store_delivery,rider_store,packaging_time,rating]]
    voting_classifier = pickle.load(open('/Users/parthkatiyar/Desktop/shadowfax/backend_prototype/ml/svm_model.sav','rb'))
    prediction = voting_classifier.predict(x)
    return prediction


@api_view(['POST'])
def ml_view(request):
    """
    List all code snippets, or create a new snippet.

    """

    if request.method == 'POST':

        serializer = PostResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            store_delivery=serializer.data.pop('store_delivery')
            rider_store=serializer.data.pop('rider_store')
            packaging_time=serializer.data.pop('packaging_time')
            rating=serializer.data.pop("rating")
            result=prediction_model(store_delivery,rider_store,packaging_time,rating)
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

