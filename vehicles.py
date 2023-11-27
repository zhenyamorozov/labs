class Vehicle:
    def move(self):
        raise NotImplementedError("move() not implemented")

class LandVehicle(Vehicle):
    def move(self):
        print("Driving....")

class WheeledVehicle(LandVehicle):
    def move(self):
        print("Wheels are spinning...")
        LandVehicle.move(self)

class TrackedVehicle(LandVehicle):
    def move(self):
        print("Tracks are rolling...")
        LandVehicle.move(self)


red_car = WheeledVehicle()
red_car.move()
yellow_car = WheeledVehicle()
selected_car = red_car

blue_tractor = TrackedVehicle()
blue_tractor.move()

print(issubclass(WheeledVehicle, Vehicle))
print(isinstance(red_car, TrackedVehicle))
print(red_car is selected_car)
print(selected_car is red_car)
