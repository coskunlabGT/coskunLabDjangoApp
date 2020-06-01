from django.shortcuts import render
import json
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['DELETE'])
def delete_Item(request):
    body_unicode = request.body.decode('utf-8')
    try:
        body_data = json.loads(body_unicode)
        item_id = body_data["item_id"]
        item = Inventory.objects.get(id = item_id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_500_BAD_REQUEST)

@api_view(['POST'])
def add_Item(request):
    serializer = InventorySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['GET'])
def get_Item(request):
    body_unicode = request.body.decode('utf-8')
    try:
        body_data = json.loads(body_unicode)
        item_id = body_data["item_id"]
        item = Inventory.objects.get(id = item_id)
        serializer = InventorySerializer(item)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_500_BAD_REQUEST)
    

@api_view(['PUT'])
def modify_Item(request):
    try:
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        

        item_id = body_data["item_id"]

        if ("item_name" in body_data.keys()):
            new_name = body_data["item_name"]
            Inventory.objects.filter(pk = item_id).update(item_name=new_name)
        if ("current_level" in body_data.keys()):
            new_current_level = body_data["current_level"]
            Inventory.objects.filter(pk = item_id).update(current_level=new_current_level)
        if ("target_level" in body_data.keys()):
            new_target_level = body_data["target_level"]
            Inventory.objects.filter(pk = item_id).update(target_level=new_target_level)
        if ("price" in body_data.keys()):
            new_price = body_data["price"]
            Inventory.objects.filter(pk = item_id).update(price=new_price)
        if ("isOrdered" in body_data.keys()):
            new_isOrdered = body_data["isOrdered"]
            Inventory.objects.filter(pk = item_id).update(isOrdered=new_isOrdered)
        if ("refillNeeded" in body_data.keys()):
            new_refillNeeded = body_data["refillNeeded"]
            Inventory.objects.filter(pk = item_id).update(refillNeeded=new_refillNeeded)
        
        
        item = Inventory.objects.get(pk = item_id)
        serializer = InventorySerializer(item)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_500_BAD_REQUEST)