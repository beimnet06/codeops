# ============================================
# DAY 6 MINI PROJECT: Clean Addis Bank System
# ============================================

print("=" * 60)
print("🏦 CLEAN ADDIS BANK SYSTEM")
print("=" * 60)
print("Built with SOLID Principles + Design Patterns")
print("=" * 60)

from abc import ABC, abstractmethod
import time

# ============================================
# Singleton Pattern: BankConfig
# ============================================

class BankConfig:
    """Singleton: Bank-wide configuration"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BankConfig, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        self.interest_rates = {
            'savings': 0.05,
            'fixed': 0.08,
            'investment': 0.10
        }
        self.overdraft_limits = {
            'current': 1000,
            'premium': 2000
        }
        self.notification_threshold = 3000
        self.bank_name = "Addis Bank"
        self.bank_version = "2.0"
    
    def get_interest_rate(self, account_type):
        return self.interest_rates.get(account_type, 0.0)
    
    def get_overdraft_limit(self, account_type):
        return self.overdraft_limits.get(account_type, 500)
    
    def get_notification_threshold(self):
        return self.notification_threshold

# ============================================
# Observer Pattern
# ============================================

class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass

class SMSAlert(Observer):
    def update(self, data):
        print(f"📱 SMS Alert: {data['owner']} made {data['type']} of ${data['amount']:.2f}")

class AuditLog(Observer):
    def update(self, data):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"📋 [{timestamp}] Audit: {data['account']} - {data['type']} ${data['amount']:.2f}")

class EmailAlert(Observer):
    def update(self, data):
        print(f"📧 Email: Dear {data['owner']}, {data['type']} of ${data['amount']:.2f} processed.")

# ============================================
# Abstract Account Class (DIP)
# ============================================

class BaseAccount(ABC):
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance
        self._observers = []
        self._transaction_counter = 0
        self._account_type = "Base"
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def account_type(self):
        return self._account_type
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def _notify_observers(self, transaction_type, amount):
        self._transaction_counter += 1
        data = {
            'id': self._transaction_counter,
            'owner': self.owner,
            'account': self.account_number,
            'type': transaction_type,
            'amount': amount
        }
        for observer in self._observers:
            observer.update(data)
    
    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be positive!")
            return False
        
        self.__balance += amount
        print(f"✅ Deposited ${amount:.2f}")
        
        config = BankConfig()
        if amount > config.get_notification_threshold():
            self._notify_observers("deposit", amount)
        return True
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    def statement(self):
        print("\n" + "=" * 50)
        print(f"📋 {self.account_type.upper()} STATEMENT")
        print("=" * 50)
        print(f"👤 Owner: {self.owner}")
        print(f"🔢 Account: {self.account_number}")
        print(f"💰 Balance: ${self.__balance:.2f}")
        print("=" * 50)

# ============================================
# Account Types (OCP - Open for Extension)
# ============================================

class SavingsAccount(BaseAccount):
    def __init__(self, owner, account_number, balance=0):
        super().__init__(owner, account_number, balance)
        self._account_type = "Savings"
        config = BankConfig()
        self.interest_rate = config.get_interest_rate('savings')
    
    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Amount must be positive!")
            return False
        
        if amount > self.balance:
            print(f"❌ Insufficient funds! You have ${self.balance:.2f}")
            return False
        
        self._BaseAccount__balance -= amount
        print(f"✅ Withdrew ${amount:.2f}")
        
        config = BankConfig()
        if amount > config.get_notification_threshold():
            self._notify_observers("withdrawal", amount)
        return True
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        if interest > 0:
            self._BaseAccount__balance += interest
            print(f"📈 Added ${interest:.2f} interest")
            return interest
        return 0

class CurrentAccount(BaseAccount):
    def __init__(self, owner, account_number, balance=0):
        super().__init__(owner, account_number, balance)
        self._account_type = "Current"
        config = BankConfig()
        self.overdraft_limit = config.get_overdraft_limit('current')
    
    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Amount must be positive!")
            return False
        
        if amount > self.balance + self.overdraft_limit:
            print(f"❌ Overdraft limit exceeded! Available: ${self.balance:.2f} + ${self.overdraft_limit:.2f}")
            return False
        
        self._BaseAccount__balance -= amount
        print(f"✅ Withdrew ${amount:.2f}")
        
        if self.balance < 0:
            print(f"⚠️ Overdraft used! Balance: ${self.balance:.2f}")
        
        config = BankConfig()
        if amount > config.get_notification_threshold():
            self._notify_observers("withdrawal", amount)
        return True

class FixedDepositAccount(BaseAccount):
    def __init__(self, owner, account_number, balance=0, lock_in_months=24):
        super().__init__(owner, account_number, balance)
        self._account_type = "Fixed Deposit"
        config = BankConfig()
        self.interest_rate = config.get_interest_rate('fixed')
        self.lock_in_months = lock_in_months
        self.created_at = time.time()
    
    def withdraw(self, amount):
        print("❌ Cannot withdraw from Fixed Deposit account until maturity!")
        print(f"📅 Lock-in period: {self.lock_in_months} months")
        return False
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate * (self.lock_in_months / 12)
        if interest > 0:
            self._BaseAccount__balance += interest
            print(f"📈 Added ${interest:.2f} interest")
            return interest
        return 0

class InvestmentAccount(BaseAccount):
    def __init__(self, owner, account_number, balance=0, risk_level="moderate"):
        super().__init__(owner, account_number, balance)
        self._account_type = "Investment"
        config = BankConfig()
        self.interest_rate = config.get_interest_rate('investment')
        self.risk_level = risk_level
    
    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Amount must be positive!")
            return False
        
        if amount > self.balance:
            print(f"❌ Insufficient funds! You have ${self.balance:.2f}")
            return False
        
        self._BaseAccount__balance -= amount
        print(f"✅ Withdrew ${amount:.2f}")
        
        config = BankConfig()
        if amount > config.get_notification_threshold():
            self._notify_observers("withdrawal", amount)
        return True
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        if interest > 0:
            self._BaseAccount__balance += interest
            print(f"📈 Added ${interest:.2f} interest")
            return interest
        return 0

# ============================================
# Factory Pattern (OCP)
# ============================================

class AccountFactory:
    """Factory to create different account types - open for extension"""
    
    @staticmethod
    def create(account_type, owner, account_number, balance=0, **kwargs):
        if account_type == "savings":
            return SavingsAccount(owner, account_number, balance)
        elif account_type == "current":
            return CurrentAccount(owner, account_number, balance)
        elif account_type == "fixed":
            return FixedDepositAccount(owner, account_number, balance, 
                                      kwargs.get('lock_in_months', 24))
        elif account_type == "investment":
            return InvestmentAccount(owner, account_number, balance,
                                    kwargs.get('risk_level', 'moderate'))
        else:
            raise ValueError(f"Unknown account type: {account_type}")

# ============================================
# Main Program
# ============================================

# Account storage
accounts = {}
account_counter = 1001

def create_account():
    """Create a new account using Factory Pattern"""
    global account_counter
    
    print("\n" + "-" * 40)
    print("📝 CREATE NEW ACCOUNT")
    print("-" * 40)
    print("Available types: savings, current, fixed, investment")
    
    acc_type = input("Enter account type: ").lower().strip()
    if acc_type not in ['savings', 'current', 'fixed', 'investment']:
        print("❌ Invalid account type!")
        return
    
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
    
    # Generate account number
    acc_number = f"ACC{account_counter:04d}"
    account_counter += 1
    
    # Create account using factory
    try:
        account = AccountFactory.create(acc_type, owner, acc_number, balance)
        
        # Attach observers for notifications
        sms = SMSAlert()
        audit = AuditLog()
        email = EmailAlert()
        account.attach(sms)
        account.attach(audit)
        account.attach(email)
        
        accounts[acc_number] = account
        
        print(f"\n✅ {account.account_type} Account created successfully!")
        print(f"🔢 Account Number: {acc_number}")
        account.statement()
        
    except ValueError as e:
        print(f"❌ {e}")

def find_account():
    """Find an account by number"""
    acc_number = input("Enter account number: ").strip().upper()
    if acc_number in accounts:
        return accounts[acc_number]
    else:
        print(f"❌ Account {acc_number} not found!")
        return None

def deposit():
    """Deposit money"""
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
    """Withdraw money"""
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

def apply_interest():
    """Apply interest to all eligible accounts"""
    print("\n" + "-" * 40)
    print("📈 APPLY INTEREST")
    print("-" * 40)
    
    count = 0
    for acc_number, account in accounts.items():
        if hasattr(account, 'apply_interest'):
            interest = account.apply_interest()
            if interest > 0:
                count += 1
                print(f"   {acc_number}: +${interest:.2f}")
    
    if count == 0:
        print("📭 No interest-bearing accounts found.")
    else:
        print(f"✅ Applied interest to {count} account(s).")

def show_all_accounts():
    """Show all accounts"""
    print("\n" + "-" * 40)
    print("📋 ALL ACCOUNTS")
    print("-" * 40)
    
    if not accounts:
        print("📭 No accounts in the system.")
        return
    
    print("\n" + "=" * 60)
    print(f"{'Number':<12} {'Type':<12} {'Owner':<15} {'Balance':<12}")
    print("-" * 60)
    
    for acc_number, account in accounts.items():
        balance = account.balance if hasattr(account, 'balance') else 0
        acc_type = account.account_type if hasattr(account, 'account_type') else "Unknown"
        print(f"{acc_number:<12} {acc_type:<12} {account.owner:<15} ${balance:<11.2f}")
    print("-" * 60)
    print(f"Total Accounts: {len(accounts)}")

def show_statement():
    """Show account statement"""
    print("\n" + "-" * 40)
    print("📋 SHOW STATEMENT")
    print("-" * 40)
    
    account = find_account()
    if not account:
        return
    
    account.statement()

def show_menu():
    """Display main menu"""
    print("\n" + "=" * 50)
    print("🏦 ADDIS BANK - MAIN MENU")
    print("=" * 50)
    print("1️⃣  Create Account")
    print("2️⃣  Deposit")
    print("3️⃣  Withdraw")
    print("4️⃣  Show Statement")
    print("5️⃣  Apply Interest")
    print("6️⃣  Show All Accounts")
    print("7️⃣  Exit")
    print("=" * 50)
    print(f"🏛️  {BankConfig().bank_name} v{BankConfig().bank_version}")
    print("=" * 50)

def main():
    """Main program loop"""
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            show_statement()
        elif choice == "5":
            apply_interest()
        elif choice == "6":
            show_all_accounts()
        elif choice == "7":
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
            break
        else:
            print("❌ Invalid choice! Please enter 1-7.")

if __name__ == "__main__":
    main()

print("\n" + "=" * 60)
print("🎉 MINI PROJECT COMPLETE!")
print("=" * 60)
