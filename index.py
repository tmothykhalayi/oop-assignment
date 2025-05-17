# Base class: Vehicle
class Vehicle:
    def __init__(self, brand, model, year):
        self._brand = brand      # Encapsulation with protected attribute
        self._model = model
        self._year = year

    def move(self):
        print("The vehicle moves...")

    def info(self):
        return f"{self._year} {self._brand} {self._model}"


# Subclass: Car
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def move(self):
        print("Driving on the road 🚗")


# Subclass: Plane
class Plane(Vehicle):
    def __init__(self, brand, model, year, airline):
        super().__init__(brand, model, year)
        self.airline = airline

    def move(self):
        print("Flying in the sky ✈️")


# Subclass: Boat
class Boat(Vehicle):
    def __init__(self, brand, model, year, boat_type):
        super().__init__(brand, model, year)
        self.boat_type = boat_type

    def move(self):
        print("Sailing on the water 🚢")


# -------------------------------
# 🎭 Polymorphism Demonstration
# -------------------------------

# Create instances of each vehicle type
my_car = Car("Toyota", "Corolla", 2022, 4)
my_plane = Plane("Boeing", "747", 2018, "Delta Airlines")
my_boat = Boat("Yamaha", "FX Cruiser", 2020, "Jet Ski")

# Store all in a list of type Vehicle
vehicles = [my_car, my_plane, my_boat]

# Loop through and demonstrate polymorphic move() behavior
for v in vehicles:
    print(v.info())
    v.move()
    print("---")
