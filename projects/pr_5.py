
class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def get_details(self):
        return f"{self.emp_id} | {self.name} | {self.age} | {self.salary} | Employee"

class Manager(Employee):
    def __init__(self, emp_id, name, age, salary):
        super().__init__(emp_id, name, age, salary)

    def get_details(self):
        return f"{self.emp_id} | {self.name} | {self.age} | {self.salary} | Manager"

class Developer(Employee):
    def __init__(self, emp_id, name, age, salary):
        super().__init__(emp_id, name, age, salary)

    def get_details(self):
        return f"{self.emp_id} | {self.name} | {self.age} | {self.salary} | Developer"

class EmployeeSystem:
    def __init__(self):
        self.emp_list = []

    def add_employee(self, emp):
        self.emp_list.append(emp)
        print("\nEmployee Added!\n")

    def view_all(self):
        if not self.emp_list:
            print("\nNo employees found.\n")
            return
        print("\n---... Employee List ...---")
        for e in self.emp_list:
            print(e.get_details())
        print("---------------------\n")

    def delete_employee(self, emp_id):
        for e in self.emp_list:
            if e.emp_id == emp_id:
                self.emp_list.remove(e)
                print("\nEmployee Deleted!\n")
                return
        print("\nEmployee not found.\n")

def main():
    system = EmployeeSystem()

    while True:
        print("1. Add Manager")
        print("2. Add Developer")
        print("3. View Employees")
        print("4. Delete Employee")
        print("5. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            emp_id = input("Enter ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            salary = input("Enter Salary: ")
            m = Manager(emp_id, name, age, salary)
            system.add_employee(m)

        elif ch == "2":
            emp_id = input("Enter ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            salary = input("Enter Salary: ")
            d = Developer(emp_id, name, age, salary)
            system.add_employee(d)

        elif ch == "3":
            system.view_all()

        elif ch == "4":
            emp_id = input("Enter Employee ID to delete: ")
            system.delete_employee(emp_id)

        elif ch == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.\n")

main()