from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .models import LevelReading
from .serializers import LevelReadingSerializer


# Create your views here.

@api_view(['GET'])
def get_list(request):
    if request.method == 'GET':
        readings = LevelReading.objects.all().order_by("-sr_num")
        serializer = LevelReadingSerializer(readings, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_reading(request, sr_num):
    queryset = LevelReading.objects.all()
    reading_instance = get_object_or_404(queryset, pk=sr_num)
    serializer = LevelReadingSerializer(reading_instance)
    return Response(serializer.data)


@api_view(['GET'])
def get_latest(request):
    latest_reading = LevelReading.objects.order_by("-id")[0]
    serializer = LevelReadingSerializer(latest_reading)
    return Response(serializer.data)


@api_view(['POST'])
def post_reading(request):
    serializer = LevelReadingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_readings(request):
    readings = LevelReading.objects.all()
    readings.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
