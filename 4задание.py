class Employee:
    name = None
    last_name = None
    employee_job = None
    age = None 
    salary = None
    pass

employee1 = Employee()
employee2 = Employee()

employee1.name = 'Иван'
employee2.name = 'Илья'
employee1.salary = 5000
employee2.salary = 100

salary1 = employee1.salary
salary2 = employee2.salary

salary = salary1 + salary2

print(salary)

