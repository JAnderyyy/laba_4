class Employee:
    name = None
    salary = None
    def show_name(self):
        print(self.name)

    def show_salary(self):
        print(self.salary)

employee = Employee()
employee.name = 'Романенко'
employee.salary = '100 тенге'
employee.show_name()
employee.show_salary()


