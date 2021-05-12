from django.shortcuts import render
from rest_framework.decorators import api_view

from django.http import Http404 
from rest_framework.response import Response
from rest_framework import status
from .serializers import GeneralOrderSerializer
from .database_abstractions import getAllGeneralOrderObjects
from .models import GenOrderTable
from .message_views import getApproval


# Create your views here.
@api_view(['POST'])
def addGeneralOrder(request):
    serializer = GeneralOrderSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        getApproval(request._request, serializer.data.get("order_id"), serializer.data.get("item_id"))
        return Response(serializer.data, status = status.HTTP_200_OK)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)






    # Create your views here.
@api_view(['GET'])
def getGeneralOrders(request):
    try:
        allitems = getAllGeneralOrderObjects()
        serializer = GeneralOrderSerializer(allitems, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    except:
        return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)




