class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.pay = salary
        self.email = f"{self.first}.{self.last}@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def bonus(self):
        return self.pay * 0.10 
    def total_salary(self):
        return self.pay + self.bonus()  

employee1 = Employee("Sam", "White", 50000)
employee2 = Employee("John", "Brown", 60000)
employee3 = Employee("Sarah", "Lee", 70000)


for employee in [employee1, employee2, employee3]:
    total_salary = employee.total_salary()
    print("$", format(total_salary, ".2f"), "is", employee.fullname(), f"({employee.email})'s salary with a 10% bonus.")
