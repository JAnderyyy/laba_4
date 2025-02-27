#1
class Employee:
  __name = None

  def __init__(self,name):
    self.__name = name
    
emp1 = Employee('john') 
emp2 = Employee('eric') 

print(emp1 == emp2)
#Программа выведет False
#2
print(emp1 == emp1) 
#Программа выведет True
#3
emp1 = Employee('john') 
emp2 = Employee('john') 

print(emp1 == emp2)
#Программа выведет False
#4
emp1 = Employee('john') 
emp2 = Employee('eric') 

print(emp1 != emp1) 
#Программа выведет False
#5
emp1 = Employee('john') 
emp2 = emp1 

print(emp1 == emp2) 
#Программа выведет True
#6
emp1 = Employee('john') 
emp2 = Employee('eric') 

print(emp1 != emp2) 
#Программа выведет True
#7
emp1 = Employee('john') 
emp2 = emp1 
emp2.name = 'eric' 

print(emp1 == emp2)
#Программа выведет True