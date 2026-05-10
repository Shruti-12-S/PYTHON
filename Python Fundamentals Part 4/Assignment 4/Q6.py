'''
Concept: Abstraction
Create an abstract class Employee with an abstract method calculate_salary().
Create subclasses Intern, FullTimeEmployee, and ContractEmployee that implement the method differently.
'''
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self,stipend):
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend

class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary, bonus):
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.monthly_salary + self.bonus


class ContractEmployee(Employee):
    def __init__(self, hours_worked, rate_per_hour):
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        return self.hours_worked * self.rate_per_hour
    
# Creating objects
i1 = Intern(15000)
f1 = FullTimeEmployee(50000, 10000)
c1 = ContractEmployee(120, 500)

# Display salaries
print("Intern Salary:", i1.calculate_salary())
print("Full Time Employee Salary:", f1.calculate_salary())
print("Contract Employee Salary:", c1.calculate_salary())