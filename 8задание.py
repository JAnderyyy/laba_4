class Student:
    def show(self):
        return self.upper_text(self.name)
    def upper_text(self, stri):
        return stri.title()
        
student = Student()
student.name = 'иван'
student.surname = 'романенков'
student.show()
print(student.upper_text(student.name))
print(student.upper_text(student.surname))
print(student.upper_text(student.name[0])+student.upper_text(student.surname[0]))