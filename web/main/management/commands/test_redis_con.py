from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import redis


class Command(BaseCommand):
    def handle(self, *args, **options):
        r = redis.Redis(host=settings.REDIS_CACHE_HOST,
                        port=int(settings.REDIS_CACHE_PORT), db=0)

        try:
            r.ping()
            self.stdout.write(self.style.SUCCESS(
                "Successfully connected to redis"))
        except (redis.exceptions.ConnectionError, ConnectionRefusedError):
            raise CommandError("Redis connection error!")
