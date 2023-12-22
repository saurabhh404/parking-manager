import heapq
from app import constants, utils


class ParkingLotTracker:
    def __init__(self):
        # create parking spots and convert it into heap
        self.parking_spots = utils.create_spots()
        heapq.heapify(self.parking_spots)
        # initialize dict for parked variables
        self.parked_vehicles = {}

    def print_stats(self):
        """
        [DEBUG]
        Print class variables
        """
        print("\n:::: DEBUG STATS ::::")
        print(f"Available Spots: {self.parking_spots}")
        print(f"Parked Vehicles: {self.parked_vehicles}")
        print(":::::::::::::::::::::\n")

    def check_if_vehicle_parked(self, vehicle_number):
        """
        Return spot if vehicle is parked, else False
        """
        return self.parked_vehicles.get(vehicle_number, False)

    def add_new_parking(self):
        """
        Add new vehicle by assigning nearest parking spot
        Uses heapq.heappop()
        """
        if not self.parking_spots:
            print("ERROR: Parking lot is currently at capacity.\n")
            return

        vehicle_number = utils.accept_vehicle_number()
        spot = self.check_if_vehicle_parked(vehicle_number)
        if spot:
            print(
                f"ERROR: Vehicle {vehicle_number} is already parked at {utils.reformat_spot(spot)}.\n"
            )
            return

        spot = heapq.heappop(self.parking_spots)

        self.parked_vehicles[vehicle_number] = spot
        print(f"Assigned Spot: {utils.reformat_spot(spot)}\n")
        return

    def fetch_parking_spot(self):
        """
        Checks if vehicle is parked and then fetches the spot
        in required format
        """
        vehicle_number = utils.accept_vehicle_number()
        spot = self.check_if_vehicle_parked(vehicle_number)
        if spot:
            print(f"Assigned Spot: {utils.reformat_spot(spot)}\n")
            return
        else:
            print(f"ERROR: Vehicle {vehicle_number} not found in the parking lot.\n")
            return

    def unpark(self):
        """
        Unparks an existing vehicle
        Uses heapq.heappush() to free the parking spot
        """
        vehicle_number = utils.accept_vehicle_number()
        spot = self.check_if_vehicle_parked(vehicle_number)
        if not spot:
            print(f"ERROR: Vehicle {vehicle_number} not found in the parking lot.\n")
            return

        heapq.heappush(self.parking_spots, spot)
        self.parked_vehicles.pop(vehicle_number)

        print(f"Unparked {vehicle_number} from spot: {utils.reformat_spot(spot)}\n")
        return
