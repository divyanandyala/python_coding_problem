
class Circle:
    pi = 3.14

    @classmethod
    def calculate_area(cls, radius):
        area = cls.pi * radius * radius
        return area


r = float(input("Enter radius: "))

result = Circle.calculate_area(r)

print("Area of Circle:", result)
