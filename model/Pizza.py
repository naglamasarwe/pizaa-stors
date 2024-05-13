from abc import ABC, abstractmethod

import Employee




class Pizza(ABC):
    @abstractmethod
    def __init__(self,pizza_id,name,address,employees, phone_number):
        self.pizza_id = pizza_id
        self.name = name
        self.address = address
        self.employees = employees
        self.phone_number = phone_number


    def number_of_employee(self):
        return len(self.employees)


    def hire_employee(self, employee: Employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def fire_employee(self, employee: Employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def calculate_employee_expenses(self):
        total_employee_salary= 0
        for employee in self.employees:
            total_employee_salary = total_employee_salary + employee.salary
            return total_employee_salary


    @abstractmethod
    def calculate_rank(self):
        pass
