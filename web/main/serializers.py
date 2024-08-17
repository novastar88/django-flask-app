from rest_framework import serializers
from main.models import *


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"


class VehicleSerializer(serializers.ModelSerializer):
    driver = DriverSerializer(read_only=True)
    route = RouteSerializer(read_only=True)

    class Meta:
        model = Vehicle
        fields = "__all__"
        read_only_fields = ["last_update"]
