from rest_framework import serializers

from apps.location.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "address", "latitude", "longitude", "created_at", "updated_at")
        read_only_fields = ("user", "created_at", "updated_at")
