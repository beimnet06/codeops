
print("=" * 60)
print("TASK 7: FULL BANK ACCOUNT WITH PROPERTIES")
print("=" * 60)

class BankAccount:
    
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance  # Private attribute
        self.transaction_history = []
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = amount
    
    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be positive!")
            return False
        
        self.__balance += amount
        self.transaction_history.append(f"Deposit: +${amount:.2f}")
        print(f"✅ Deposited ${amount:.2f}")
        print(f"💰 New balance: ${self.__balance:.2f}")
        return True
    
    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
            return False
        
        if amount > self.__balance:
            print(f"❌ Insufficient funds! You have ${self.__balance:.2f}")
            return False
        
        self.__balance -= amount
        self.transaction_history.append(f"Withdrawal: -${amount:.2f}")
        print(f"✅ Withdrew ${amount:.2f}")
        print(f"💰 New balance: ${self.__balance:.2f}")
        return True
    
    def transfer(self, to_account, amount):
        if not isinstance(to_account, BankAccount):
            print("❌ Invalid target account!")
            return False
        
        if amount <= 0:
            print("❌ Transfer amount must be positive!")
            return False
        
        if amount > self.__balance:
            print(f"❌ Insufficient funds! You have ${self.__balance:.2f}")
            return False
        
        self.__balance -= amount
        to_account.deposit(amount)
        self.transaction_history.append(f"Transfer to {to_account.owner}: -${amount:.2f}")
        print(f"✅ Transferred ${amount:.2f} to {to_account.owner}")
        print(f"💰 Your new balance: ${self.__balance:.2f}")
        return True
    
    def show_transactions(self):
        if not self.transaction_history:
            print("📭 No transactions yet.")
            return
        
        print("\n📋 Transaction History:")
        print("-" * 40)
        for transaction in self.transaction_history:
            print(f"  {transaction}")
        print("-" * 40)

print("\n--- Creating Accounts ---")
account1 = BankAccount("Beimnet Tariku", "ACC001", 1000)
account2 = BankAccount("Abel Kebede", "ACC002", 500)

print(f"Account 1: {account1.owner} (Balance: ${account1.balance:.2f})")
print(f"Account 2: {account2.owner} (Balance: ${account2.balance:.2f})")

print("\n--- Testing Deposits ---")
account1.deposit(500)

print("\n--- Testing Withdrawals ---")
account1.withdraw(200)

print("\n--- Testing Transfers ---")
account1.transfer(account2, 300)

print("\n--- Testing Overdraw ---")
account1.withdraw(2000)

print("\n--- Transaction History ---")
account1.show_transactions()

print("\n" + "=" * 60)
print("TASK 8: LIBRARY SYSTEM")
print("=" * 60)

class Book:
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True  # Private attribute
    
    @property
    def available(self):
        return self.__available
    
    def borrow(self):
        if self.__available:
            self.__available = False
            print(f"📖 '{self.title}' borrowed successfully!")
            return True
        else:
            print(f"❌ '{self.title}' is currently unavailable.")
            return False
    
    def return_book(self):
        if not self.__available:
            self.__available = True
            print(f"📚 '{self.title}' returned successfully!")
            return True
        else:
            print(f"⚠️ '{self.title}' was not borrowed.")
            return False
    
    def __str__(self):
        status = "Available" if self.__available else "Borrowed"
        return f"{self.title} by {self.author} ({self.isbn}) - {status}"

