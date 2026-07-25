# ============================================
# DAY 5 MINI PROJECT: Addis Bank System V2
# ============================================

print("=" * 60)
print("🏦 ADDIS BANK SYSTEM - VERSION 2")
print("=" * 60)
print("Welcome to Addis Bank! Your trusted banking partner.")
print("=" * 60)

from abc import ABC, abstractmethod
import time

# ============================================
# Account Classes (Abstract)
# ============================================

class Account(ABC):
    """Abstract Base Class: Account"""
    
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance
        self.transaction_history = []
        self._is_active = True
        self._account_type = "Base"
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = amount
    
    @property
    def is_active(self):
        return self._is_active
    
    @property
    def account_type(self):
        return self._account_type
    
    def deposit(self, amount):
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
        print("\n" + "=" * 50)
        print(f"📋 {self.account_type.upper()} STATEMENT")
        print("=" * 50)
        print(f"👤 Owner: {self.owner}")
        print(f"🔢 Account: {self.account_number}")
        print(f"💰 Balance: ${self.__balance:.2f}")
        print(f"📊 Status: {'🟢 Active' if self._is_active else '🔴 Inactive'}")
        print("=" * 50)
    
    def deactivate(self):
        if self._is_active:
            self._is_active = False
            print(f"🔴 Account {self.account_number} deactivated.")
    
    def activate(self):
        if not self._is_active:
            self._is_active = True
            print(f"🟢 Account {self.account_number} activated.")
    
    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    """SavingsAccount with interest rate"""
    
    def __init__(self, owner, account_number, balance=0, interest_rate=0.05):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate
        self._account_type = "Savings"
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        if interest > 0:
            self._Account__balance += interest
            self.transaction_history.append(f"Interest: +${interest:.2f}")
            print(f"📈 Added interest: ${interest:.2f}")
            return interest
        return 0
    
    def calculate_interest(self):
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
        print(f"📊 Status: {'🟢 Active' if self._is_active else '🔴 Inactive'}")
        print("=" * 50)

class CurrentAccount(Account):
    """CurrentAccount with overdraft facility"""
    
    def __init__(self, owner, account_number, balance=0, overdraft_limit=500):
        super().__init__(owner, account_number, balance)
        self.overdraft_limit = overdraft_limit
        self._account_type = "Current"
    
    def withdraw(self, amount):
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
        return 0
    
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
        else:
            print(f"💚 Overdraft available: ${self.overdraft_limit:.2f}")
        print(f"📊 Status: {'🟢 Active' if self._is_active else '🔴 Inactive'}")
        print("=" * 50)

class FixedDepositAccount(SavingsAccount):
    """Bonus: FixedDepositAccount with lock-in period"""
    
    def __init__(self, owner, account_number, balance=0, interest_rate=0.08, lock_in_years=1):
        super().__init__(owner, account_number, balance, interest_rate)
        self.lock_in_years = lock_in_years
        self._account_type = "Fixed Deposit"
        self._created_date = time.time()
    
    def withdraw(self, amount):
        print("❌ Cannot withdraw from Fixed Deposit account until maturity!")
        return False
    
    def calculate_interest(self):
        return self.balance * self.interest_rate * self.lock_in_years

# ============================================
# Main Program Functions
# ============================================

accounts = {}
next_account_number = 1001

def create_savings_account():
    """Create a new Savings Account"""
    global next_account_number
    
    print("\n" + "-" * 40)
    print("💰 CREATE SAVINGS ACCOUNT")
    print("-" * 40)
    
    owner = input("Enter account holder name: ").strip()
    if not owner:
        print("❌ Name cannot be empty!")
        return
    
    try:
        balance = float(input("Enter initial balance (default 0): ") or "0")
        if balance < 0:
            print("❌ Balance cannot be negative!")
            return
    except ValueError:
        print("❌ Invalid amount!")
        return
    
    try:
        interest_rate = float(input("Enter interest rate (default 0.05): ") or "0.05")
        if interest_rate < 0 or interest_rate > 1:
            print("❌ Interest rate must be between 0 and 1!")
            return
    except ValueError:
        print("❌ Invalid interest rate!")
        return
    
    account_number = f"SAV{next_account_number:04d}"
    next_account_number += 1
    
    account = SavingsAccount(owner, account_number, balance, interest_rate)
    accounts[account_number] = account
    
    print(f"\n✅ Savings Account created successfully!")
    print(f"🔢 Account Number: {account_number}")
    account.statement()

