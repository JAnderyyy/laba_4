class Student:
    name = 'иван'
    surname = 'романенков'
    def show(self):
        print(self.name.upper())
        print(self.surname.lower())
    
        
student = Student()
student.show()
