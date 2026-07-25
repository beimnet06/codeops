# ============================================
# DAY 8 MINI PROJECT: Bank Transaction Analyzer
# ============================================

print("=" * 60)
print("🏦 ADDIS BANK - TRANSACTION ANALYZER")
print("=" * 60)
print("Demonstrating Recursion, Searching & Sorting")
print("=" * 60)

import time
import random
from datetime import datetime, timedelta

# ============================================
# Data Generation
# ============================================

class Transaction:
    """Transaction class with amount, date, and type"""
    
    def __init__(self, amount, date, type):
        self.amount = amount
        self.date = date
        self.type = type  # 'deposit' or 'withdrawal'
    
    def __str__(self):
        return f"{self.date}: {self.type} ${self.amount:.2f}"

class BankTransactionAnalyzer:
    def __init__(self):
        self.transactions = []
        self._generate_sample_data()
    
    def _generate_sample_data(self):
        """Generate sample transactions for testing"""
        print("📊 Generating sample transactions...")
        
        types = ['deposit', 'withdrawal']
        start_date = datetime.now() - timedelta(days=30)
        
        for i in range(20):
            amount = round(random.uniform(50, 5000), 2)
            type = random.choice(types)
            date = start_date + timedelta(days=random.randint(0, 30))
            
            # Balance should never go negative for deposits
            if type == 'withdrawal' and amount > 2000:
                amount = round(random.uniform(50, 1000), 2)
            
            self.transactions.append(Transaction(amount, date.strftime("%Y-%m-%d"), type))
        
        print(f"✅ Generated {len(self.transactions)} transactions")
    
    # ============================================
    # Recursive Functions
    # ============================================
    
    def calculate_total_balance_recursive(self, transactions=None):
        """Calculate total balance using recursion - O(n)"""
        if transactions is None:
            transactions = self.transactions
        
        if not transactions:
            return 0
        
        # Base case: single transaction
        if len(transactions) == 1:
            return transactions[0].amount if transactions[0].type == 'deposit' else -transactions[0].amount
        
        # Recursive case: first + rest
        first = transactions[0]
        first_amount = first.amount if first.type == 'deposit' else -first.amount
        return first_amount + self.calculate_total_balance_recursive(transactions[1:])
    
    def get_transactions_above_threshold(self, threshold, transactions=None):
        """Recursively get transactions above threshold - O(n)"""
        if transactions is None:
            transactions = self.transactions
        
        if not transactions:
            return []
        
        # Recursive case: check first + rest
        first = transactions[0]
        rest = self.get_transactions_above_threshold(threshold, transactions[1:])
        
        if abs(first.amount) >= threshold:
            return [first] + rest
        return rest
    
    # ============================================
    # Sorting Functions
    # ============================================
    
    def sort_by_amount(self, ascending=True):
        """Sort transactions by amount using Bubble Sort - O(n²)"""
        arr = self.transactions.copy()
        n = len(arr)
        comparison_count = 0
        swap_count = 0
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                comparison_count += 1
                if ascending:
                    condition = arr[j].amount > arr[j + 1].amount
                else:
                    condition = arr[j].amount < arr[j + 1].amount
                
                if condition:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swap_count += 1
                    swapped = True
            
            if not swapped:
                break
        
        print(f"📊 Sort by Amount ({'Ascending' if ascending else 'Descending'}):")
        print(f"  Comparisons: {comparison_count}")
        print(f"  Swaps: {swap_count}")
        return arr
    
    def sort_by_date(self, ascending=True):
        """Sort transactions by date using Bubble Sort - O(n²)"""
        arr = self.transactions.copy()
        n = len(arr)
        comparison_count = 0
        swap_count = 0
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                comparison_count += 1
                if ascending:
                    condition = arr[j].date > arr[j + 1].date
                else:
                    condition = arr[j].date < arr[j + 1].date
                
                if condition:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swap_count += 1
                    swapped = True
            
            if not swapped:
                break
        
        print(f"📊 Sort by Date ({'Ascending' if ascending else 'Descending'}):")
        print(f"  Comparisons: {comparison_count}")
        print(f"  Swaps: {swap_count}")
        return arr
    
    # ============================================
    # Search Functions
    # ============================================
    
    def linear_search_by_amount(self, target):
        """Search for transactions with specific amount using Linear Search - O(n)"""
        print(f"\n🔍 Linear Search for Amount: ${target:.2f}")
        print("-" * 40)
        
        found = []
        for i, transaction in enumerate(self.transactions):
            if abs(transaction.amount - target) < 0.01:  # Floating point comparison
                found.append((i, transaction))
        
        if found:
            print(f"✅ Found {len(found)} transaction(s):")
            for idx, trans in found:
                print(f"  [{idx}] {trans}")
        else:
            print(f"❌ No transactions found with amount ${target:.2f}")
        
        return found
    
    def binary_search_by_amount(self, target):
        """Search for transactions with specific amount using Binary Search - O(log n)"""
        print(f"\n🔍 Binary Search for Amount: ${target:.2f}")
        print("-" * 40)
        
        # Need sorted array for binary search
        sorted_transactions = self.sort_by_amount(ascending=True)
        
        left = 0
        right = len(sorted_transactions) - 1
        found = []
        
        while left <= right:
            mid = (left + right) // 2
            
            if abs(sorted_transactions[mid].amount - target) < 0.01:
                # Found one, check neighbors for duplicates
                found.append(sorted_transactions[mid])
                
                # Check left neighbors
                i = mid - 1
                while i >= 0 and abs(sorted_transactions[i].amount - target) < 0.01:
                    found.append(sorted_transactions[i])
                    i -= 1
                
                # Check right neighbors
                i = mid + 1
                while i < len(sorted_transactions) and abs(sorted_transactions[i].amount - target) < 0.01:
                    found.append(sorted_transactions[i])
                    i += 1
                
                break
            
            elif sorted_transactions[mid].amount < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if found:
            print(f"✅ Found {len(found)} transaction(s):")
            for trans in found:
                print(f"  {trans}")
        else:
            print(f"❌ No transactions found with amount ${target:.2f}")
        
        return found
    
    # ============================================
    # Display Functions
    # ============================================
    
    def display_transactions(self, transactions=None):
        """Display transactions in a readable format"""
        if transactions is None:
            transactions = self.transactions
        
        if not transactions:
            print("📭 No transactions to display")
            return
        
        print("\n📋 Transaction List:")
        print("-" * 50)
        print(f"{'#':<4} {'Date':<12} {'Type':<12} {'Amount':<10}")
        print("-" * 50)
        
        for i, trans in enumerate(transactions, 1):
            emoji = "📈" if trans.type == 'deposit' else "📉"
            print(f"{i:<4} {trans.date:<12} {trans.type:<12} ${trans.amount:<10.2f} {emoji}")
        
        print("-" * 50)
        print(f"Total: {len(transactions)} transactions")
    
    def display_summary(self):
        """Display summary statistics"""
        total_balance = self.calculate_total_balance_recursive()
        
        deposits = [t for t in self.transactions if t.type == 'deposit']
        withdrawals = [t for t in self.transactions if t.type == 'withdrawal']
        
        total_deposits = sum(t.amount for t in deposits)
        total_withdrawals = sum(t.amount for t in withdrawals)
        
        print("\n📊 SUMMARY STATISTICS")
        print("=" * 40)
        print(f"💰 Total Balance: ${total_balance:.2f}")
        print(f"📈 Total Deposits: ${total_deposits:.2f}")
        print(f"📉 Total Withdrawals: ${total_withdrawals:.2f}")
        print(f"📝 Total Transactions: {len(self.transactions)}")
        print(f"  - Deposits: {len(deposits)}")
        print(f"  - Withdrawals: {len(withdrawals)}")
        
        # Find largest and smallest
        if self.transactions:
            max_trans = max(self.transactions, key=lambda x: abs(x.amount))
            min_trans = min(self.transactions, key=lambda x: abs(x.amount))
            print(f"📈 Largest: ${abs(max_trans.amount):.2f} ({max_trans.type})")
            print(f"📉 Smallest: ${abs(min_trans.amount):.2f} ({min_trans.type})")
    
    def generate_report(self, threshold=1000):
        """Recursive report of transactions above threshold"""
        print(f"\n📋 RECURSIVE REPORT: Transactions above ${threshold:.2f}")
        print("-" * 40)
        
        high_value = self.get_transactions_above_threshold(threshold)
        
        if high_value:
            print(f"✅ Found {len(high_value)} high-value transactions:")
            for trans in high_value:
                print(f"  {trans}")
        else:
            print(f"❌ No transactions above ${threshold:.2f}")

