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
    list_display = ("pk", "make", "model", "plate_number", "driver",
                    "route", "occupied", "functional", "remaining_fuel",)
    list_filter = ("route", "occupied", "functional",)
    ordering = ("pk",)
