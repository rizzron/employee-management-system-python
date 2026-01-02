from employee import *
from abc import ABC, abstractmethod


class FullTimeEmployee(Employee, ABC):
    employment_type: str = "Full Time Employee"

    def __init__(self, name: str, id: str, salary: int):
        self.name = name
        self.__id = id
        self.salary = salary

    @abstractmethod
    def set_id(self, new_id):
        pass

    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def give_increment(self):
        pass
