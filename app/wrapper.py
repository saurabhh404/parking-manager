import os
import sys
import traceback

app_directory_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(app_directory_path)
# The above two lines can be replaced by updating PYTHONPATH in ENV itself
from app import parking_lot_tracker as main, utils, constants


def menu(parking):
    print("Welcome to Parking Lot Tracker.")
    while True:
        if constants.MODE == "DEBUG":
            parking.print_stats()

        choice = input(
            "\nMenu\n"
            + "1. Assign a parking space to a new vehicle\n"
            + "2. Retrieve Parking spot number\n"
            + "3. Unpark a vehicle\n"
            + "4. Exit\n"
            + "Choice: ",
        )
        if not utils.is_valid_choice(choice):
            print("ERROR: Please enter a valid choice.\n")
            continue

        choice = int(choice)

        if choice == 1:
            vehicle_number = utils.accept_vehicle_number()
            result = parking.add_new_parking(vehicle_number)
            print(result, "\n")
        elif choice == 2:
            vehicle_number = utils.accept_vehicle_number()
            result = parking.fetch_parking_spot(vehicle_number)
            print(result, "\n")
        elif choice == 3:
            vehicle_number = utils.accept_vehicle_number()
            result = parking.unpark(vehicle_number)
            print(result, "\n")
        else:
            print("Exiting..")
            break


if __name__ == "__main__":
    try:
        if not utils.is_valid_config():
            print(
                "Invalid configuration detected.\n" + "Allowed config: ",
                {"LEVEL_CAPACITY": "0 < x < 500", "LEVEL_COUNTER": "0 < x < 27"},
            )
            exit()
        parking = main.ParkingLotTracker()
        menu(parking)
    except KeyboardInterrupt:
        print("Exited")
    except Exception as ex:
        traceback.print_exc()
