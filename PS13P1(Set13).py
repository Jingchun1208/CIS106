class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.pay = salary
        self.email = self.first + '.' + self.last + '@company.com'

    def fullname (self):
        return '{} {}'.format(self.first,self.last)

    def bonus(self):
        return self.pay * 0.10  

class Manager(Employee):
    def long_term_bonus(self):
        return self.pay * 0.40  

class Executive(Manager):  
    def long_term_bonus(self):
        return self.pay * 0.50  

    def executive_bonus(self):
        return self.pay * 2.00  

employee1 = Employee("Sam", "White", 50000)
manager1 = Manager("John", "Brown", 60000)
executive1 =Executive("Sarah", "Lee", 70000)

print(f"{employee1.fullname()} ({employee1.email}) has a salary of ${employee1.pay} and a bonus of ${employee1.bonus():.2f}")

print(f"{manager1.fullname()} ({manager1.email}) has a salary of ${manager1.pay}, a 10% bonus of ${manager1.bonus():.2f}, and a long-term bonus of ${manager1.long_term_bonus():.2f}")

print(f"{executive1.fullname()} ({executive1.email}) has a salary of ${executive1.pay}, a 10% bonus of ${executive1.bonus():.2f}, a long-term bonus of ${executive1.long_term_bonus():.2f}, and an executive bonus of ${executive1.executive_bonus():.2f}")
