class Employee:
    __age = None
    __name = None
    __salary = None
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
    def show(self):
        print (self.name)
        print (self.salary)
        print (self.age)
employee1 = Employee('Romanenko', 200, 17)
employee1.show()



