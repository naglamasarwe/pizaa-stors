from datetime import datetime
from random import random


class Employee:
 def __init__(self,employee_id,first_name,last_name,adress,salary,start_date,pizza_rank,pizza_rank_date,surprise):
     self.employee_id = employee_id
     self.first_name = first_name
     self.last_name = last_name
     self.adress = adress
     self.salary = salary
     self.start_date = start_date
     self.pizza_rank = pizza_rank
     self.pizza_rank_date = pizza_rank_date
     self.surprise = surprise


 def set_rank(self):
     self.pizza_rank = random.randint(1-100)
     self.start_date = datetime.now()

