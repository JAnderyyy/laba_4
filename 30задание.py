class User:
    def __init__(self, first_name="", last_name="", salary=0):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

class Employee(User):
    def __init__(self, first_name="", last_name="",salary=0):
        super().__init__(first_name, last_name, salary)
    def set_first_name(self, first_name):
        self.first_name = first_name
    def get_first_name(self):
        return self.first_name
    def set_last_name(self, last_name):
        self.last_name = last_name
    def get_last_name(self):
        return self.last_name
    def set_salary(self, salary):
        return self.salary
    def get_salary(self):
        return self.salary

employee = Employee("Лев","Белавин",120000)
first_name = employee.get_first_name()
last_name = employee.get_last_name()
salary = employee.get_salary()
print(first_name)
print(last_name)
print(salary)