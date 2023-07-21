import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

with open("C:/Users/Asif Qayom/Desktop/employee.json") as file:
    data = json.load(file)

employee_list = []
for employee_data in data["employees"]:
    name = employee_data["Name"]
    dob = employee_data["DOB"]
    height = employee_data["Height"]
    city = employee_data["City"]
    state = employee_data["State"]
    employee = Employee(name, dob, height, city, state)
    employee_list.append(employee)

for employee in employee_list:
    print("Name:", employee.name)
    print("DOB:",employee.dob)
    print("Height:",employee.height)
    print("City:",employee.city)
    print("State:",employee.state)
    print()