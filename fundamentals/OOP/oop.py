class Employee:

    def __init__(self, first_name, last_name, salary, department, middle_name = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.salary = salary
        self.departmane = department

    def change_salary(self, new_salary):
        if isinstance(new_salary, int):
            if new_salary > 40000:
                self.salary = new_salary

    def full_name(self):
        if self.middle_name != None:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.last_name}"

new_employee = Employee("Adam", "Jones", 48000, "Sales")
new_employee2 = Employee("Brad", "Smith", 68000, "HR")
new_employee3 = Employee("Charlie","Adams",74000,"Engineering", middle_name = "Jacob")

print(new_employee.salary)
new_employee.change_salary(52000)
print(new_employee.salary)
new_employee.change_salary(-40000)
print(new_employee.salary)

employees = [new_employee, new_employee2, new_employee3]

for employee in employees:
    print (employee.full_name())