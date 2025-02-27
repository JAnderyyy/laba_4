class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show_name(self):
        print (self.name)
    def show_salary(self):
        print (self.salary)
    def salary_supplement(self):
        print(self.salary * 0.1 + self.salary)
employee1 = Employee('Romanenko', 200)
employee1.show_name()
employee1.show_salary()
employee1.salary_supplement()



