# list comprehension
class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary


class Company(Employee):
    def __init__(self, company):
        self.company = company
        self.emp_dict = {}
        super().__init__("name", "department", "salary")

    def add_employee(self, employee):
        self.emp_dict.update({employee.name: employee})

    def display_employee(self, employee):
        new_dict = {employee.name: [name, dept, salary] for name in self.emp_dict}
        print(new_dict)

    def update_employee(self, name, dept, salary):
        if not name in self.emp_dict:
            return

        employee = Employee(name=name, department=dept, salary=salary)
        self.emp_dict.update({employee.name: employee})


if __name__ == '__main__':
    company = Company("tata")
    name = input("enter name: ")
    dept = input("dept: ")
    salary = input("salary: ")
    employee = Employee(name, dept, salary)
    company.add_employee(employee)
    company.display_employee(employee)
    name = input("enter name: ")
    dept = input("dept: ")
    salary = input("salary: ")
    company.update_employee(name, dept, salary)
    company.display_employee(employee)
