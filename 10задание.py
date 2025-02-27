class Employee:
    name = 'Romanenko'
    def __init__(self):
        print(self.name.upper())
        
employees = Employee()
employees.__init__()

