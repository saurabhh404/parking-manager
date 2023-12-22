import string
from app import constants


def is_valid_config():
    """
    Validate configs set
    """
    validation_array = [
        1 <= constants.LEVEL_COUNTER <= 26,
        1 <= constants.LEVEL_CAPACITY <= 1000,
    ]
    return all(validation_array)


def is_valid_choice(choice):
    """
    Validate entered Menu choice
    """
    try:
        return 1 <= int(choice) <= 4
    except:
        return False


def get_level(counter):
    """
    Returns Nth letter of alphabet, index starting from 0
    e.g. 0 -> 'A'
    e.g. 5 -> 'F'
    """
    return [x for x in string.ascii_uppercase][counter]


def create_spots():
    """
    Create list of configured spots
    e.g. if LEVEL_CAPACITY = 20 and LEVEL_COUNTER = 2
    then list -> [1, 2, ... 39, 40]
    """
    return list(range(1, (constants.LEVEL_CAPACITY * constants.LEVEL_COUNTER) + 1))


def accept_vehicle_number():
    """
    Accepts Vehicle number in stdin
    Repeats if Vehicle number is not a truthy value
    """
    while True:
        vehicle_number = input("Enter Vehicle number: ")
        if not vehicle_number:  # Can use regex here.
            print("Please enter a valid vehicle number.")
            continue
        return vehicle_number


def reformat_spot(spot):
    """
    Returns spot in required format
    e.g. 1 -> {"level": 'A', "spot": 1}
    """
    return {
        "level": get_level((spot - 1) // constants.LEVEL_CAPACITY),
        "spot": spot,
    }
