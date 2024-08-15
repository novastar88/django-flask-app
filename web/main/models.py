from django.db import models
from django.core import validators


class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField(validators=[validators.MinValueValidator(
        18), validators.MaxValueValidator(100)])
    nationality = models.CharField(
        max_length=2, help_text="ISO 3166-1 alpha-2")

    def __str__(self) -> str:
        return " | ".join([self.first_name, self.surname, str(self.age), self.nationality])


class Route(models.Model):
    departure_point = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)

    def __str__(self) -> str:
        return " -> ".join([self.departure_point, self.destination])


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

    def __str__(self) -> str:
        return " | ".join([self.make, self.model, self.plate_number])
