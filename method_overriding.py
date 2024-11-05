class Employee:
    def calculate_salary(self):
        print("Calculating salary for employee.")

class Manager(Employee):
    def calculate_salary(self):
        print("Calculating salary for manager.")

emp = Employee()
mgr = Manager()
emp.calculate_salary()
mgr.calculate_salary()
