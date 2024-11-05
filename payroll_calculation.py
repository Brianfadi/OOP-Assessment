class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_payroll(self):
        return sum(employee.salary for employee in self.employees)

emp1 = Employee("Alice", 5000)
emp2 = Employee("Bob", 7000)

payroll = Payroll()
payroll.add_employee(emp1)
payroll.add_employee(emp2)
print("Total Payroll:", payroll.total_payroll())
