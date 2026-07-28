
print("=" * 60)
print("🏦 ADDIS BANK ACCOUNT SYSTEM")
print("=" * 60)
print("Welcome to Addis Bank! Your trusted banking partner.")
print("=" * 60)

class BankAccount:
    
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance  # Private attribute
        self.transaction_history = []
        self.__is_active = True
    
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
        return self.__is_active
    
    def deposit(self, amount):
        if not self.__is_active:
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
        if not self.__is_active:
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
    
    def transfer(self, to_account, amount):
        if not self.__is_active:
            print("❌ Your account is deactivated!")
            return False
        
        if not isinstance(to_account, BankAccount):
            print("❌ Invalid target account!")
            return False
        
        if not to_account.is_active:
            print("❌ Target account is deactivated!")
            return False
        
        if amount <= 0:
            print("❌ Transfer amount must be positive!")
            return False
        
        if amount > self.__balance:
            print(f"❌ Insufficient funds! You have ${self.__balance:.2f}")
            return False
        
        self.__balance -= amount
        to_account._BankAccount__balance += amount
        self.transaction_history.append(f"Transfer to {to_account.owner}: -${amount:.2f}")
        to_account.transaction_history.append(f"Transfer from {self.owner}: +${amount:.2f}")
        print(f"✅ Transferred ${amount:.2f} to {to_account.owner}")
        print(f"💰 Your new balance: ${self.__balance:.2f}")
        return True
    
    def show_transactions(self):
        if not self.transaction_history:
            print("📭 No transactions yet.")
            return
        
        print("\n📋 Transaction History:")
        print("-" * 50)
        for i, transaction in enumerate(self.transaction_history, 1):
            print(f"  {i:2d}. {transaction}")
        print("-" * 50)
    
    def account_info(self):
        print("\n" + "=" * 50)
        print("📋 ACCOUNT INFORMATION")
        print("=" * 50)
        print(f"👤 Owner: {self.owner}")
        print(f"🔢 Account Number: {self.account_number}")
        print(f"💰 Balance: ${self.__balance:.2f}")
        print(f"📊 Status: {'🟢 Active' if self.__is_active else '🔴 Inactive'}")
        print(f"📝 Total Transactions: {len(self.transaction_history)}")
        print("=" * 50)
    
    def deactivate(self):
        if self.__is_active:
            self.__is_active = False
            print(f"🔴 Account {self.account_number} deactivated.")
        else:
            print("⚠️ Account is already deactivated.")
    
    def activate(self):
        if not self.__is_active:
            self.__is_active = True
            print(f"🟢 Account {self.account_number} activated.")
        else:
            print("⚠️ Account is already active.")


accounts = {}
next_account_number = 1001

def create_account():
    global next_account_number
    
    print("\n" + "-" * 40)
    print("📝 CREATE NEW ACCOUNT")
    print("-" * 40)
    
    owner = input("Enter account holder name: ").strip()
    
    if not owner:
        print("❌ Name cannot be empty!")
        return
    
    try:
        initial_balance = float(input("Enter initial balance (default 0): ") or "0")
        if initial_balance < 0:
            print("❌ Initial balance cannot be negative!")
            return
    except ValueError:
        print("❌ Invalid amount! Please enter a number.")
        return
    
    account_number = f"ACC{next_account_number:04d}"
    next_account_number += 1
    
    account = BankAccount(owner, account_number, initial_balance)
    accounts[account_number] = account
    
    print(f"\n✅ Account created successfully!")
    print(f"🔢 Account Number: {account_number}")
    print(f"👤 Owner: {owner}")
    print(f"💰 Initial Balance: ${initial_balance:.2f}")
    print("📝 Please save your account number for future transactions!")

def find_account():
    account_number = input("Enter account number: ").strip().upper()
    
    if account_number in accounts:
        return accounts[account_number]
    else:
        print(f"❌ Account {account_number} not found!")
        return None

def deposit():
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
        print("❌ Invalid amount! Please enter a number.")

def withdraw():
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
        print("❌ Invalid amount! Please enter a number.")

