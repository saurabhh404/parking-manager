from app import constants, utils


class ParkingLotTracker:
    def __init__(self):
        # import configs
        self.level_counter = constants.LEVEL_COUNTER
        self.level_capacity = constants.LEVEL_CAPACITY
        # create parking spots
        self.available_spots = utils.create_spots(
            self.level_counter, self.level_capacity
        )
        # initialize usage variables
        self.unparked_spots = []
        self.parked_vehicles = {}

    def print_stats(self):
        print("\n:::: Stats ::::")
        print(f"Available Spots: {self.available_spots}")
        print(f"Unparked Spots: {self.unparked_spots}")
        print(f"Parked Vehicles: {self.parked_vehicles}")
        print(
            f"Spot Count [Must be {constants.LEVEL_CAPACITY * constants.LEVEL_COUNTER}]: "
            + f"{len(self.available_spots) + len(self.unparked_spots) + len(self.parked_vehicles)}"
        )
        print(":::::::::::::::\n")

    def check_if_vehicle_parked(self, vehicle_number):
        if vehicle_number in self.parked_vehicles:
            return self.parked_vehicles[vehicle_number]
        else:
            return False

    def add_new_parking(self, vehicle_number):
        if not self.available_spots:
            return "ERROR: Parking lot is currently at capacity."
        if self.check_if_vehicle_parked(vehicle_number):
            return f"ERROR: Vehicle {vehicle_number} is already parked."

        spot = (
            self.unparked_spots.pop(0)
            if self.unparked_spots
            else self.available_spots.pop(0)
        )
        self.parked_vehicles[vehicle_number] = spot
        return f"Assigned Spot: {utils.reformat_spot(spot)}"

    def fetch_parking_spot(self, vehicle_number):
        vehicle = self.check_if_vehicle_parked(vehicle_number)
        return (
            f"ERROR: Vehicle {vehicle_number} not found in the parking lot."
            if not vehicle
            else f"Assigned Spot: {utils.reformat_spot(vehicle)}"
        )

    def unpark(self, vehicle_number):
        vehicle = self.check_if_vehicle_parked(vehicle_number)
        if not vehicle:
            return f"ERROR: Vehicle {vehicle_number} not found in the parking lot."

        self.unparked_spots.append(vehicle)
        self.parked_vehicles.pop(vehicle_number)
        self.manage_buffer()
        next_nearest = (
            (self.unparked_spots[0] if self.unparked_spots else self.available_spots[0])
            if (self.unparked_spots or self.available_spots)
            else None
        )  # TODO: refactor

        return (
            f"Unparked {vehicle_number} from spot {utils.reformat_spot(vehicle)}\n"
            + f"Next nearest parking spot: {utils.reformat_spot(next_nearest)}"
        )

    def manage_buffer(self):
        self.unparked_spots.sort(key=lambda x: list(x.values())[0])
        if len(self.unparked_spots) > constants.ALLOWED_BUFFER_LEN:
            self.available_spots = sorted(
                (self.unparked_spots + self.available_spots),
                key=lambda x: list(x.values())[0],
            )  # TODO: common sort stmt
            self.unparked_spots = []
