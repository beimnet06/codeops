
print("=" * 60)
print("💰 PERSONAL FINANCE TRACKER")
print("=" * 60)

balance = 0.0
transactions = []

def add_income():
    global balance
    
    print("\n" + "-" * 40)
    print("💵 ADD INCOME")
    print("-" * 40)
    
    try:
        amount = float(input("Enter income amount: $"))
        
        if amount <= 0:
            print("❌ Amount must be greater than 0!")
            return
        
        description = input("Enter description (e.g., Salary, Freelance): ")
        
        balance += amount
        transactions.append(f"+${amount:.2f} - {description}")
        
        print(f"✅ Income of ${amount:.2f} added successfully!")
        print(f"💰 New balance: ${balance:.2f}")
        
    except ValueError:
        print("❌ Invalid input! Please enter a number.")

def add_expense():
    global balance
    
    print("\n" + "-" * 40)
    print("💸 ADD EXPENSE")
    print("-" * 40)
    
    try:
        amount = float(input("Enter expense amount: $"))
        
        if amount <= 0:
            print("❌ Amount must be greater than 0!")
            return
        
        if amount > balance:
            print("❌ Insufficient balance! You don't have enough money.")
            print(f"💰 Current balance: ${balance:.2f}")
            return
        
        description = input("Enter description (e.g., Food, Transport): ")
        
        balance -= amount
        transactions.append(f"-${amount:.2f} - {description}")
        
        print(f"✅ Expense of ${amount:.2f} recorded successfully!")
        print(f"💰 New balance: ${balance:.2f}")
        
    except ValueError:
        print("❌ Invalid input! Please enter a number.")

def show_balance():
    print("\n" + "-" * 40)
    print("📊 BALANCE SUMMARY")
    print("-" * 40)
    
    print(f"💰 Current Balance: ${balance:.2f}")
    print(f"📝 Total Transactions: {len(transactions)}")
    
    if len(transactions) > 0:
        print("\n📋 Transaction History:")
        print("-" * 40)
        for i, transaction in enumerate(transactions, 1):
            print(f"{i:2d}. {transaction}")
    else:
        print("\n📋 No transactions yet.")
    
    print("-" * 40)

print("\n📱 Welcome to your Personal Finance Tracker!")
print("Manage your income and expenses easily.\n")

while True:
    print("\n" + "=" * 40)
    print("📋 MENU")
    print("=" * 40)
    print("1️⃣  Add Income")
    print("2️⃣  Add Expense")
    print("3️⃣  Show Balance")
    print("4️⃣  Exit")
    print("=" * 40)
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == "1":
        add_income()
    
    elif choice == "2":
        add_expense()
    
    elif choice == "3":
        show_balance()
    
    elif choice == "4":
        print("\n" + "=" * 40)
        print("👋 Thank you for using the Finance Tracker!")
        print("=" * 40)
        
        if len(transactions) > 0:
            print("\n📊 FINAL SUMMARY")
            print("-" * 40)
            print(f"💰 Final Balance: ${balance:.2f}")
            print(f"📝 Total Transactions: {len(transactions)}")
            print("\nHappy budgeting! 💰")
        else:
            print("\nNo transactions were made.")
            print("Come back when you're ready to track your finances!")
        
        break
    
    else:
        print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")
        print("Press any key to continue...")
        input()  # Wait for user to press Enter

print("\n" + "=" * 60)
print("🎉 MINI PROJECT COMPLETE!")
print("=" * 60)
