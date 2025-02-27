class Employee:
    __name = None
    __salary = None
    __age = None
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def getAge(self):
        return self.__age
employee1 = Employee('Romanenko', 200, 17)
print(employee1.getName())
print(employee1.getSalary())
print(employee1.getAge())



