from django.test import TestCase, SimpleTestCase, TransactionTestCase
from rest_framework.test import APIClient
import main.models as models
from django.core.exceptions import ObjectDoesNotExist


class TestDriver(TransactionTestCase):
    fixtures = ["fixtures_minimal"]
    url_model_root = "/api/driver"

    def setUp(self) -> None:
        self.client = APIClient()
        self.client.login(username="admin", password="admin")
        return super().setUp()

    def test_get_list(self):
        req = self.client.get(
            "".join([self.url_model_root, "/"]), format="json")

        self.assertEqual(req.status_code, 200)
        self.assertIsInstance(req.json(), list)
        self.assertEqual(2, len(req.json()))

    def test_retrieve(self):
        req = self.client.get("/".join([self.url_model_root, "1"]))

        self.assertEqual(req.status_code, 200)

    def test_update(self):
        url = "/".join([self.url_model_root, "1", "update"])
        req = self.client.patch(url, {"age": 35, "surname": "test"})

        self.assertEqual(200, req.status_code)

        db_obj = models.Driver.objects.get(pk=1)
        self.assertEqual(35, db_obj.age)
        self.assertEqual("test", db_obj.surname)

    def test_delete(self):
        url = "/".join([self.url_model_root, "2", "delete"])
        req = self.client.delete(url)

        self.assertEqual(204, req.status_code)

        with self.assertRaises(ObjectDoesNotExist):
            models.Driver.objects.get(pk=2)

    def test_creation(self):
        to_send = dict(first_name="test1", surname="test2",
                       age=20, nationality="GB")
        url = "/".join([self.url_model_root, "create"])
        req = self.client.post(url, to_send, format="json")

        self.assertEqual(201, req.status_code)

        models.Driver.objects.get(**to_send)


class TestRoute(TransactionTestCase):
    fixtures = ["fixtures_minimal"]
    url_model_root = "/api/route"

    def setUp(self) -> None:
        self.client = APIClient()
        self.client.login(username="admin", password="admin")
        return super().setUp()

    def test_get_list(self):
        req = self.client.get(
            "".join([self.url_model_root, "/"]), format="json")

        self.assertEqual(req.status_code, 200)
        self.assertIsInstance(req.json(), list)
        self.assertEqual(2, len(req.json()))

    def test_retrieve(self):
        req = self.client.get("/".join([self.url_model_root, "1"]))

        self.assertEqual(req.status_code, 200)

    def test_update(self):
        url = "/".join([self.url_model_root, "1", "update"])
        req = self.client.patch(url, {"destination": "test"})

        self.assertEqual(200, req.status_code)

        db_obj = models.Route.objects.get(pk=1)
        self.assertEqual("test", db_obj.destination)

    def test_delete(self):
        url = "/".join([self.url_model_root, "2", "delete"])
        req = self.client.delete(url)

        self.assertEqual(204, req.status_code)

        with self.assertRaises(ObjectDoesNotExist):
            models.Route.objects.get(pk=2)

    def test_creation(self):
        to_send = dict(departure_point="test1", destination="test2")
        url = "/".join([self.url_model_root, "create"])
        req = self.client.post(url, to_send)

        self.assertEqual(201, req.status_code)

        models.Route.objects.get(**to_send)


class TestVehicle(TransactionTestCase):
    fixtures = ["fixtures_minimal"]
    url_model_root = "/api/vehicle"

    def setUp(self) -> None:
        self.client = APIClient()
        self.client.login(username="admin", password="admin")
        return super().setUp()

    def test_get_list(self):
        req = self.client.get(
            "".join([self.url_model_root, "/"]), format="json")

        self.assertEqual(req.status_code, 200)
        self.assertIsInstance(req.json(), list)
        self.assertEqual(2, len(req.json()))

    def test_retrieve(self):
        req = self.client.get("/".join([self.url_model_root, "1"]))

        self.assertEqual(req.status_code, 200)

    def test_update(self):
        url = "/".join([self.url_model_root, "1", "update"])
        req = self.client.patch(url, {"make": "test", "model": "test2"})

        self.assertEqual(200, req.status_code)

        db_obj = models.Vehicle.objects.get(pk=1)
        self.assertEqual("test", db_obj.make)
        self.assertEqual("test2", db_obj.model)

    def test_delete(self):
        url = "/".join([self.url_model_root, "2", "delete"])
        req = self.client.delete(url)

        self.assertEqual(204, req.status_code)

        with self.assertRaises(ObjectDoesNotExist):
            models.Vehicle.objects.get(pk=2)

    def test_creation(self):
        to_send = dict(make="test1", model="test2", plate_number="77777",
                       track_external_id=3, remaining_fuel=100)
        url = "/".join([self.url_model_root, "create"])
        req = self.client.post(url, to_send, format="json")

        self.assertEqual(201, req.status_code)

        models.Vehicle.objects.get(**to_send)
