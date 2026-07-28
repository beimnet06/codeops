
print("=" * 60)
print("TASK 1: SIMPLE INHERITANCE")
print("=" * 60)

class Vehicle:
    
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
    
    def info(self):
        print(f"🚗 Vehicle: {self.name} {self.model}")
        print(f"   Year: {self.year}")

class Car(Vehicle):
    
    def __init__(self, name, model, year, doors):
        super().__init__(name, model, year)  # Call parent constructor
        self.doors = doors
    
    def honk(self):
        print(f"📯 {self.name} says: Beep beep!")

class Motorcycle(Vehicle):
    
    def __init__(self, name, model, year, type):
        super().__init__(name, model, year)
        self.type = type  # e.g., Sport, Cruiser, Off-road
    
    def wheelie(self):
        print(f"🏍️ {self.name} is doing a wheelie!")

print("\n--- Creating Car ---")
my_car = Car("Toyota", "Camry", 2022, 4)
my_car.info()
print(f"   Doors: {my_car.doors}")
my_car.honk()

print("\n--- Creating Motorcycle ---")
my_bike = Motorcycle("Harley-Davidson", "Sportster", 2023, "Cruiser")
my_bike.info()
print(f"   Type: {my_bike.type}")
my_bike.wheelie()

print("\n" + "=" * 60)
print("TASK 2: SAVINGSACCOUNT INHERITANCE")
print("=" * 60)

class Account:
    
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance
        self.transaction_history = []
    
    @property
    def balance(self):
        return self.__balance
    
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
    
    def statement(self):
        print("\n" + "=" * 50)
        print("📋 ACCOUNT STATEMENT")
        print("=" * 50)
        print(f"👤 Owner: {self.owner}")
        print(f"🔢 Account: {self.account_number}")
        print(f"💰 Balance: ${self.__balance:.2f}")
        print("=" * 50)

class SavingsAccount(Account):
    
    def __init__(self, owner, account_number, balance=0, interest_rate=0.05):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate  # 5% default
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"📈 Added interest: ${interest:.2f} (Rate: {self.interest_rate * 100}%)")
        print(f"💰 New balance: ${self.balance:.2f}")

print("\n--- Creating Savings Account ---")
savings = SavingsAccount("Beimnet Tariku", "SAV001", 1000, 0.05)
print(f"Account: {savings.account_number}")
print(f"Owner: {savings.owner}")
print(f"Balance: ${savings.balance:.2f}")
print(f"Interest Rate: {savings.interest_rate * 100}%")

print("\n--- Adding Interest ---")
savings.add_interest()

print("\n" + "=" * 60)
print("TASK 3: CURRENTACCOUNT INHERITANCE")
print("=" * 60)

class CurrentAccount(Account):
    
    def __init__(self, owner, account_number, balance=0, overdraft_limit=500):
        super().__init__(owner, account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
            return False
        
        if amount <= self.balance + self.overdraft_limit:
            self._Account__balance -= amount  # Access private balance
            self.transaction_history.append(f"Withdrawal: -${amount:.2f}")
            print(f"✅ Withdrew ${amount:.2f}")
            
            if self.balance < 0:
                print(f"⚠️ Overdraft used! Current balance: ${self.balance:.2f}")
                print(f"📊 Overdraft remaining: ${self.overdraft_limit + self.balance:.2f}")
            else:
                print(f"💰 New balance: ${self.balance:.2f}")
            return True
        else:
            print(f"❌ Overdraft limit exceeded!")
            print(f"💰 Available funds: ${self.balance:.2f} + ${self.overdraft_limit:.2f} overdraft")
            return False

print("\n--- Creating Current Account ---")
current = CurrentAccount("Abel Kebede", "CUR001", 500, 1000)
print(f"Account: {current.account_number}")
print(f"Owner: {current.owner}")
print(f"Balance: ${current.balance:.2f}")
print(f"Overdraft Limit: ${current.overdraft_limit:.2f}")

print("\n--- Testing Withdrawal (Within balance) ---")
current.withdraw(200)

print("\n--- Testing Withdrawal (With overdraft) ---")
current.withdraw(1200)  # This will use overdraft

print("\n--- Testing Withdrawal (Exceeding overdraft) ---")
current.withdraw(500)  # This should fail

print("\n" + "=" * 60)
print("🎉 LEVEL 1 COMPLETE!")
print("=" * 60)
