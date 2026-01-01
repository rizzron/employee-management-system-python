from employee import *

import textwrap


class FullTimeEmployee(Employee):
    employment_type: str = "Full Time Employee"

    def __init__(self, name: str, id: str, salary: int):
        self.name = name
        self.__id = id
        self.salary = salary
        print(f"New Full Time Employee ID for {self.name} has been created successfully.")

    def set_id(self, new_id):
        self.__id = new_id

    def get_info(self):
        info = textwrap.dedent(f"""
        Employee name: {self.name}
        Employee ID: {self.__id}
        Employment Type: {self.employment_type}
        Salary Amount: {self.salary}
        """)
        print(info)
