from django.contrib import admin
from main.models import *


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("pk", "first_name", "surname", "age", "nationality",)
    list_filter = ("nationality",)
    ordering = ("pk",)


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ("pk", "departure_point", "destination",)
    ordering = ("pk",)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("pk", "make", "model", "plate_number", "track_external_id", "driver", "route", "functional",
                    "remaining_fuel", "speed_kmh", "distance_traveled_km", "current_weight_kg", "last_update",)
    list_filter = ("route", "functional", "driver",)
    ordering = ("pk",)
