class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
    
employee = [
    Employee('Ivan',4500),
    Employee('Anton',6500),
    Employee('Misha',1050),
    Employee('Nikitos',4550),
    ]
for employees in employee:
    print(employees.name)
    print(employees.salary)