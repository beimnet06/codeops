# ============================================
# Day 6 - Intermediate: SOLID + Design Patterns
# ============================================

print("=" * 60)
print("TASK 1: SRP + DIP REFACTORING")
print("=" * 60)

from abc import ABC, abstractmethod

# ============================================
# BAD DESIGN: Account does everything
# ============================================
class BadAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        self.__balance += amount
        self.transactions.append(f"+${amount}")
        self._save_to_db()
        self._send_notification()
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append(f"-${amount}")
            self._save_to_db()
            self._send_notification()
    
    def _save_to_db(self):
        print(f"💾 Saving to database: {self.owner}")
    
    def _send_notification(self):
        print(f"📧 Sending email notification to {self.owner}")

print("--- Bad Design (SRP + DIP Violation) ---")
bad_account = BadAccount("John Doe", 1000)
bad_account.deposit(500)
bad_account.withdraw(200)

print("\n" + "=" * 40)
print("--- Good Design (SRP + DIP) ---")

# ============================================
# GOOD DESIGN: Separate responsibilities with Dependency Injection
# ============================================

# Interface for notifications (DIP)
class Notifier(ABC):
    @abstractmethod
    def notify(self, message):
        pass

# Interface for persistence (DIP)
class Repository(ABC):
    @abstractmethod
    def save(self, data):
        pass

# Concrete implementations
class EmailNotifier(Notifier):
    def notify(self, message):
        print(f"📧 Email: {message}")

class SMSNotifier(Notifier):
    def notify(self, message):
        print(f"📱 SMS: {message}")

class DatabaseRepository(Repository):
    def save(self, data):
        print(f"💾 Database: {data}")

class FileRepository(Repository):
    def save(self, data):
        print(f"📁 File: {data}")

# Clean Account class - only handles account logic (SRP)
class Account:
    def __init__(self, owner, balance=0, notifier=None, repository=None):
        self.owner = owner
        self.__balance = balance
        self.transactions = []
        self.notifier = notifier or EmailNotifier()  # Dependency Injection
        self.repository = repository or DatabaseRepository()  # Dependency Injection
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be positive!")
            return False
        
        self.__balance += amount
        self.transactions.append(f"+${amount}")
        self._notify(f"Deposited ${amount}")
        self._save()
        print(f"✅ Deposited ${amount}")
        return True
    
    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
            return False
        
        if amount > self.__balance:
            print(f"❌ Insufficient funds! You have ${self.__balance}")
            return False
        
        self.__balance -= amount
        self.transactions.append(f"-${amount}")
        self._notify(f"Withdrew ${amount}")
        self._save()
        print(f"✅ Withdrew ${amount}")
        return True
    
    def _notify(self, message):
        if self.notifier:
            self.notifier.notify(f"Account {self.owner}: {message}")
    
    def _save(self):
        if self.repository:
            data = {
                'owner': self.owner,
                'balance': self.__balance,
                'transactions': len(self.transactions)
            }
            self.repository.save(data)

# Test the good design
print("\n--- Creating Account with Email + Database ---")
account1 = Account(
    "Jane Smith", 
    1000, 
    notifier=EmailNotifier(),
    repository=DatabaseRepository()
)
account1.deposit(500)
account1.withdraw(200)

print("\n--- Creating Account with SMS + File ---")
account2 = Account(
    "Bob Johnson",
    500,
    notifier=SMSNotifier(),
    repository=FileRepository()
)
account2.deposit(100)

print("\n" + "=" * 60)
print("TASK 2: FACTORY PATTERN")
print("=" * 60)

# ============================================
# Factory Pattern
# ============================================

# Base Account classes (simplified for demo)
class BaseAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance
        self.type = "Base"
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"✅ Deposited ${amount}")
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"✅ Withdrew ${amount}")
            return True
        print("❌ Insufficient funds!")
        return False

class SavingsAccount(BaseAccount):
    def __init__(self, owner, account_number, balance=0, interest_rate=0.05):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate
        self.type = "Savings"
    
    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"📈 Added ${interest:.2f} interest")

class CurrentAccount(BaseAccount):
    def __init__(self, owner, account_number, balance=0, overdraft_limit=500):
        super().__init__(owner, account_number, balance)
        self.overdraft_limit = overdraft_limit
        self.type = "Current"
    
    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            print(f"✅ Withdrew ${amount}")
            if self._balance < 0:
                print(f"⚠️ Overdraft used! Balance: ${self._balance}")
            return True
        print("❌ Overdraft limit exceeded!")
        return False

class FixedDepositAccount(BaseAccount):
    def __init__(self, owner, account_number, balance=0, interest_rate=0.08, lock_in_years=2):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate
        self.lock_in_years = lock_in_years
        self.type = "Fixed Deposit"
    
    def withdraw(self, amount):
        print("❌ Cannot withdraw from Fixed Deposit account until maturity!")
        return False

# Factory Pattern Implementation
class AccountFactory:
    """Factory class to create different account types"""
    
    @staticmethod
    def create(kind, owner, account_number, balance=0, **kwargs):
        """Static method to create accounts based on type"""
        
        if kind == "savings":
            return SavingsAccount(owner, account_number, balance, 
                                 kwargs.get('interest_rate', 0.05))
        elif kind == "current":
            return CurrentAccount(owner, account_number, balance,
                                 kwargs.get('overdraft_limit', 500))
        elif kind == "fixed":
            return FixedDepositAccount(owner, account_number, balance,
                                      kwargs.get('interest_rate', 0.08),
                                      kwargs.get('lock_in_years', 2))
        else:
            raise ValueError(f"Unknown account type: {kind}")

