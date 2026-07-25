# ============================================
# Day 5 - Level 3: Advanced
# ============================================

print("=" * 60)
print("TASK 7: FULL ACCOUNT HIERARCHY")
print("=" * 60)

from abc import ABC, abstractmethod

# 7. Full Account Hierarchy
class Account(ABC):
    """Abstract Base Class: Account with full implementation"""
    
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance
        self.transaction_history = []
        self._is_active = True
    
    @property
    def balance(self):
        """Getter for balance"""
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        """Setter for balance with validation"""
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = amount
    
    @property
    def is_active(self):
        """Getter for account status"""
        return self._is_active
    
    def deposit(self, amount):
        """Deposit money with validation"""
        if not self._is_active:
            print("❌ Account is deactivated!")
            return False
        
        if amount <= 0:
            print("❌ Deposit amount must be positive!")
            return False
        
        self.__balance += amount
        self.transaction_history.append(f"Deposit: +${amount:.2f}")
        print(f"✅ Deposited ${amount:.2f}")
        print(f"💰 New balance: ${self.__balance:.2f}")
        return True
    
    def withdraw(self, amount):
        """Withdraw money with validation"""
        if not self._is_active:
            print("❌ Account is deactivated!")
            return False
        
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
        print(f"📊 Status: {'🟢 Active' if self._is_active else '🔴 Inactive'}")
        print("=" * 50)
    
    def deactivate(self):
        """Deactivate the account"""
        if self._is_active:
            self._is_active = False
            print(f"🔴 Account {self.account_number} deactivated.")
        else:
            print("⚠️ Account is already deactivated.")
    
    def activate(self):
        """Activate the account"""
        if not self._is_active:
            self._is_active = True
            print(f"🟢 Account {self.account_number} activated.")
        else:
            print("⚠️ Account is already active.")
    
    @abstractmethod
    def calculate_interest(self):
        """Abstract method to calculate interest"""
        pass

class SavingsAccount(Account):
    """SavingsAccount with interest rate"""
    
    def __init__(self, owner, account_number, balance=0, interest_rate=0.05):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        """Add interest to the balance"""
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"📈 Added interest: ${interest:.2f}")
        return interest
    
    def calculate_interest(self):
        """Implement abstract method"""
        return self.balance * self.interest_rate
    
    def statement(self):
        """Override statement to show interest rate"""
        print("\n" + "=" * 50)
        print("📋 SAVINGS ACCOUNT STATEMENT")
        print("=" * 50)
        print(f"👤 Owner: {self.owner}")
        print(f"🔢 Account: {self.account_number}")
        print(f"💰 Balance: ${self.balance:.2f}")
        print(f"📊 Interest Rate: {self.interest_rate * 100}%")
        print(f"📈 Interest Earned: ${self.calculate_interest():.2f}")
        print(f"📊 Status: {'🟢 Active' if self._is_active else '🔴 Inactive'}")
        print("=" * 50)

class CurrentAccount(Account):
    """CurrentAccount with overdraft facility"""
    
    def __init__(self, owner, account_number, balance=0, overdraft_limit=500):
        super().__init__(owner, account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        """Override withdraw to allow overdraft"""
        if not self._is_active:
            print("❌ Account is deactivated!")
            return False
        
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
            return False
        
        if amount <= self.balance + self.overdraft_limit:
            self._Account__balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount:.2f}")
            print(f"✅ Withdrew ${amount:.2f}")
            
            if self.balance < 0:
                print(f"⚠️ Overdraft used! Balance: ${self.balance:.2f}")
                print(f"📊 Remaining overdraft: ${self.overdraft_limit + self.balance:.2f}")
            else:
                print(f"💰 New balance: ${self.balance:.2f}")
            return True
        else:
            print(f"❌ Overdraft limit exceeded!")
            print(f"💰 Available: ${self.balance:.2f} + ${self.overdraft_limit:.2f}")
            return False
    
    def calculate_interest(self):
        """Implement abstract method"""
        return 0  # Current accounts don't earn interest
    
    def statement(self):
        """Override statement to show overdraft info"""
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
        print(f"📊 Status: {'🟢 Active' if self._is_active else '🔴 Inactive'}")
        print("=" * 50)

# Test the full hierarchy
print("\n--- Testing Full Account Hierarchy ---")

# Create accounts
savings = SavingsAccount("Beimnet Tariku", "SAV003", 1000, 0.05)
current = CurrentAccount("Abel Kebede", "CUR003", 500, 1000)

# Test methods
print("\n--- Savings Account ---")
savings.statement()
savings.deposit(200)
savings.add_interest()

print("\n--- Current Account ---")
current.statement()
current.withdraw(1200)  # Using overdraft
current.withdraw(500)   # Should exceed limit

print("\n" + "=" * 60)
print("🎉 LEVEL 3 COMPLETE!")
print("=" * 60)
