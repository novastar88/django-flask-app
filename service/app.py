from flask import Flask
from data_gen import Generator
from flask_caching import Cache
import os
from dotenv import load_dotenv

app_folder = os.path.abspath(os.path.join(__file__, os.pardir))
load_dotenv(
    os.path.join(os.path.abspath(os.path.join(app_folder, os.pardir)), ".env"))

cache = Cache(
    config={
        "DEBUG": True,
        "CACHE_TYPE": "redis",
        "CACHE_REDIS_HOST": os.environ.get("REDIS_CACHE_HOST"),
        "CACHE_REDIS_PORT": os.environ.get("REDIS_CACHE_PORT"),
        "CACHE_REDIS_DB": 1
    })

app = Flask(__name__)
cache.init_app(app)


@app.route("/", methods=["GET"])
def hello_world():
    return "OK"


@app.route("/vehicle_status/<vehicle_id>", methods=["GET"])
@cache.cached(timeout=10)
def vehicle_status_gen(vehicle_id):
    try:
        to_int = int(vehicle_id)
    except ValueError:
        return {"error": "vehicle_id must be a positive integer"}

    return Generator(to_int).as_dict()


if __name__ == "__main__":
    app.run()