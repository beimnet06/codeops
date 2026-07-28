
print("=" * 60)
print("TASK 1: SINGLE RESPONSIBILITY PRINCIPLE (SRP)")
print("=" * 60)

class BadEmployee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def calculate_bonus(self):
        return self.salary * 0.10
    
    def save_to_file(self):
        with open('employee.txt', 'w') as f:
            f.write(f"{self.name},{self.salary}")
        print("Saved to file")
    
    def send_email(self):
        print(f"Sending email to {self.name}")
        print("Email sent!")
    
    def show_info(self):
        print(f"Employee: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Bonus: ${self.calculate_bonus()}")

print("\n--- Bad Design (Violates SRP) ---")
bad_emp = BadEmployee("John Doe", 5000)
bad_emp.show_info()
bad_emp.save_to_file()
bad_emp.send_email()

print("\n" + "=" * 40)
print("--- Good Design (Follows SRP) ---")


class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.salary

class SalaryCalculator:
    
    @staticmethod
    def calculate_bonus(employee):
        return employee.get_salary() * 0.10
    
    @staticmethod
    def calculate_annual_salary(employee):
        return employee.get_salary() * 12

class EmployeeFileManager:
    
    @staticmethod
    def save_to_file(employee, filename="employee.txt"):
        with open(filename, 'w') as f:
            f.write(f"{employee.get_name()},{employee.get_salary()}")
        print(f"✅ Saved {employee.get_name()} to {filename}")
    
    @staticmethod
    def load_from_file(filename="employee.txt"):
        try:
            with open(filename, 'r') as f:
                data = f.read().split(',')
                return Employee(data[0], float(data[1]))
        except FileNotFoundError:
            print("File not found!")
            return None

class EmailNotifier:
    
    @staticmethod
    def send_email(employee, subject="Welcome to the Company!"):
        print(f"📧 Sending email to {employee.get_name()}...")
        print(f"   Subject: {subject}")
        print("   Message: Hello and welcome!")
        print("✅ Email sent successfully!")

print("\n--- Creating Employee ---")
emp = Employee("Jane Smith", 6000)
print(f"Employee: {emp.get_name()}")
print(f"Salary: ${emp.get_salary()}")

print("\n--- Calculating Bonus ---")
bonus = SalaryCalculator.calculate_bonus(emp)
print(f"Bonus: ${bonus}")
annual = SalaryCalculator.calculate_annual_salary(emp)
print(f"Annual Salary: ${annual}")

print("\n--- Saving to File ---")
EmployeeFileManager.save_to_file(emp)

print("\n--- Sending Email ---")
EmailNotifier.send_email(emp)

print("\n" + "=" * 60)
print("TASK 2: OPEN/CLOSED PRINCIPLE (OCP)")
print("=" * 60)

print("\n--- Bad Design (Violates OCP) ---")

def calculate_bonus_bad(employee_type, salary):
    if employee_type == "developer":
        return salary * 0.15
    elif employee_type == "manager":
        return salary * 0.20
    elif employee_type == "intern":
        return salary * 0.05
    else:
        return 0

print(f"Developer bonus: ${calculate_bonus_bad('developer', 5000)}")
print(f"Manager bonus: ${calculate_bonus_bad('manager', 7000)}")
print(f"Intern bonus: ${calculate_bonus_bad('intern', 2000)}")

print("\n--- Good Design (Follows OCP) ---")


class EmployeeType:
    
    def get_bonus_percentage(self):
        raise NotImplementedError("Subclasses must implement this method")

class Developer(EmployeeType):
    def get_bonus_percentage(self):
        return 0.15

class Manager(EmployeeType):
    def get_bonus_percentage(self):
        return 0.20

class Intern(EmployeeType):
    def get_bonus_percentage(self):
        return 0.05

class SeniorDeveloper(EmployeeType):
    def get_bonus_percentage(self):
        return 0.25

def calculate_bonus(employee_type, salary):
    return salary * employee_type.get_bonus_percentage()

print("--- Testing OCP Design ---")
dev = Developer()
mgr = Manager()
intern = Intern()
senior = SeniorDeveloper()  # New type

print(f"Developer bonus: ${calculate_bonus(dev, 5000)}")
print(f"Manager bonus: ${calculate_bonus(mgr, 7000)}")
print(f"Intern bonus: ${calculate_bonus(intern, 2000)}")
print(f"Senior Developer bonus: ${calculate_bonus(senior, 10000)}")

print("\n" + "=" * 60)
print("TASK 3: LISKOV SUBSTITUTION PRINCIPLE (LSP)")
print("=" * 60)

print("\n--- Bad Design (Violates LSP) ---")

class Bird:
    def fly(self):
        print("Flying...")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")

def make_bird_fly(bird):
    bird.fly()

print("Making a bird fly:")
make_bird_fly(Bird())

print("Making a penguin fly:")
try:
    make_bird_fly(Penguin())
except Exception as e:
    print(f"❌ Error: {e}")

print("\n--- Good Design (Follows LSP) ---")


class Bird:
    def eat(self):
        print("Eating...")
    
    def sleep(self):
        print("Sleeping...")

class FlyingBird(Bird):
    def fly(self):
        print("Flying...")

class WalkingBird(Bird):
    def walk(self):
        print("Walking...")

class Sparrow(FlyingBird):
    pass

class Penguin(WalkingBird):
    pass

class Duck(FlyingBird):
    pass

def make_bird_fly_lsp(bird):
    if isinstance(bird, FlyingBird):
        bird.fly()
    else:
        print(f"⚠️ {bird.__class__.__name__} is a walking bird and can't fly!")

print("--- Testing LSP Design ---")
sparrow = Sparrow()
penguin = Penguin()
duck = Duck()

print("\nSparrow:")
sparrow.eat()
make_bird_fly_lsp(sparrow)

print("\nPenguin:")
penguin.eat()
penguin.walk()
make_bird_fly_lsp(penguin)

print("\nDuck:")
duck.eat()
make_bird_fly_lsp(duck)

print("\n" + "=" * 60)
print("TASK 4: IDENTIFY SOLID VIOLATIONS")
print("=" * 60)

print("""
🔍 SOLID Violation Analysis:

class Account:
    def __init__(self):
        self.notifier = EmailNotifier()
        ...
    def withdraw(self, amount):
        ...
        self.notifier.send_email(...)
        self.save_to_db(...)

❌ Violations:
1. Single Responsibility Principle (SRP) - Account class:
   - Manages balance AND sends emails AND saves to database
   - Should only handle account logic

2. Dependency Inversion Principle (DIP) - Account class:
   - Depends directly on concrete EmailNotifier
   - Should depend on an abstraction (interface) for notification

3. Interface Segregation Principle (ISP) - Account class:
   - Forced to depend on methods it doesn't need
   - Email and DB operations should be separate

💡 Fix: Create separate classes for:
   - Account (balance, deposit, withdraw)
   - Notifier (email, SMS, etc.)
   - Repository (save, load from DB)
   - Inject dependencies through constructor

print("\n" + "=" * 60)
print("BASIC EXERCISES COMPLETE! 🎉")
print("=" * 60)
