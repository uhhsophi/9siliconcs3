# 2a. Create three classes with a move() method
class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

# 2b. Function that takes a vehicle object and calls its move() method
def start_trip(vehicle):
    vehicle.move()

# 2c. Create one object of each class
my_car = Car()
my_boat = Boat()
my_drone = Drone()

# 2d. Call the start_trip() function for each object
start_trip(my_car)
start_trip(my_boat)
start_trip(my_drone)
