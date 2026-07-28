
print("=" * 60)
print("TASK 1: SIMPLE CLASS - PERSON")
print("=" * 60)

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"👋 Hello! My name is {self.name} and I am {self.age} years old.")

print("\n--- Creating Person Objects ---")
person1 = Person("Beimnet Tariku", 22)
person2 = Person("Abel Kebede", 25)

print("\n--- Introductions ---")
person1.introduce()
person2.introduce()

print("\n" + "=" * 60)
print("TASK 2: RECTANGLE CLASS")
print("=" * 60)

class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

print("\n--- Creating Rectangle Objects ---")
rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)

print("\n--- Rectangle 1 (10 x 5) ---")
print(f"Area: {rect1.area()}")
print(f"Perimeter: {rect1.perimeter()}")

print("\n--- Rectangle 2 (7 x 3) ---")
print(f"Area: {rect2.area()}")
print(f"Perimeter: {rect2.perimeter()}")

print("\n" + "=" * 60)
print("TASK 3: BANK ACCOUNT (BASIC)")
print("=" * 60)

class Account:
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ${amount:.2f}")
            print(f"💰 New balance: ${self.balance:.2f}")
        else:
            print("❌ Deposit amount must be positive!")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"✅ Withdrew ${amount:.2f}")
                print(f"💰 New balance: ${self.balance:.2f}")
            else:
                print(f"❌ Insufficient balance! You have ${self.balance:.2f}")
        else:
            print("❌ Withdrawal amount must be positive!")

print("\n--- Creating Account ---")
my_account = Account("Beimnet Tariku", 1000)
print(f"Account owner: {my_account.owner}")
print(f"Initial balance: ${my_account.balance:.2f}")

print("\n--- Testing Deposits ---")
my_account.deposit(500)

print("\n--- Testing Withdrawals ---")
my_account.withdraw(200)

print("\n--- Testing Overdraw ---")
my_account.withdraw(2000)

print("\n" + "=" * 60)
print("LEVEL 1 COMPLETE! 🎉")
print("=" * 60)
