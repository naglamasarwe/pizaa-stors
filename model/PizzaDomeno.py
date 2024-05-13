from overrides import overrides

from model.Pizza import Pizza


class PizzaDomeno(Pizza):
    def __init__(self,pizza_id,name,address,employees, phone_number):
        super().__init__(pizza_id,name,address,employees, phone_number)
        self.store_rank = self.calculate_rank()
    @overrides
    def calculate_rank(self):
        total_employee_rank = 0
        for employee in self.employees:
            total_employee_rank = total_employee_rank + employee.pizza_rank
            self.store_rank = total_employee_rank
        return self.store_rank