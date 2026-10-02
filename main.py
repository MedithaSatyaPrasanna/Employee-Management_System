from abc import ABC, abstractmethod


# =========================================================
# EMPLOYEE BASE CLASS
# =========================================================

class Employee(ABC):

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    # Encapsulation
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value
        else:
            raise ValueError("Salary cannot be negative")

    # Abstraction
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def details(self):
        pass


# =========================================================
# DEVELOPER CLASS
# =========================================================

class Developer(Employee):

    def __init__(self, emp_id, name, salary, language):
        super().__init__(emp_id, name, salary)
        self.language = language

    # Polymorphism
    def work(self):
        print("Developer is coding")

    def details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Language:", self.language)


# =========================================================
# MANAGER CLASS
# =========================================================

class Manager(Employee):

    def __init__(self, emp_id, name, salary, team_size):
        super().__init__(emp_id, name, salary)
        self.team_size = team_size

    # Polymorphism
    def work(self):
        print("Manager is managing")

    def details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Team Size:", self.team_size)


# =========================================================
# EMPLOYEE LISTS
# =========================================================

employees = []
developers = []
managers = []


# =========================================================
# ADD EMPLOYEE
# =========================================================

def add_employee(employee):

    # Check duplicate ID
    for emp in employees:
        if emp.emp_id == employee.emp_id:
            print("Employee ID already exists.")
            return False

    employees.append(employee)

    if isinstance(employee, Developer):
        developers.append(employee)

    elif isinstance(employee, Manager):
        managers.append(employee)

    return True


# =========================================================
# DISPLAY EMPLOYEES
# =========================================================

def display():

    if not employees:
        print("\nNo employees found.")
        return

    print("\n========== ALL EMPLOYEES ==========")

    for employee in employees:
        employee.details()
        employee.work()
        print()

    print("========== DEVELOPERS ==========")

    if developers:
        for developer in developers:
            developer.details()
            print()
    else:
        print("No developers found.")

    print("========== MANAGERS ==========")

    if managers:
        for manager in managers:
            manager.details()
            print()
    else:
        print("No managers found.")


# =========================================================
# SEARCH EMPLOYEE BY ID
# =========================================================

def search_employee(emp_id):

    for employee in employees:

        if employee.emp_id == emp_id:
            print("\nEmployee found:")
            employee.details()
            return employee

    print("Employee not found.")
    return None


# =========================================================
# UPDATE SALARY BY ID
# =========================================================

def update_salary(emp_id, value):

    employee = search_employee(emp_id)

    if employee:

        try:
            employee.salary = value
            print("Salary updated successfully.")

        except ValueError as error:
            print(error)


# =========================================================
# REMOVE EMPLOYEE BY ID
# =========================================================

def remove_employee(emp_id):

    for employee in employees:

        if employee.emp_id == emp_id:

            employees.remove(employee)

            if isinstance(employee, Developer):
                developers.remove(employee)

            elif isinstance(employee, Manager):
                managers.remove(employee)

            print("Employee removed successfully.")
            return

    print("Employee not found.")


# =========================================================
# MENU
# =========================================================

def menu():

    while True:

        print("\n================================")
        print("   EMPLOYEE MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee")
        print("4. Update Salary")
        print("5. Remove Employee")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        # =================================================
        # ADD EMPLOYEE
        # =================================================

        if choice == 1:

            print("\n1. Developer")
            print("2. Manager")

            try:
                employee_type = int(input("Choose employee type: "))

            except ValueError:
                print("Please enter 1 or 2.")
                continue

            # -------------------------------------------------
            # Developer
            # -------------------------------------------------

            if employee_type == 1:

                try:
                    emp_id = int(input("Employee ID: "))
                    name = input("Name: ")
                    salary = float(input("Salary: "))
                    language = input("Programming language: ")

                    developer = Developer(
                        emp_id,
                        name,
                        salary,
                        language
                    )

                    if add_employee(developer):
                        print("Developer added successfully.")

                except ValueError as error:
                    print(error)

            # -------------------------------------------------
            # Manager
            # -------------------------------------------------

            elif employee_type == 2:

                try:
                    emp_id = int(input("Employee ID: "))
                    name = input("Name: ")
                    salary = float(input("Salary: "))
                    team_size = int(input("Team size: "))

                    manager = Manager(
                        emp_id,
                        name,
                        salary,
                        team_size
                    )

                    if add_employee(manager):
                        print("Manager added successfully.")

                except ValueError as error:
                    print(error)

            else:
                print("Invalid employee type.")

        # =================================================
        # DISPLAY
        # =================================================

        elif choice == 2:

            display()

        # =================================================
        # SEARCH
        # =================================================

        elif choice == 3:

            try:
                emp_id = int(input("Enter Employee ID: "))
                search_employee(emp_id)

            except ValueError:
                print("Employee ID must be a number.")

        # =================================================
        # UPDATE SALARY
        # =================================================

        elif choice == 4:

            try:
                emp_id = int(input("Enter Employee ID: "))
                new_salary = float(input("Enter new salary: "))

                update_salary(emp_id, new_salary)

            except ValueError:
                print("Please enter valid numbers.")

        # =================================================
        # REMOVE EMPLOYEE
        # =================================================

        elif choice == 5:

            try:
                emp_id = int(input("Enter Employee ID: "))
                remove_employee(emp_id)

            except ValueError:
                print("Employee ID must be a number.")

        # =================================================
        # EXIT
        # =================================================

        elif choice == 6:

            print("\nExiting Employee Management System...")
            break

        else:

            print("Invalid choice. Please try again.")


# =========================================================
# START PROGRAM
# =========================================================

menu()