def transfer():
    print("\n" + "-" * 40)
    print("🔄 TRANSFER")
    print("-" * 40)
    
    print("From Account:")
    from_account = find_account()
    if not from_account:
        return
    
    print("\nTo Account:")
    to_account = find_account()
    if not to_account:
        return
    
    try:
        amount = float(input("Enter transfer amount: $"))
        from_account.transfer(to_account, amount)
    except ValueError:
        print("❌ Invalid amount! Please enter a number.")

def check_balance():
    print("\n" + "-" * 40)
    print("📊 CHECK BALANCE")
    print("-" * 40)
    
    account = find_account()
    if not account:
        return
    
    print(f"\n💰 Current Balance: ${account.balance:.2f}")

def view_account_info():
    print("\n" + "-" * 40)
    print("📋 VIEW ACCOUNT INFO")
    print("-" * 40)
    
    account = find_account()
    if not account:
        return
    
    account.account_info()
    
    show_trans = input("\nShow transaction history? (y/n): ").lower()
    if show_trans == 'y':
        account.show_transactions()

def view_all_accounts():
    print("\n" + "-" * 40)
    print("📋 ALL ACCOUNTS")
    print("-" * 40)
    
    if not accounts:
        print("📭 No accounts in the system.")
        return
    
    print("\n🏦 Account Summary:")
    print("=" * 60)
    print(f"{'Account Number':<15} {'Owner':<20} {'Balance':<15} {'Status'}")
    print("-" * 60)
    
    for acc_num, account in accounts.items():
        status = "🟢 Active" if account.is_active else "🔴 Inactive"
        print(f"{acc_num:<15} {account.owner:<20} ${account.balance:<14.2f} {status}")
    print("-" * 60)
    print(f"Total Accounts: {len(accounts)}")

def deactivate_account():
    print("\n" + "-" * 40)
    print("🔴 DEACTIVATE ACCOUNT")
    print("-" * 40)
    
    account = find_account()
    if not account:
        return
    
    confirm = input(f"Are you sure you want to deactivate account {account.account_number}? (y/n): ").lower()
    if confirm == 'y':
        account.deactivate()

def activate_account():
    print("\n" + "-" * 40)
    print("🟢 ACTIVATE ACCOUNT")
    print("-" * 40)
    
    account = find_account()
    if not account:
        return
    
    account.activate()


def main():
    
    while True:
        print("\n" + "=" * 50)
        print("🏦 ADDIS BANK - MAIN MENU")
        print("=" * 50)
        print("1️⃣  Create New Account")
        print("2️⃣  Deposit")
        print("3️⃣  Withdraw")
        print("4️⃣  Transfer")
        print("5️⃣  Check Balance")
        print("6️⃣  View Account Info")
        print("7️⃣  View All Accounts")
        print("8️⃣  Deactivate Account")
        print("9️⃣  Activate Account")
        print("0️⃣  Exit")
        print("=" * 50)
        
        choice = input("\nEnter your choice (0-9): ").strip()
        
        if choice == "1":
            create_account()
        
        elif choice == "2":
            deposit()
        
        elif choice == "3":
            withdraw()
        
        elif choice == "4":
            transfer()
        
        elif choice == "5":
            check_balance()
        
        elif choice == "6":
            view_account_info()
        
        elif choice == "7":
            view_all_accounts()
        
        elif choice == "8":
            deactivate_account()
        
        elif choice == "9":
            activate_account()
        
        elif choice == "0":
            print("\n" + "=" * 50)
            print("👋 Thank you for using Addis Bank!")
            print("=" * 50)
            print("\n📊 Final Summary:")
            print("-" * 30)
            print(f"Total Accounts: {len(accounts)}")
            if accounts:
                total_balance = sum(account.balance for account in accounts.values())
                print(f"Total Balance Across All Accounts: ${total_balance:.2f}")
            print("\n💼 Addis Bank - Your Trusted Partner!")
            print("=" * 50)
            break
        
        else:
            print("❌ Invalid choice! Please enter a number between 0-9.")


if __name__ == "__main__":
    main()

print("\n" + "=" * 60)
print("🎉 MINI PROJECT COMPLETE!")
print("=" * 60)
