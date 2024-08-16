from django.urls import path, include
from main.views import *


def urls_factory(viewsets_cls):
    return [path("", viewsets_cls.as_view({"get": "list"})),
            path("create", viewsets_cls.as_view({"post": "create"})),
            path("<int:pk>",
                 viewsets_cls.as_view({"get": "retrieve"})),
            path("<int:pk>/update",
                 viewsets_cls.as_view({"patch": "partial_update"})),
            path("<int:pk>/delete", viewsets_cls.as_view({"delete": "destroy"}))]


vehicle_urls = urls_factory(VehicleViewSet)
driver_urls = urls_factory(DriverViewSet)
route_urls = urls_factory(RouteViewSet)

urlpatterns = [path("vehicle/", include(vehicle_urls)),
               path("driver/", include(driver_urls)),
               path("route/", include(route_urls))]
