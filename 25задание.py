class Employe:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"Имя: {self.name}, Зарплата: {self.salary}"

class EmployeeCollection:
    def __init__(self):
        self.employees = []
    def add_employee(self, name, salary):
        new_employee = Employe(name, salary)
        self.employees.append(new_employee)
    def all_employee(self):
        if not self.employees:
            print('Список пуст')
        else:
            for employee in self.employees:
                print(employee)
    def total_salary(self):
        total_salary = sum(employee.salary for employee in self.employees)
        return total_salary
    def average_salary(self):
        if not self.employees:
            return 0
        total_salary = self.total_salary()
        average_salary = total_salary / len(self.employees)
        return average_salary
        
employe = EmployeeCollection()
employe.add_employee('Белавин', 21111)
employe.add_employee('Романов', 42200)
employe.all_employee()  # Вызываем all_employee без print, так как он сам печатает
total_salary = employe.total_salary()
print(total_salary)
average_salary = employe.average_salary()  # Вызываем average_salary как метод с круглыми скобками
print(average_salary)