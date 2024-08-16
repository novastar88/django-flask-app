from django.core.management.base import BaseCommand
from django.conf import settings
import redis


class Command(BaseCommand):
    def handle(self, *args, **options):
        r = redis.Redis(host='localhost', port=6390, db=0)

        try:
            r.ping()
            print("Successfully connected to redis")
        except (redis.exceptions.ConnectionError, ConnectionRefusedError):
            print("Redis connection error!")
            return False

        return True
