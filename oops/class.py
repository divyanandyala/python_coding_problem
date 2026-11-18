class Student:

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


# Creating object
s1 = Student()

s1.name = "Divya"
s1.age = 22
s1.course = "Python"

s1.display()