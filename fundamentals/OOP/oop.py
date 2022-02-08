class Employee:

    def __init__(self, first_name, last_name, salary, department):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.departmane = department

    def change_salary(self, new_salary):
        if isinstance(new_salary, int):
            if new_salary > 40000:
                self.salary = new_salary


new_employee = Employee("Adam", "Jones", 48000, "Sales")
new_employee2 = Employee("Brad", "Smith", 68000, "HR")

print(new_employee.salary)
new_employee.change_salary(52000)
print(new_employee.salary)
new_employee.change_salary(-40000)
print(new_employee.salary)
