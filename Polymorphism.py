# The Parent Blueprint
class Vehicle:
    def drive(self):
        pass  # A placeholder that says "all vehicles can drive"

# Child Class 1
class Car(Vehicle):
    def drive(self):
        return "The car zooms down the highway at 100 mph! 🏎️💨"

# Child Class 2
class Truck(Vehicle):
    def drive(self):
        return "The truck rumbles slowly at 40 mph, carrying heavy logs. 🚛"

# --- Testing our game ---
# We put both vehicles into a list (like a garage)
garage = [Car(), Truck()]

# One command loop: we tell EVERYTHING in the garage to drive
for vehicle in garage:
    print(vehicle.drive())