from django.db import models


class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    nationality = models.CharField(
        max_length=2, help_text="ISO 3166-1 alpha-2")


class Route(models.Model):
    departure_point = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)


class Vehicle(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=10, unique=True)
    driver = models.ForeignKey(
        to=Driver, on_delete=models.PROTECT, null=True, blank=True)
    route = models.ForeignKey(
        to=Route, on_delete=models.PROTECT, null=True, blank=True)
    occupied = models.BooleanField(
        editable=False, help_text="Auto managed field")
    functional = models.BooleanField()
    remaining_fuel = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="Percentage of fuel remaining in tank")
