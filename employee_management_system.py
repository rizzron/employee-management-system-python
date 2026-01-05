from employee import *
from typing import List, Optional, Dict


class EMS:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        print(f"Successfully added {employee.name} to the list.")

    def get_employee_details_by_id(self, emp_id: int) -> Employee | None:
        for emp in self.employees:
            if emp.get_id() == emp_id:
                print(f"ID {emp_id} is assigned to {emp.name}. The employee details is given below: ")
                emp.get_info()
                return emp
        print(f"No employee found with ID {emp_id}.")
        return None

    def get_employee_details_by_name(self, emp_name: str) -> Employee | None:
        for emp in self.employees:
            if emp.name == emp_name:
                print(f"The employee with the name '{emp_name}' is found. The employee details is given below: ")
                emp.get_info()
                return emp
        print(f"No employee found with the name {emp_name}.")
        return None

    def remove_employee_by_id(self, emp_id: int) -> bool:
        for emp in self.employees:
            if emp.id == emp_id:
                self.employees.remove(emp)
                return True
            print("Didn't found an employee with this ID")
            return False

    def get_all_employee(self):
        for emp in self.employees:
            print(emp.name)

    def get_employee_by_role(self, emp_role: str):
        print(f"The employees with the {emp_role} role are given below: ")
        for emp in self.employees:
            if emp.role == emp_role:
                print(emp.name)


