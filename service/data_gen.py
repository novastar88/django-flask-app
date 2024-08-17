import random


class Generator:

    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.functional = None
        self.remaining_fuel = None
        self.speed_kmh = None
        self.distance_traveled_km = None
        self.current_weight_kg = None

        self.__functional()
        self.__remaining_fuel()
        self.__speed_kmh()
        self.__distance_traveled_km()
        self.__current_weight_kg()

    def __functional(self):
        rand_val = random.randint(0, 10)

        if rand_val <= 2:
            self.functional = False
            return

        self.functional = True

    def __remaining_fuel(self):
        rand_val = random.randint(0, 10000)

        self.remaining_fuel = float(rand_val / 100)

    def __speed_kmh(self):
        if self.functional is True and self.remaining_fuel != 0:
            self.speed_kmh = random.randint(0, 92)
            return

        self.speed_kmh = 0

    def __distance_traveled_km(self):
        self.distance_traveled_km = random.randint(0, 1200)

    def __current_weight_kg(self):
        self.current_weight_kg = random.randint(0, 16000)

    def as_dict(self):
        return dict(vehicle_id=self.vehicle_id,
                    functional=self.functional,
                    remaining_fuel=self.remaining_fuel,
                    speed_kmh=self.speed_kmh,
                    distance_traveled_km=self.distance_traveled_km,
                    current_weight_kg=self.current_weight_kg)