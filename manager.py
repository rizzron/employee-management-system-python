from full_time_employee import *

import textwrap


class Manager(FullTimeEmployee):
    role: str = "Manager"

    def __init__(self, name: str, salary: int):
        super().__init__(name, salary)
        print(f"New {self.role} ID for {self.name} has been created successfully.")

    def get_salary(self):
        print(f"The salary of {self.role} {self.name} is {self.salary:.2f}")

    def get_info(self):
        info = textwrap.dedent(f"""
        Employee name: {self.name}
        Employee ID: {self.id}
        Employment Type: {FullTimeEmployee.employment_type}
        Salary Amount: {self.salary:.2f}
        """)
        print(info)

    def give_increment(self):
        self.salary *= 1.10
        print(f"Salary increment is successfully done for '{self.name}'")

