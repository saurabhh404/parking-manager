from app import constants, utils


class ParkingLotTracker:
    def __init__(self):
        # import configs
        self.level_counter = constants.LEVEL_COUNTER
        self.level_capacity = constants.LEVEL_CAPACITY
        self.available_spots = utils.create_spots(
            self.level_counter, self.level_capacity
        )
        self.unparked_spots = []
        self.parked_vehicles = {}

    def print_vars(self):
        print("\n\nVARS", vars(self), "\n\n")

    def add_new_parking(self, vehicle_number):
        if not self.available_spots:
            return "ERROR: Parking lot is currently at capacity."

        spot = (
            self.unparked_spots.pop()
            if self.unparked_spots
            else self.available_spots.pop(0)
        )
        self.parked_vehicles[vehicle_number] = spot
        return spot

    def check_if_vehicle_parked(self, vehicle_number):
        if vehicle_number in self.parked_vehicles:
            return self.parked_vehicles[vehicle_number]
        else:
            return False

    def fetch_parking_spot(self, vehicle_number):
        vehicle = self.check_if_vehicle_parked(vehicle_number)
        return (
            f"ERROR: Vehicle {vehicle_number} not found in the parking lot."
            if not vehicle
            else vehicle
        )

    # TODO: Sort logic for self.unparked_spots
    def unpark(self, vehicle_number):
        vehicle = self.check_if_vehicle_parked(vehicle_number)
        if not vehicle:
            return f"ERROR: Vehicle {vehicle_number} not found in the parking lot."

        self.unparked_spots.append(vehicle)
        del self.parked_vehicles[vehicle_number]
        return True
