
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)
        print("Car Price:", self.price)


car1 = Car("Toyota", "Innova", 2000000)
car2 = Car("Honda", "City", 1500000)

car1.display()
print("----------------")
car2.display()
