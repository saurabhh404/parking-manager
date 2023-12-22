import os

# Number of levels, default 2 (A and B)
LEVEL_COUNTER = int(os.getenv("LEVEL_COUNTER", "2"))
# Per level parking capacity, default 20
LEVEL_CAPACITY = int(os.getenv("LEVEL_CAPACITY", "20"))
# Set to DEBUG for enabling debug stats
MODE = os.getenv("MODE", "TEST")
