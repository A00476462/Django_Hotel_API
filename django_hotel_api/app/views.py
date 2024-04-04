from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view

from .models import Hotels
from app.serializers import HotelSerializers
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def home(request):
    return HttpResponse("hello world!")

@api_view(["GET", "POST"])
def gethotels(request):
    if request.method == "GET":
        hotels = Hotels.objects.all()
        hotelSerializers = HotelSerializers(hotels, many = True)
        return Response(hotelSerializers.data)
    elif request.method == "POST":
        serializer = HotelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_hotel_by_id(request, id):
    if request.method == "GET":
        try:
            hotel = Hotels.objects.get(id=id)
            serializer = HotelSerializers(hotel)
            return Response(serializer.data)
        except Hotels.DoesNotExist:
            return Response({"message": "Hotel not found"}, status=status.HTTP_404_NOT_FOUND)
