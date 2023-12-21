import os

LEVEL_COUNTER = int(os.getenv("LEVEL_COUNTER", "2"))
LEVEL_CAPACITY = int(os.getenv("LEVEL_CAPACITY", "20"))
MODE = os.getenv("MODE", "DEBUG")  # TODO
ALLOWED_BUFFER_LEN = 5
