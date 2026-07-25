# ============================================
# DAY 7 MINI PROJECT: Bank Customer Service Simulator
# ============================================

print("=" * 60)
print("🏦 ADDIS BANK - CUSTOMER SERVICE SIMULATOR")
print("=" * 60)
print("Using Linear Data Structures: Stack, Queue, Dictionary")
print("=" * 60)

import time
from collections import deque
import random

# ============================================
# Data Structures
# ============================================

class TransactionHistory:
    """Stack implementation for transaction history"""
    
    def __init__(self):
        self.history = []  # O(1) push/pop
    
    def push(self, transaction):
        """Add a transaction - O(1)"""
        self.history.append(transaction)
        print(f"✅ Transaction added: {transaction}")
    
    def pop(self):
        """Undo last transaction - O(1)"""
        if not self.history:
            print("❌ No transactions to undo!")
            return None
        transaction = self.history.pop()
        print(f"↩️ Undone: {transaction}")
        return transaction
    
    def peek(self):
        """View last transaction without removing - O(1)"""
        if not self.history:
            return None
        return self.history[-1]
    
    def get_size(self):
        """Get number of transactions - O(1)"""
        return len(self.history)
    
    def __str__(self):
        if not self.history:
            return "No transactions"
        return " -> ".join(self.history)

class CustomerQueue:
    """Queue implementation for customer service"""
    
    def __init__(self):
        self.queue = deque()  # O(1) append/popleft
    
    def add_customer(self, name):
        """Add customer to queue - O(1)"""
        self.queue.append(name)
        print(f"📥 {name} added to queue")
    
    def serve_customer(self):
        """Serve next customer - O(1)"""
        if not self.queue:
            print("❌ No customers in queue!")
            return None
        customer = self.queue.popleft()
        print(f"💼 Serving: {customer}")
        return customer
    
    def get_size(self):
        """Get number of waiting customers - O(1)"""
        return len(self.queue)
    
    def get_queue(self):
        """Get all customers in queue"""
        return list(self.queue)

class CustomerDatabase:
    """Dictionary implementation for fast customer lookup"""
    
    def __init__(self):
        self.customers = {}  # O(1) lookup
    
    def add_customer(self, account_number, name, balance=0):
        """Add customer - O(1)"""
        self.customers[account_number] = {
            'name': name,
            'balance': balance,
            'created_at': time.strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"✅ Customer {name} (Account: {account_number}) added")
    
    def find_customer(self, account_number):
        """Find customer by account number - O(1)"""
        if account_number in self.customers:
            return self.customers[account_number]
        return None
    
    def update_balance(self, account_number, amount):
        """Update customer balance - O(1)"""
        if account_number in self.customers:
            self.customers[account_number]['balance'] += amount
            return True
        return False
    
    def get_all_customers(self):
        """Get all customers"""
        return self.customers

# ============================================
# Main Program
# ============================================

