
print("=" * 60)
print("TASK 4: STUDENT CLASS")
print("=" * 60)

class Student:
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []  # Empty list to store grades
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"✅ Added grade: {grade}")
        else:
            print("❌ Invalid grade! Must be between 0 and 100.")
    
    def average_grade(self):
        if len(self.grades) == 0:
            print("⚠️ No grades available!")
            return 0
        
        total = sum(self.grades)
        average = total / len(self.grades)
        return average

print("\n--- Creating Student ---")
student1 = Student("Beimnet Tariku", "S12345")
print(f"Student: {student1.name}")
print(f"ID: {student1.student_id}")

print("\n--- Adding Grades ---")
student1.add_grade(95)
student1.add_grade(85)
student1.add_grade(78)
student1.add_grade(92)

print("\n--- Grade Summary ---")
print(f"Grades: {student1.grades}")
print(f"Average: {student1.average_grade():.2f}")

print("\n" + "=" * 60)
print("TASK 5: PRODUCT CLASS")
print("=" * 60)

class Product:
    
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def sell(self, quantity):
        if quantity <= 0:
            print("❌ Quantity must be positive!")
            return
        
        if quantity <= self.stock:
            self.stock -= quantity
            total_price = quantity * self.price
            print(f"✅ Sold {quantity} {self.name}(s)")
            print(f"💰 Total: ${total_price:.2f}")
            print(f"📦 Remaining stock: {self.stock}")
        else:
            print(f"❌ Not enough stock! Only {self.stock} available.")
    
    def restock(self, quantity):
        if quantity <= 0:
            print("❌ Quantity must be positive!")
            return
        
        self.stock += quantity
        print(f"✅ Restocked {quantity} {self.name}(s)")
        print(f"📦 New stock: {self.stock}")

print("\n--- Creating Product ---")
product1 = Product("Injera", 50.00, 100)
print(f"Product: {product1.name}")
print(f"Price: ${product1.price:.2f}")
print(f"Stock: {product1.stock}")

print("\n--- Selling Product ---")
product1.sell(10)

print("\n--- Restocking Product ---")
product1.restock(25)

print("\n--- Trying to sell more than available ---")
product1.sell(200)

print("\n" + "=" * 60)
print("TASK 6: ENCAPSULATION PRACTICE")
print("=" * 60)

class Account:
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited ${amount:.2f}")
            print(f"💰 New balance: ${self.__balance:.2f}")
        else:
            print("❌ Deposit amount must be positive!")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
            return
        
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Withdrew ${amount:.2f}")
            print(f"💰 New balance: ${self.__balance:.2f}")
        else:
            print(f"❌ Insufficient funds! You have ${self.__balance:.2f}")

print("\n--- Creating Improved Account ---")
my_account = Account("Beimnet Tariku", 1000)
print(f"Owner: {my_account.owner}")

print(f"\n--- Using Getter ---")
print(f"💰 Balance: ${my_account.balance:.2f}")

print("\n--- Testing Valid Deposits ---")
my_account.deposit(500)

print("\n--- Testing Invalid Deposit ---")
my_account.deposit(-100)

print("\n--- Testing Valid Withdrawal ---")
my_account.withdraw(300)

print("\n--- Testing Overdraw ---")
my_account.withdraw(2000)

print("\n" + "=" * 60)
print("LEVEL 2 COMPLETE! 🎉")
print("=" * 60)
