# Parking Lot Tracker

### Problem Statement

There is a parking lot and it has 2 levels A and B, each level has the capacity to park 20
vehicles of any size. Level A has parking space numbered from 1-20 and level B has parking
space numbered from 21-40. Use this information to build a system that supports below
mentioned operations.

1. Automatically assign a parking space to a new vehicle.
2. Retrieve parking spot number of any particular vehicle(consider vehicle number as the
   unique identifier of the vehicle.) output should return level and parking spot number. \
   e.g. `{"level": A, "spot":19}`
3. Unpark the Vehicle
4. Retrieve the nearest parking location if vehicle is unparked. (eg:A1 A2 A3 is parked and
   vehicle from A2 is unparked then next vehicle will be parked in A2 even if other slots are
   empty.)

● Design and build a terminal based application which facilitates above two operations in a scalable and efficient manner. \
● Keep the code modular clean and optimised. \
● Avoid using a database by using in-memory storage (RAM) \
● Share the link of the github repository (It is a must) for final assessment.

### Steps to run

1. Set the following config variables

   ```
   LEVEL_COUNTER -- (int) Number of levels, default 2 (A and B)
   LEVEL_CAPACITY -- (int) Per level parking capacity, default 20
   MODE -- (str) Set to DEBUG for enabling debug stats, default TEST
   ```

1. Run the wrapper file to start Application Menu
   ```
   python app/wrapper.py
   ```

---

> 💡Developed solely using inbuilt functions, no additional dependencies are required.
