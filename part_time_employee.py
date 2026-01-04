from employee import *
from abc import ABC, abstractmethod


class PartTimeEmployee(Employee):
    employment_type: str = "Part Time Employee"

    def __init__(self, name: str, salary: int):
        super().__init__(name)
        self.salary = salary

    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def give_increment(self):
        pass