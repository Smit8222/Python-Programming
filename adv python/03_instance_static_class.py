class Employee:
    company ="HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("smit", 43232)
e2 = Employee("ram", 32432)
print(Employee.company)        