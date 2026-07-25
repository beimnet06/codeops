# ============================================
# Day 5 - Level 2: Intermediate
# ============================================

print("=" * 60)
print("TASK 4: METHOD OVERRIDING")
print("=" * 60)

# First, let's recreate the classes from Level 1
class Account:
    """Base Account class"""
    
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
        """Display account statement"""
        print("\n" + "=" * 50)
        print("📋 ACCOUNT STATEMENT")
        print("=" * 50)
        print(f"👤 Owner: {self.owner}")
        print(f"🔢 Account: {self.account_number}")
        print(f"💰 Balance: ${self.__balance:.2f}")
        print("=" * 50)

class SavingsAccount(Account):
    """SavingsAccount with interest rate"""
    
    def __init__(self, owner, account_number, balance=0, interest_rate=0.05):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        """Add interest to the balance"""
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"📈 Added interest: ${interest:.2f} (Rate: {self.interest_rate * 100}%)")
    
    # Override statement() to show interest rate
    def statement(self):
        """Override statement to show interest rate"""
        print("\n" + "=" * 50)
        print("📋 SAVINGS ACCOUNT STATEMENT")
        print("=" * 50)
        print(f"👤 Owner: {self.owner}")
        print(f"🔢 Account: {self.account_number}")
        print(f"💰 Balance: ${self.balance:.2f}")
        print(f"📊 Interest Rate: {self.interest_rate * 100}%")
        print("=" * 50)

class CurrentAccount(Account):
    """CurrentAccount with overdraft facility"""
    
    def __init__(self, owner, account_number, balance=0, overdraft_limit=500):
        super().__init__(owner, account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        """Override withdraw to allow overdraft"""
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
            return False
        
        if amount <= self.balance + self.overdraft_limit:
            self._Account__balance -= amount
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
            return False
    
    # Override statement() to show overdraft info
    def statement(self):
        """Override statement to show overdraft information"""
        print("\n" + "=" * 50)
        print("📋 CURRENT ACCOUNT STATEMENT")
        print("=" * 50)
        print(f"👤 Owner: {self.owner}")
        print(f"🔢 Account: {self.account_number}")
        print(f"💰 Balance: ${self.balance:.2f}")
        print(f"🏦 Overdraft Limit: ${self.overdraft_limit:.2f}")
        if self.balance < 0:
            print(f"⚠️ Overdraft used: ${abs(self.balance):.2f}")
            print(f"📊 Remaining overdraft: ${self.overdraft_limit + self.balance:.2f}")
        else:
            print(f"💚 Overdraft available: ${self.overdraft_limit:.2f}")
        print("=" * 50)

# 4. Method Overriding
print("--- Testing Method Overriding ---")

savings = SavingsAccount("Beimnet Tariku", "SAV001", 1000, 0.05)
current = CurrentAccount("Abel Kebede", "CUR001", 500, 1000)

print("\n--- Savings Account Statement ---")
savings.statement()

print("\n--- Current Account Statement ---")
current.statement()

print("\n" + "=" * 60)
print("TASK 5: POLYMORPHISM PRACTICE")
print("=" * 60)

# 5. Polymorphism Practice
print("\n--- Polymorphism Practice ---")

# Create a list containing objects of the three account types
accounts = [
    Account("Sara Hailu", "ACC001", 1000),
    SavingsAccount("Dawit Mekonnen", "SAV001", 2000, 0.05),
    CurrentAccount("Meron Taddesse", "CUR001", 1500, 800)
]

# Loop through and call statement() and deposit(100) on each
print("Demonstrating Polymorphism:")
for i, account in enumerate(accounts, 1):
    print(f"\n📌 Account {i}: {type(account).__name__}")
    account.statement()
    print("\n--- Making Deposit of $100 ---")
    account.deposit(100)

print("\n" + "=" * 60)
print("TASK 6: ABSTRACT BASE CLASS")
print("=" * 60)

# 6. Abstract Base Class
from abc import ABC, abstractmethod

class Account(ABC):
    """Abstract Base Class: Account"""
    
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
        """Display account statement"""
        print("\n" + "=" * 50)
        print("📋 ACCOUNT STATEMENT")
        print("=" * 50)
        print(f"👤 Owner: {self.owner}")
        print(f"🔢 Account: {self.account_number}")
        print(f"💰 Balance: ${self.__balance:.2f}")
        print("=" * 50)
    
    @abstractmethod
    def calculate_interest(self):
        """Abstract method to calculate interest"""
        pass

class SavingsAccount(Account):
    """SavingsAccount implementing abstract method"""
    
    def __init__(self, owner, account_number, balance=0, interest_rate=0.05):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"📈 Added interest: ${interest:.2f}")
    
    def calculate_interest(self):
        """Implement abstract method"""
        return self.balance * self.interest_rate
    
    def statement(self):
        print("\n" + "=" * 50)
        print("📋 SAVINGS ACCOUNT STATEMENT")
        print("=" * 50)
        print(f"👤 Owner: {self.owner}")
        print(f"🔢 Account: {self.account_number}")
        print(f"💰 Balance: ${self.balance:.2f}")
        print(f"📊 Interest Rate: {self.interest_rate * 100}%")
        print(f"📈 Interest Earned: ${self.calculate_interest():.2f}")
        print("=" * 50)

class CurrentAccount(Account):
    """CurrentAccount implementing abstract method"""
    
    def __init__(self, owner, account_number, balance=0, overdraft_limit=500):
        super().__init__(owner, account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
            return False
        
        if amount <= self.balance + self.overdraft_limit:
            self._Account__balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount:.2f}")
            print(f"✅ Withdrew ${amount:.2f}")
            if self.balance < 0:
                print(f"⚠️ Overdraft used! Balance: ${self.balance:.2f}")
            else:
                print(f"💰 New balance: ${self.balance:.2f}")
            return True
        else:
            print(f"❌ Overdraft limit exceeded!")
            return False
    
    def calculate_interest(self):
        """Implement abstract method"""
        return 0  # Current accounts don't earn interest
    
    def statement(self):
        print("\n" + "=" * 50)
        print("📋 CURRENT ACCOUNT STATEMENT")
        print("=" * 50)
        print(f"👤 Owner: {self.owner}")
        print(f"🔢 Account: {self.account_number}")
        print(f"💰 Balance: ${self.balance:.2f}")
        print(f"🏦 Overdraft Limit: ${self.overdraft_limit:.2f}")
        if self.balance < 0:
            print(f"⚠️ Overdraft used: ${abs(self.balance):.2f}")
            print(f"📊 Remaining overdraft: ${self.overdraft_limit + self.balance:.2f}")
        print("=" * 50)

# Test abstract classes
print("\n--- Testing Abstract Class Implementation ---")
savings = SavingsAccount("Beimnet Tariku", "SAV002", 1000, 0.05)
current = CurrentAccount("Abel Kebede", "CUR002", 500, 1000)

print("\n--- Savings Account ---")
savings.statement()
print(f"📈 Interest calculated: ${savings.calculate_interest():.2f}")

print("\n--- Current Account ---")
current.statement()
print(f"📈 Interest calculated: ${current.calculate_interest():.2f}")

print("\n" + "=" * 60)
print("🎉 LEVEL 2 COMPLETE!")
print("=" * 60)
