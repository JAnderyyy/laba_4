class Employee:
    def show(self,name, salary):
        return name + '' + salary

employee = Employee()
employee.show('Романенко', ' 100 тенге зарплата')
print(employee.show('Романенко', ' 100 тенге зарплата'))
