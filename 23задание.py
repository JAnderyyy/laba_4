class User: 
    name = None 
    def __init__(self,name, position, department): 
        self.name = name 
        self.position = position 
        self.department = department 
class Position: 
    def __init__(self,name): 
        self.name = name 
class Department: 
    def __init__(self,name): 
        self.name = name 

PositionEmployee = Position('courier') 
DepartmentEmployee = Department('PizzaFabrica') 
employee = User('Ivan',PositionEmployee,DepartmentEmployee) 

print(employee.name) 
print(employee.position.name) 
print(employee.department.name)
