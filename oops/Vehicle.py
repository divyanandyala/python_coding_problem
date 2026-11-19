
# Parent class
class Vehicle:
    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")


# Child class 1
class Car(Vehicle):
    def car_details(self):
        print("This is a Car")
        print("Car has 4 wheels")


# Child class 2
class Bike(Vehicle):
    def bike_details(self):
        print("This is a Bike")
        print("Bike has 2 wheels")


# Car object
c = Car()
c.start()
c.car_details()
c.stop()


# Bike object
b = Bike()
b.start()
b.bike_details()
b.stop()

