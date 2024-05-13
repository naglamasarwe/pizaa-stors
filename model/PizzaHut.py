from overrides import overrides

from Pizza import Pizza


class PizzaHut(Pizza):
    def __init__(self,pizza_id,name,address,employees, phone_number):
        super().__init__(pizza_id,name,address,employees, phone_number)
        self.store_rank = self.calculate_rank()
    @overrides
    def calculate_rank(self):
        total_employee_rank = 0
        for employee in self.employees:
            total_employee_rank = total_employee_rank + employee.pizza_rank
        averagr_rank = total_employee_rank/len(self.employees)
        self.store_rank = averagr_rank
        return self.store_rank
