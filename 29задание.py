class User:
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name

class Employee(User):
    pass

employe = Employee()
employe.set_name('Nikitos')
name = employe.get_name()
print(name)