# Test the Factory Pattern
print("\n--- Testing Factory Pattern ---")

# Create different account types using the factory
savings = AccountFactory.create("savings", "Alice", "SAV001", 1000)
current = AccountFactory.create("current", "Bob", "CUR001", 500, overdraft_limit=1000)
fixed = AccountFactory.create("fixed", "Charlie", "FIX001", 2000, interest_rate=0.10, lock_in_years=3)

print(f"Created {savings.type} account: {savings.account_number}")
print(f"Created {current.type} account: {current.account_number}")
print(f"Created {fixed.type} account: {fixed.account_number}")

print("\n--- Testing Account Operations ---")
savings.deposit(200)
savings.add_interest()
print(f"Savings balance: ${savings.balance}")

print("\n" + "=" * 60)
print("TASK 3: OBSERVER PATTERN")
print("=" * 60)

# ============================================
# Observer Pattern Implementation
# ============================================

class Observer(ABC):
    """Abstract Observer class"""
    @abstractmethod
    def update(self, message):
        pass

class SMSAlert(Observer):
    """SMS Alert Observer"""
    def update(self, message):
        print(f"📱 SMS Alert: {message}")

class AuditLog(Observer):
    """Audit Log Observer"""
    def update(self, message):
        print(f"📋 Audit Log: {message}")

class EmailAlert(Observer):
    """Email Alert Observer"""
    def update(self, message):
        print(f"📧 Email Alert: {message}")

class ObservableAccount:
    """Account with Observer pattern"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self._observers = []
        self.transactions = []
    
    def attach(self, observer):
        """Add an observer"""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"✅ Added observer: {observer.__class__.__name__}")
    
    def detach(self, observer):
        """Remove an observer"""
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"✅ Removed observer: {observer.__class__.__name__}")
    
    def _notify_observers(self, message):
        """Notify all observers"""
        for observer in self._observers:
            observer.update(message)
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be positive!")
            return False
        
        self.__balance += amount
        self.transactions.append(f"+${amount}")
        print(f"✅ Deposited ${amount}")
        if amount > 1000:
            self._notify_observers(f"Large deposit: ${amount} by {self.owner}")
        return True
    
    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
            return False
        
        if amount > self.__balance:
            print(f"❌ Insufficient funds! You have ${self.__balance}")
            return False
        
        self.__balance -= amount
        self.transactions.append(f"-${amount}")
        print(f"✅ Withdrew ${amount}")
        
        # Notify observers for large withdrawals (> $3000)
        if amount > 3000:
            self._notify_observers(f"Large withdrawal: ${amount} by {self.owner}")
        return True

# Test Observer Pattern
print("\n--- Testing Observer Pattern ---")

# Create account with observers
account = ObservableAccount("Alice Johnson", 5000)
print(f"Account created for {account.owner}")

# Attach observers
print("\n--- Attaching Observers ---")
sms = SMSAlert()
audit = AuditLog()
email = EmailAlert()

account.attach(sms)
account.attach(audit)
account.attach(email)

print("\n--- Performing Normal Transaction ---")
account.deposit(500)

print("\n--- Performing Large Withdrawal (> $3000) ---")
account.withdraw(4000)

print("\n--- Performing Another Large Transaction ---")
account.deposit(2000)

print("\n" + "=" * 60)
print("TASK 4: INTERFACE SEGREGATION PRINCIPLE (ISP)")
print("=" * 60)

# ============================================
# ISP - Interface Segregation Principle
# ============================================

print("\n--- ISP Demonstration ---")

class InterestBearing:
    """Interface for accounts that earn interest"""
    def add_interest(self):
        raise NotImplementedError("Subclasses must implement add_interest()")
    
    def get_interest_rate(self):
        raise NotImplementedError("Subclasses must implement get_interest_rate()")

# SavingsAccount implements InterestBearing interface
class ISPSavingsAccount(InterestBearing):
    def __init__(self, balance=0, interest_rate=0.05):
        self.__balance = balance
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.__balance * self.interest_rate
        self.__balance += interest
        print(f"📈 Added ${interest:.2f} interest")
    
    def get_interest_rate(self):
        return self.interest_rate
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount

# CurrentAccount does NOT implement InterestBearing (ISP violation prevented)
class ISPCurrentAccount:
    def __init__(self, balance=0, overdraft_limit=500):
        self.__balance = balance
        self.overdraft_limit = overdraft_limit
    
    @property
    def balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount <= self.__balance + self.overdraft_limit:
            self.__balance -= amount
            print(f"✅ Withdrew ${amount}")
            return True
        print("❌ Insufficient funds!")
        return False

print("--- Testing ISP Design ---")

savings_account = ISPSavingsAccount(1000, 0.05)
print(f"Savings Account Balance: ${savings_account.balance}")
savings_account.add_interest()
print(f"After interest: ${savings_account.balance}")

current_account = ISPCurrentAccount(500, 1000)
print(f"Current Account Balance: ${current_account.balance}")
current_account.withdraw(1200)
print(f"After withdrawal: ${current_account.balance}")

print("\n✅ ISP: Savings accounts implement interest methods, Current accounts don't")
print("   No empty or unused methods in any class!")

print("\n" + "=" * 60)
print("INTERMEDIATE EXERCISES COMPLETE! 🎉")
print("=" * 60)