class Library:
    
    def __init__(self, name):
        self.name = name
        self.__books = []  # Private list of books
    
    def add_book(self, book):
        if isinstance(book, Book):
            self.__books.append(book)
            print(f"✅ '{book.title}' added to library!")
        else:
            print("❌ Invalid book object!")
    
    def borrow_book(self, isbn):
        for book in self.__books:
            if book.isbn == isbn:
                return book.borrow()
        print(f"❌ Book with ISBN {isbn} not found!")
        return False
    
    def return_book(self, isbn):
        for book in self.__books:
            if book.isbn == isbn:
                return book.return_book()
        print(f"❌ Book with ISBN {isbn} not found!")
        return False
    
    def search_by_title(self, title):
        found = [book for book in self.__books if title.lower() in book.title.lower()]
        if found:
            print(f"\n📚 Found {len(found)} book(s):")
            for book in found:
                print(f"  {book}")
        else:
            print(f"❌ No books found with title '{title}'")
        return found
    
    def show_all_books(self):
        if not self.__books:
            print("📭 Library is empty!")
            return
        
        print(f"\n📚 {self.name} - Book Collection")
        print("-" * 50)
        for book in self.__books:
            print(f"  {book}")
        print("-" * 50)
        print(f"Total books: {len(self.__books)}")

print("\n--- Creating Books ---")
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4")
book3 = Book("1984", "George Orwell", "978-0-452-28423-4")

print("--- Creating Library ---")
library = Library("Addis Ababa Public Library")

print("\n--- Adding Books ---")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("\n--- Displaying All Books ---")
library.show_all_books()

print("\n--- Borrowing Books ---")
library.borrow_book("978-0-7432-7356-5")

print("\n--- Trying to Borrow Unavailable Book ---")
library.borrow_book("978-0-7432-7356-5")

print("\n--- Returning Books ---")
library.return_book("978-0-7432-7356-5")

print("\n--- Searching Books ---")
library.search_by_title("1984")

print("\n" + "=" * 60)
print("TASK 9: CAR CLASS WITH ENCAPSULATION")
print("=" * 60)

class Car:
    
    def __init__(self, make, model, speed=0, fuel=100):
        self.make = make
        self.model = model
        self.__speed = speed  # Private attribute (km/h)
        self.__fuel = fuel    # Private attribute (percentage)
    
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Speed cannot be negative!")
        if value > 240:
            print("⚠️ Speed limit exceeded! Max speed is 240 km/h")
            self.__speed = 240
        else:
            self.__speed = value
    
    @property
    def fuel(self):
        return self.__fuel
    
    @fuel.setter
    def fuel(self, value):
        if value < 0:
            self.__fuel = 0
        elif value > 100:
            self.__fuel = 100
        else:
            self.__fuel = value
    
    def accelerate(self, amount=10):
        if self.__fuel <= 0:
            print("❌ No fuel! Please refuel.")
            return
        
        fuel_consumption = amount * 0.5  # 0.5% fuel per 10 km/h
        if self.__fuel >= fuel_consumption:
            self.speed += amount  # Uses the setter
            self.__fuel -= fuel_consumption
            print(f"🚗 Accelerated to {self.__speed} km/h")
            print(f"⛽ Fuel: {self.__fuel:.1f}%")
        else:
            print("❌ Not enough fuel to accelerate!")
    
    def brake(self, amount=10):
        if self.__speed == 0:
            print("🚗 Car is already stopped.")
            return
        
        self.__speed = max(0, self.__speed - amount)
        print(f"🚗 Braked to {self.__speed} km/h")
    
    def refuel(self, amount):
        if amount <= 0:
            print("❌ Refuel amount must be positive!")
            return
        
        self.fuel += amount  # Uses the setter
        print(f"⛽ Refueled {amount}%")
        print(f"⛽ Current fuel: {self.__fuel}%")
    
    def status(self):
        print(f"\n🚗 {self.make} {self.model}")
        print(f"   Speed: {self.__speed} km/h")
        print(f"   Fuel: {self.__fuel:.1f}%")

print("\n--- Creating Car ---")
my_car = Car("Toyota", "Camry")

my_car.status()

print("\n--- Accelerating ---")
my_car.accelerate(30)
my_car.accelerate(40)

print("\n--- Braking ---")
my_car.brake(20)

print("\n--- Refueling ---")
my_car.refuel(20)

print("\n--- Trying to drive without fuel ---")
my_car.accelerate(100)  # Will reduce fuel significantly

print("\n--- Final Status ---")
my_car.status()

print("\n" + "=" * 60)
print("LEVEL 3 COMPLETE! 🎉")
print("=" * 60)