class BankServiceSimulator:
    def __init__(self):
        self.history = TransactionHistory()
        self.queue = CustomerQueue()
        self.database = CustomerDatabase()
        self.account_counter = 1001
    
    def generate_account_number(self):
        """Generate a unique account number"""
        acc_num = f"ACC{self.account_counter:04d}"
        self.account_counter += 1
        return acc_num
    
    def create_customer(self):
        """Create a new customer account"""
        print("\n" + "-" * 40)
        print("📝 CREATE NEW CUSTOMER")
        print("-" * 40)
        
        name = input("Enter customer name: ").strip()
        if not name:
            print("❌ Name cannot be empty!")
            return
        
        try:
            initial_balance = float(input("Enter initial balance (default 0): ") or "0")
            if initial_balance < 0:
                print("❌ Balance cannot be negative!")
                return
        except ValueError:
            print("❌ Invalid amount!")
            return
        
        account_number = self.generate_account_number()
        self.database.add_customer(account_number, name, initial_balance)
        
        # Add to transaction history
        self.history.push(f"Created account {account_number} for {name}")
        print(f"🔢 Account Number: {account_number}")
        print(f"💰 Balance: ${initial_balance:.2f}")
    
    def make_transaction(self):
        """Make a transaction (deposit or withdraw)"""
        print("\n" + "-" * 40)
        print("💰 MAKE TRANSACTION")
        print("-" * 40)
        
        account_number = input("Enter account number: ").strip().upper()
        customer = self.database.find_customer(account_number)
        
        if not customer:
            print(f"❌ Account {account_number} not found!")
            return
        
        print(f"👤 Customer: {customer['name']}")
        print(f"💰 Current Balance: ${customer['balance']:.2f}")
        
        try:
            amount = float(input("Enter transaction amount: $"))
            if amount <= 0:
                print("❌ Amount must be positive!")
                return
            
            transaction_type = input("Type 'deposit' or 'withdraw': ").lower().strip()
            
            if transaction_type == "deposit":
                self.database.update_balance(account_number, amount)
                self.history.push(f"Deposited ${amount:.2f} to {account_number}")
                print(f"✅ Deposited ${amount:.2f}")
                print(f"💰 New Balance: ${customer['balance']:.2f}")
                
                # Check if this is a large transaction
                if amount > 5000:
                    print("⚠️ Large deposit detected! Adding to queue for review.")
                    self.queue.add_customer(f"Review: {account_number} (${amount:.2f})")
                
            elif transaction_type == "withdraw":
                if amount > customer['balance']:
                    print(f"❌ Insufficient funds! You have ${customer['balance']:.2f}")
                    return
                
                self.database.update_balance(account_number, -amount)
                self.history.push(f"Withdrew ${amount:.2f} from {account_number}")
                print(f"✅ Withdrew ${amount:.2f}")
                print(f"💰 New Balance: ${customer['balance']:.2f}")
                
                # Check for large withdrawal
                if amount > 3000:
                    print("⚠️ Large withdrawal detected! Adding to queue for verification.")
                    self.queue.add_customer(f"Verify: {account_number} (${amount:.2f})")
                
            else:
                print("❌ Invalid transaction type!")
                return
                
        except ValueError:
            print("❌ Invalid amount!")
    
    def undo_transaction(self):
        """Undo the last transaction"""
        print("\n" + "-" * 40)
        print("↩️ UNDO LAST TRANSACTION")
        print("-" * 40)
        
        transaction = self.history.pop()
        if transaction:
            print(f"✅ Last transaction undone: {transaction}")
            print("💡 The balance has been restored to previous state.")
    
    def search_customer(self):
        """Search for a customer by account number"""
        print("\n" + "-" * 40)
        print("🔍 SEARCH CUSTOMER")
        print("-" * 40)
        
        account_number = input("Enter account number: ").strip().upper()
        customer = self.database.find_customer(account_number)
        
        if customer:
            print("\n" + "=" * 50)
            print("📋 CUSTOMER INFORMATION")
            print("=" * 50)
            print(f"👤 Name: {customer['name']}")
            print(f"🔢 Account: {account_number}")
            print(f"💰 Balance: ${customer['balance']:.2f}")
            print(f"📅 Joined: {customer['created_at']}")
            print("=" * 50)
        else:
            print(f"❌ Customer with account {account_number} not found!")
            print("💡 Tip: Searching by account number is O(1) with dictionary lookup.")
    
    def show_transaction_history(self):
        """Show transaction history (Stack)"""
        print("\n" + "-" * 40)
        print("📋 TRANSACTION HISTORY (Stack)")
        print("-" * 40)
        print(f"📊 Stack: {self.history}")
        print(f"📝 Total transactions: {self.history.get_size()}")
    
    def show_customer_queue(self):
        """Show customer queue (Queue)"""
        print("\n" + "-" * 40)
        print("👥 CUSTOMER QUEUE (Queue)")
        print("-" * 40)
        queue_list = self.queue.get_queue()
        if queue_list:
            print(f"📊 Customers waiting: {self.queue.get_size()}")
            print("📋 Queue:")
            for i, customer in enumerate(queue_list, 1):
                print(f"  {i}. {customer}")
        else:
            print("📭 No customers in queue.")
    
    def simulate_queue_processing(self):
        """Simulate processing customers from the queue"""
        print("\n" + "-" * 40)
        print("💼 PROCESSING QUEUE")
        print("-" * 40)
        
        if self.queue.get_size() == 0:
            print("📭 No customers to process!")
            return
        
        print(f"📊 Processing {self.queue.get_size()} customers...")
        processed = 0
        while self.queue.get_size() > 0:
            customer = self.queue.serve_customer()
            if customer:
                processed += 1
                time.sleep(0.5)  # Simulate processing time
        
        print(f"✅ Processed {processed} customers!")
        self.history.push(f"Processed {processed} customers from queue")
    
    def show_statistics(self):
        """Show system statistics"""
        print("\n" + "-" * 40)
        print("📊 SYSTEM STATISTICS")
        print("-" * 40)
        print(f"👥 Total customers: {len(self.database.get_all_customers())}")
        print(f"📊 Transactions in history: {self.history.get_size()}")
        print(f"👤 Customers in queue: {self.queue.get_size()}")
        print(f"🔢 Next account number: {self.account_counter}")
        
        # Calculate total balance
        total_balance = sum(c['balance'] for c in self.database.get_all_customers().values())
        print(f"💰 Total balance across all accounts: ${total_balance:.2f}")
    
    def show_menu(self):
        """Display main menu"""
        print("\n" + "=" * 50)
        print("🏦 ADDIS BANK - CUSTOMER SERVICE SIMULATOR")
        print("=" * 50)
        print("1️⃣  Create Customer Account")
        print("2️⃣  Make Transaction")
        print("3️⃣  Undo Last Transaction")
        print("4️⃣  Search Customer by Account")
        print("5️⃣  Show Transaction History (Stack)")
        print("6️⃣  Show Customer Queue (Queue)")
        print("7️⃣  Process Queue")
        print("8️⃣  Show Statistics")
        print("9️⃣  Exit")
        print("=" * 50)
        print("📊 Data Structures Used:")
        print("   - Stack: Transaction History (O(1) push/pop)")
        print("   - Queue: Customer Service (O(1) enqueue/dequeue)")
        print("   - Dictionary: Customer Lookup (O(1) access)")
        print("=" * 50)
    
    def run(self):
        """Main program loop"""
        print("\n👋 Welcome to the Bank Customer Service Simulator!")
        print("💡 Demonstrating Stack, Queue, and Dictionary operations.")
        
        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-9): ").strip()
            
            if choice == "1":
                self.create_customer()
            elif choice == "2":
                self.make_transaction()
            elif choice == "3":
                self.undo_transaction()
            elif choice == "4":
                self.search_customer()
            elif choice == "5":
                self.show_transaction_history()
            elif choice == "6":
                self.show_customer_queue()
            elif choice == "7":
                self.simulate_queue_processing()
            elif choice == "8":
                self.show_statistics()
            elif choice == "9":
                print("\n" + "=" * 50)
                print("👋 Thank you for using Addis Bank!")
                print("=" * 50)
                self.show_statistics()
                print("\n💼 Addis Bank - Your Trusted Partner!")
                print("=" * 50)
                break
            else:
                print("❌ Invalid choice! Please enter 1-9.")

# ============================================
# Run the Program
# ============================================

if __name__ == "__main__":
    simulator = BankServiceSimulator()
    simulator.run()

print("\n" + "=" * 60)
print("🎉 MINI PROJECT COMPLETE!")
print("=" * 60)
