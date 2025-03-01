class Vehicle:
    def fueltype(self):
        return "General Fuel"
class Car (Vehicle):
    def fueltype(self):
        return "Petrol or Diesel"
class Bike (Vehicle):
    def fueltype(self):
        return "Petrol "
car = Car()
bike = Bike()
print("Car fuel type:", car.fueltype())
print("Bike fuel type:", bike.fueltype())
