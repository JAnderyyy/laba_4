class Employee:
    name = None
    last_name = None
    employee_job = None
    age = None 
    salary = None
    pass

employee = Employee()

employee.name = 'Иван'
employee.last_name = 'Романов'
employee.employee_job = 'Разноробочий'
employee.age = '17'
employee.salary = '5000'

employee1 = (employee.name, employee.last_name, employee.employee_job)

print(employee.name)
print(employee.age)
print(employee.salary)

