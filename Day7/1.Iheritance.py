# Base class 1
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, my name is {self.name}."
# Base class 2
class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id
    def get_id(self):
        return f"My employee ID is {self.employee_id}."
# Derived class inheriting from both Person and Employee
class Manager(Person, Employee):
    def __init__(self, name, employee_id, department):
        Person.__init__(self, name)  # Initialize Person part
        Employee.__init__(self, employee_id)  # Initialize Employee part
        self.department = department
    def show_details(self):
        return f"{self.greet()} {self.get_id()} I manage the {self.department} department."

# Create an instance of the derived class
manager = Manager("Alice", "E12345", "Sales")

# Call methods from base classes and derived class
print(manager.greet())         # Output: Hello, my name is Alice.
print(manager.get_id())        # Output: My employee ID is E12345.
print(manager.show_details())  # Output: Hello, my name is Alice. My employee ID is E12345. I manage the Sales department.

#using super()
# Base class 1
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, my name is {self.name}."

class Employee(Person):#inheriting person to employee
    def __init__(self, name, employee_id):
        super().__init__(name)#initializing base class with name
        self.employee_id = employee_id
    def get_id(self):
        return f"My employee ID is {self.employee_id}."
# Derived class inheriting from both Person and Employee
class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name,employee_id)      #iniatialize the base class (Person)
        self.department = department
    def show_details(self):
        return f"{self.greet()} {self.get_id()} I manage the {self.department} department."

# Create an instance of the derived class
manager = Manager("Alice", "E12345", "Sales")

# Call methods from base classes and derived class
print(manager.greet())         # Output: Hello, my name is Alice.
print(manager.get_id())        # Output: My employee ID is E12345.
print(manager.show_details())  # Output: Hello, my name is Alice. My employee ID is E12345. I manage the Sales department.