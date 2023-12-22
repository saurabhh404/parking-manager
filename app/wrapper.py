import os
import sys
import traceback

app_directory_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(app_directory_path)
# The above two lines can be replaced by updating PYTHONPATH in ENV itself
from app import parking_lot_tracker as main, utils, constants


def menu(parking):
    """
    Starts menu for the application
    """
    print("Welcome to Parking Lot Tracker!")
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
            parking.add_new_parking()
        elif choice == 2:
            parking.fetch_parking_spot()
        elif choice == 3:
            parking.unpark()
        else:
            print("Exiting..")
            break


if __name__ == "__main__":
    try:
        if not utils.is_valid_config():
            print(
                "Invalid configuration detected.\n" + "Allowed config: ",
                {"LEVEL_CAPACITY": "1 <= x <= 1000", "LEVEL_COUNTER": "1 <= x <= 26"},
            )
            exit()
        parking = main.ParkingLotTracker()
        menu(parking)
    except KeyboardInterrupt:
        print("Exited")
    except Exception as ex:
        traceback.print_exc()
