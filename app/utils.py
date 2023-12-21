import string
from app import constants


def is_valid_config():
    validation_array = [
        0 < constants.LEVEL_COUNTER < 27,
        0 < constants.LEVEL_CAPACITY < 500,
    ]
    return all(validation_array)


def is_valid_choice(choice):
    try:
        return 1 <= int(choice) <= 4
    except:
        return False


def create_level(counter):
    return [x for x in string.ascii_uppercase][counter]


def create_spots(level_counter, level_capacity):
    result = []
    spot_acc = 0
    for level in range(level_counter):
        level_label = create_level(level)
        result.extend(
            [{level_label: spot_acc + i} for i in range(1, level_capacity + 1)]
        )
        spot_acc += level_capacity
    return result


def accept_vehicle_number():
    while True:
        vehicle_number = input("Enter Vehicle number: ")
        if not vehicle_number:
            print("Please enter a valid vehicle number.")
            continue
        return vehicle_number


def reformat_spot(spot):
    try:
        return {"level": list(spot.keys())[0], "spot": list(spot.values())[0]}
    except:
        return None
