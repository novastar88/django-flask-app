from django.db import models


# class Driver(models.Model):
#     first_name = models.CharField(max_length=50)
#     surname = models.CharField(max_length=50)
#     nationality = models.CharField(
#         max_length=2, help_text="ISO 3166-1 alpha-2")


# class Route(models.Model):
#     ...


# class Vehicle(models.Model):
#     plate_number = models.CharField(max_length=10)
#     driver = models.ForeignKey(to=Driver, on_delete=models.PROTECT)
#     route = models.ForeignKey(to=Route, on_delete=models.PROTECT)
