
# Parent class
class Animal:
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")



class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def sound(self):
        print("Cat is meowing")


# Creating objects
d = Dog()
d.eat()
d.sleep()
d.bark()

print()

c = Cat()
c.eat()
c.sleep()
c.sound()
