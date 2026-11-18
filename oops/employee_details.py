class Employee:

    def __init__(self, eid, name, salary):
        self.eid = eid
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.eid)
        print("Name:", self.name)
        print("Salary:", self.salary)


e1 = Employee(101, "Divya", 25000)

e1.display()