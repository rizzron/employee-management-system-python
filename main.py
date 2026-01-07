from manager import *
from annotator import *
from employee_management_system import *



rizz = Manager("Rizvy Kamal", 3000)
rizz.get_info()
rizz.give_increment()
rizz.get_salary()

fizz = Annotator("Mustafizur Rahman", 1500)
fizz.get_info()
fizz.give_increment()
fizz.get_salary()

ems = EMS()
ems.add_employee(rizz)
ems.add_employee(fizz)
ems.get_employee_details_by_name("Rizvy Kamal")
ems.get_employee_details_by_id(2)

ems.get_all_employee()
ems.get_employee_by_role("Manager")
ems.get_employee_by_role("Annotator")
ems.get_employee_by_salary(1000, 5000)
