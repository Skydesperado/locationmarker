from django.shortcuts import render, get_object_or_404
from django.views import View

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.location.models import Location
from apps.location.apis.serializers import LocationSerializer
from apps.location.permissions import IsOwner
from apps.location.services.geocoding import geocode_address


class LocationListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        locations = Location.objects.filter(user=request.user)
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LocationDetailView(View):
    template_name = "location.html"

    def get(self, request, pk, *args, **kwargs):
        location = get_object_or_404(Location, pk=pk, user=request.user)
        context = {
            "location": location,
            "address": location.address,
            "latitude": location.latitude,
            "longitude": location.longitude,
        }
        return render(request, self.template_name, context)


class LocationCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        address = request.data.get("address")
        if not address:
            return Response({"Error": "Address Field Is Required"}, status=status.HTTP_400_BAD_REQUEST)

        latitude, longitude = geocode_address(address)
        if not latitude or not longitude:
            return Response({"Error": "Invalid Address"}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            "address": address,
            "latitude": latitude,
            "longitude": longitude,
        }

        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            location = serializer.save(user=request.user)
            return Response(LocationSerializer(location).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationRetrieveAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self, pk):
        return Location.objects.filter(pk=pk, user=self.request.user).first()

    def get(self, request, pk, *args, **kwargs):
        location = self.get_object(pk)
        if location:
            serializer = LocationSerializer(location)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"Error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)


class LocationUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self, pk):
        return Location.objects.filter(pk=pk, user=self.request.user).first()

    def put(self, request, pk, *args, **kwargs):
        location = self.get_object(pk)
        if location:
            serializer = LocationSerializer(location, data=request.data, partial=True)
            if serializer.is_valid():
                address = request.data.get("address")
                if address:
                    latitude, longitude = geocode_address(address)
                    if latitude and longitude:
                        serializer.validated_data.update({"latitude": latitude, "longitude": longitude})
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)


class LocationDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self, pk):
        return Location.objects.filter(pk=pk, user=self.request.user).first()

    def delete(self, request, pk, *args, **kwargs):
        location = self.get_object(pk)
        if location:
            location.delete()
            return Response({"Message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"Error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
