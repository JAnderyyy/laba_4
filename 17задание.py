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
    def setName(self, name):
            self.__name = name
    def setSalary(self, salary):
            self.__salary = salary
    def setAge(self, age):
            self.__age = age        
employee1 = Employee('', '', '')
employee1.setName('Romanenko')
employee1.setSalary(200)
employee1.setAge(17)
print(employee1.getName())
print(employee1.getSalary())
print(employee1.getAge())



