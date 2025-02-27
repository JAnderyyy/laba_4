class Employee:
    first_name = None
    last_name = None
    employee_job = None
    pass

employee = Employee()

employee.first_name = 'Иван'
employee.last_name = 'Романов'
employee.employee_job = 'Разноробочий'

employee1 = (employee.first_name, employee.last_name, employee.employee_job)

print(employee1)

