import string
from app import constants


def is_valid_config():
    return (0 < constants.LEVEL_COUNTER < 27) and (0 < constants.LEVEL_CAPACITY < 500)


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