# ============================================
# Main Menu
# ============================================

def main():
    """Main program loop"""
    analyzer = BankTransactionAnalyzer()
    
    print("\n👋 Welcome to the Addis Bank Transaction Analyzer!")
    print("Demonstrating Recursion, Searching & Sorting")
    
    while True:
        print("\n" + "=" * 50)
        print("🏦 TRANSACTION ANALYZER - MENU")
        print("=" * 50)
        print("1️⃣  Display All Transactions")
        print("2️⃣  Show Summary")
        print("3️⃣  Sort by Amount (Ascending)")
        print("4️⃣  Sort by Amount (Descending)")
        print("5️⃣  Sort by Date (Ascending)")
        print("6️⃣  Sort by Date (Descending)")
        print("7️⃣  Linear Search by Amount")
        print("8️⃣  Binary Search by Amount")
        print("9️⃣  Recursive Report (Above Threshold)")
        print("0️⃣  Exit")
        print("=" * 50)
        
        choice = input("\nEnter your choice (0-9): ").strip()
        
        if choice == "1":
            analyzer.display_transactions()
        
        elif choice == "2":
            analyzer.display_summary()
        
        elif choice == "3":
            sorted_trans = analyzer.sort_by_amount(ascending=True)
            analyzer.display_transactions(sorted_trans)
        
        elif choice == "4":
            sorted_trans = analyzer.sort_by_amount(ascending=False)
            analyzer.display_transactions(sorted_trans)
        
        elif choice == "5":
            sorted_trans = analyzer.sort_by_date(ascending=True)
            analyzer.display_transactions(sorted_trans)
        
        elif choice == "6":
            sorted_trans = analyzer.sort_by_date(ascending=False)
            analyzer.display_transactions(sorted_trans)
        
        elif choice == "7":
            try:
                target = float(input("Enter amount to search: $"))
                analyzer.linear_search_by_amount(target)
            except ValueError:
                print("❌ Invalid amount!")
        
        elif choice == "8":
            try:
                target = float(input("Enter amount to search: $"))
                analyzer.binary_search_by_amount(target)
            except ValueError:
                print("❌ Invalid amount!")
        
        elif choice == "9":
            try:
                threshold = float(input("Enter threshold amount: $"))
                analyzer.generate_report(threshold)
            except ValueError:
                print("❌ Invalid amount!")
        
        elif choice == "0":
            print("\n" + "=" * 50)
            print("👋 Thank you for using the Transaction Analyzer!")
            print("=" * 50)
            analyzer.display_summary()
            print("\n💼 Addis Bank - Your Trusted Partner!")
            print("=" * 50)
            break
        
        else:
            print("❌ Invalid choice! Please enter 0-9.")

if __name__ == "__main__":
    main()

print("\n" + "=" * 60)
print("🎉 MINI PROJECT COMPLETE!")
print("=" * 60)
