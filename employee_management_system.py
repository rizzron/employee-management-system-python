from employee import *
from typing import List, Optional, Dict


class EMS:
    def __init__(self):
        self.employees = List[Employee]

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def get_employee_by_id(self, id: int) -> Employee | None:
        for emp in self.employees:
            if(emp.__id == id):
                return emp
        return None



