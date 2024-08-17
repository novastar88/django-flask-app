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

urlpatterns = [path("vehicle/", include(urls_factory(VehicleViewSet))),
               path("driver/", include(urls_factory(DriverViewSet))),
               path("route/", include(urls_factory(RouteViewSet)))]