def create_current_account():
    """Create a new Current Account"""
    global next_account_number
    
    print("\n" + "-" * 40)
    print("💳 CREATE CURRENT ACCOUNT")
    print("-" * 40)
    
    owner = input("Enter account holder name: ").strip()
    if not owner:
        print("❌ Name cannot be empty!")
        return
    
    try:
        balance = float(input("Enter initial balance (default 0): ") or "0")
        if balance < 0:
            print("❌ Balance cannot be negative!")
            return
    except ValueError:
        print("❌ Invalid amount!")
        return
    
    try:
        overdraft = float(input("Enter overdraft limit (default 500): ") or "500")
        if overdraft < 0:
            print("❌ Overdraft limit cannot be negative!")
            return
    except ValueError:
        print("❌ Invalid amount!")
        return
    
    account_number = f"CUR{next_account_number:04d}"
    next_account_number += 1
    
    account = CurrentAccount(owner, account_number, balance, overdraft)
    accounts[account_number] = account
    
    print(f"\n✅ Current Account created successfully!")
    print(f"🔢 Account Number: {account_number}")
    account.statement()

def find_account():
    """Find and return an account by account number"""
    account_number = input("Enter account number: ").strip().upper()
    
    if account_number in accounts:
        return accounts[account_number]
    else:
        print(f"❌ Account {account_number} not found!")
        return None

def deposit():
    """Deposit money into an account"""
    print("\n" + "-" * 40)
    print("💰 DEPOSIT")
    print("-" * 40)
    
    account = find_account()
    if not account:
        return
    
    try:
        amount = float(input("Enter deposit amount: $"))
        account.deposit(amount)
    except ValueError:
        print("❌ Invalid amount!")

def withdraw():
    """Withdraw money from an account"""
    print("\n" + "-" * 40)
    print("💸 WITHDRAW")
    print("-" * 40)
    
    account = find_account()
    if not account:
        return
    
    try:
        amount = float(input("Enter withdrawal amount: $"))
        account.withdraw(amount)
    except ValueError:
        print("❌ Invalid amount!")

def show_statement():
    """Show account statement"""
    print("\n" + "-" * 40)
    print("📋 SHOW STATEMENT")
    print("-" * 40)
    
    account = find_account()
    if not account:
        return
    
    account.statement()

def apply_interest():
    """Apply interest to all savings accounts"""
    print("\n" + "-" * 40)
    print("📈 APPLY INTEREST")
    print("-" * 40)
    
    count = 0
    for acc_num, account in accounts.items():
        if isinstance(account, SavingsAccount):
            account.add_interest()
            count += 1
    
    if count == 0:
        print("📭 No Savings Accounts found.")
    else:
        print(f"✅ Applied interest to {count} Savings Account(s).")

def show_all_accounts():
    """Show all accounts using polymorphism"""
    print("\n" + "-" * 40)
    print("📋 ALL ACCOUNTS")
    print("-" * 40)
    
    if not accounts:
        print("📭 No accounts in the system.")
        return
    
    print("\n🏦 Account Summary:")
    print("=" * 70)
    print(f"{'Account Number':<15} {'Type':<12} {'Owner':<20} {'Balance':<15} {'Status'}")
    print("-" * 70)
    
    for acc_num, account in accounts.items():
        status = "🟢 Active" if account.is_active else "🔴 Inactive"
        print(f"{acc_num:<15} {account.account_type:<12} {account.owner:<20} ${account.balance:<14.2f} {status}")
    print("-" * 70)
    print(f"Total Accounts: {len(accounts)}")

# ============================================
# Main Menu
# ============================================

def main():
    while True:
        print("\n" + "=" * 50)
        print("🏦 ADDIS BANK - MAIN MENU V2")
        print("=" * 50)
        print("1️⃣  Create Savings Account")
        print("2️⃣  Create Current Account")
        print("3️⃣  Deposit")
        print("4️⃣  Withdraw")
        print("5️⃣  Show Statement")
        print("6️⃣  Apply Interest (All Savings)")
        print("7️⃣  Show All Accounts")
        print("8️⃣  Exit")
        print("=" * 50)
        
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == "1":
            create_savings_account()
        elif choice == "2":
            create_current_account()
        elif choice == "3":
            deposit()
        elif choice == "4":
            withdraw()
        elif choice == "5":
            show_statement()
        elif choice == "6":
            apply_interest()
        elif choice == "7":
            show_all_accounts()
        elif choice == "8":
            print("\n" + "=" * 50)
            print("👋 Thank you for using Addis Bank!")
            print("=" * 50)
            print(f"\n📊 Final Summary:")
            print("-" * 30)
            print(f"Total Accounts: {len(accounts)}")
            if accounts:
                total_balance = sum(account.balance for account in accounts.values())
                print(f"Total Balance: ${total_balance:.2f}")
            print("\n💼 Addis Bank - Your Trusted Partner!")
            print("=" * 50)
            break
        else:
            print("❌ Invalid choice! Please enter 1-8.")

if __name__ == "__main__":
    main()

print("\n" + "=" * 60)
print("🎉 MINI PROJECT COMPLETE!")
print("=" * 60)
