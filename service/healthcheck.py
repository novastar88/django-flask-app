import redis
import os
from dotenv import load_dotenv

app_folder = os.path.abspath(os.path.join(__file__, os.pardir))
load_dotenv(
    os.path.join(os.path.abspath(os.path.join(app_folder, os.pardir)), ".env"))

r = redis.Redis(host=os.environ.get("REDIS_CACHE_HOST"),
                port=os.environ.get("REDIS_CACHE_PORT"),
                db=1)

r.ping()