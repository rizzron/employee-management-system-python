from part_time_employee import *

import textwrap


class Annotator(PartTimeEmployee, ABC):
    role: str = "Annotator"

    def __init__(self, name: str, id: str, salary: int):
        self.name = name
        self.__id = id
        self.salary = salary
        print(f"New {self.role} ID for {self.name} has been created successfully.")

    def set_id(self, new_id):
        self.__id = new_id
        print(f"New ID is appointed for {self.role} '{self.name}'")

    def get_salary(self):
        print(f"The salary of {self.role} {self.name} is {self.salary:.2f}")

    def get_info(self):
        info = textwrap.dedent(f"""
        Employee name: {self.name}
        Employee ID: {self.__id}
        Employment Type: {PartTimeEmployee.employment_type}
        Salary Amount: {self.salary:.2f}
        """)
        print(info)

    def give_increment(self):
        self.salary *= 1.05
        print(f"Salary increment is successfully done for '{self.name}'")


