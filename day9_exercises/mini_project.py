# ============================================
# DAY 9 MINI PROJECT: Addis Bank Network & Priority System
# ============================================

print("=" * 60)
print("🏦 ADDIS BANK - NETWORK & PRIORITY SYSTEM")
print("=" * 60)
print("Combining Trees, Graphs, and Heaps")
print("=" * 60)

import heapq
from collections import deque

# ============================================
# TREE: Bank Branch Hierarchy
# ============================================

class TreeNode:
    """TreeNode for bank hierarchy - O(1) operations"""
    
    def __init__(self, name, position="", parent=None):
        self.name = name
        self.position = position
        self.parent = parent
        self.children = []
    
    def add_child(self, child):
        """Add a child node - O(1)"""
        child.parent = self
        self.children.append(child)
        return child
    
    def find_node(self, name):
        """Find a node by name - O(n)"""
        if self.name == name:
            return self
        
        for child in self.children:
            result = child.find_node(name)
            if result:
                return result
        return None
    
    def get_depth(self):
        """Get the depth of the node - O(n)"""
        if self.parent is None:
            return 0
        return 1 + self.parent.get_depth()
    
    def print_tree(self, level=0):
        """Print the tree with indentation - O(n)"""
        indent = "  " * level
        position_info = f" ({self.position})" if self.position else ""
        print(f"{indent}├── {self.name}{position_info}")
        
        for child in self.children:
            child.print_tree(level + 1)

# ============================================
# BINARY SEARCH TREE: Customer Accounts
# ============================================

class BSTNode:
    """Node for BST - O(log n) operations"""
    
    def __init__(self, account_number, customer_name):
        self.account_number = account_number
        self.customer_name = customer_name
        self.left = None
        self.right = None

class CustomerBST:
    """BST for customer account lookup - O(log n) average"""
    
    def __init__(self):
        self.root = None
    
    def insert(self, account_number, customer_name):
        """Insert customer account - O(log n) average"""
        if self.root is None:
            self.root = BSTNode(account_number, customer_name)
            return
        
        self._insert_recursive(self.root, account_number, customer_name)
    
    def _insert_recursive(self, node, account_number, customer_name):
        """Helper recursive insert - O(log n) average"""
        if account_number < node.account_number:
            if node.left is None:
                node.left = BSTNode(account_number, customer_name)
            else:
                self._insert_recursive(node.left, account_number, customer_name)
        else:
            if node.right is None:
                node.right = BSTNode(account_number, customer_name)
            else:
                self._insert_recursive(node.right, account_number, customer_name)
    
    def search(self, account_number):
        """Search for customer account - O(log n) average"""
        return self._search_recursive(self.root, account_number)
    
    def _search_recursive(self, node, account_number):
        """Helper recursive search - O(log n) average"""
        if node is None:
            return None
        
        if node.account_number == account_number:
            return node
        elif account_number < node.account_number:
            return self._search_recursive(node.left, account_number)
        else:
            return self._search_recursive(node.right, account_number)
    
    def inorder_traversal(self):
        """Inorder traversal - O(n)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper inorder traversal - O(n)"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append((node.account_number, node.customer_name))
            self._inorder_recursive(node.right, result)

# ============================================
# GRAPH: Customer Money Transfer Network
# ============================================

class CustomerGraph:
    """Graph for customer money transfers - O(1) edge operations"""
    
    def __init__(self):
        self.adjacency_list = {}
    
    def add_customer(self, customer):
        """Add a customer vertex - O(1)"""
        if customer not in self.adjacency_list:
            self.adjacency_list[customer] = []
    
    def add_transfer(self, from_customer, to_customer, amount):
        """Add a money transfer edge - O(1)"""
        if from_customer not in self.adjacency_list:
            self.add_customer(from_customer)
        if to_customer not in self.adjacency_list:
            self.add_customer(to_customer)
        
        self.adjacency_list[from_customer].append({"to": to_customer, "amount": amount})
        self.adjacency_list[to_customer].append({"to": from_customer, "amount": amount})
    
    def get_connections(self, customer):
        """Get all transfers for a customer - O(1)"""
        return self.adjacency_list.get(customer, [])
    
    def bfs(self, start_customer):
        """Breadth-First Search traversal - O(V + E)"""
        if start_customer not in self.adjacency_list:
            return []
        
        visited = set()
        queue = deque([start_customer])
        result = []
        
        while queue:
            customer = queue.popleft()
            if customer not in visited:
                visited.add(customer)
                result.append(customer)
                
                for connection in self.adjacency_list[customer]:
                    if connection["to"] not in visited:
                        queue.append(connection["to"])
        
        return result
    
    def dfs(self, start_customer):
        """Depth-First Search traversal - O(V + E)"""
        if start_customer not in self.adjacency_list:
            return []
        
        visited = set()
        stack = [start_customer]
        result = []
        
        while stack:
            customer = stack.pop()
            if customer not in visited:
                visited.add(customer)
                result.append(customer)
                
                for connection in self.adjacency_list[customer]:
                    if connection["to"] not in visited:
                        stack.append(connection["to"])
        
        return result
    
    def print_graph(self):
        """Print the graph - O(V + E)"""
        print("\n📊 Customer Transfer Network:")
        print("-" * 50)
        
        if not self.adjacency_list:
            print("  No customers in the network")
            return
        
        for customer, connections in self.adjacency_list.items():
            if connections:
                transfers = []
                for conn in connections:
                    transfers.append(f"{conn['to']} (${conn['amount']})")
                print(f"  {customer} → {', '.join(transfers)}")
            else:
                print(f"  {customer} → No transfers")
        
        total_transfers = sum(len(conn) for conn in self.adjacency_list.values()) // 2
        print(f"\n📊 Total Customers: {len(self.adjacency_list)}")
        print(f"📊 Total Transfers: {total_transfers}")

# ============================================
# HEAP: Priority Queue for Urgent Transactions
# ============================================

class PriorityQueue:
    """Priority queue for urgent transactions - O(log n) operations"""
    
    def __init__(self):
        self.heap = []
        self.counter = 0
    
    def add_transaction(self, priority, description, customer=""):
        """Add urgent transaction - O(log n)"""
        # Lower priority number = higher priority
        heapq.heappush(self.heap, (priority, self.counter, description, customer))
        self.counter += 1
        print(f"✅ Added: Priority {priority} - {description} {f'({customer})' if customer else ''}")
    
    def process_highest_priority(self):
        """Process highest priority transaction - O(log n)"""
        if not self.heap:
            print("❌ No urgent transactions to process!")
            return None
        
        priority, _, description, customer = heapq.heappop(self.heap)
        print(f"\n🚨 Processing: {description} (Priority: {priority}) {f'({customer})' if customer else ''}")
        return (priority, description, customer)
    
    def peek(self):
        """View highest priority without removing - O(1)"""
        if not self.heap:
            return None
        priority, _, description, customer = self.heap[0]
        return (priority, description, customer)
    
    def get_queue(self):
        """Get all transactions sorted by priority - O(n log n)"""
        return sorted(self.heap, key=lambda x: x[0])
    
    def is_empty(self):
        """Check if queue is empty - O(1)"""
        return len(self.heap) == 0

# ============================================
# MAIN SYSTEM
# ============================================

class AddisBankNetwork:
    def __init__(self):
        self.tree = None
        self.bst = CustomerBST()
        self.graph = CustomerGraph()
        self.priority_queue = PriorityQueue()
        self._initialize_data()
    
    def _initialize_data(self):
        """Initialize with sample data"""
        print("\n📊 Initializing Bank Network...")
        
        # Build tree
        self.tree = TreeNode("Head Office", "Main Branch")
        bole = self.tree.add_child(TreeNode("Bole Branch", "Manager"))
        piassa = self.tree.add_child(TreeNode("Piassa Branch", "Manager"))
        
        bole.add_child(TreeNode("Teller 1", "Teller"))
        bole.add_child(TreeNode("Teller 2", "Teller"))
        bole.add_child(TreeNode("Loan Officer", "Loan Officer"))
        
        piassa.add_child(TreeNode("Teller 3", "Teller"))
        piassa.add_child(TreeNode("Teller 4", "Teller"))
        
        # Add customers to BST
        customers = [
            (1001, "Almaz"),
            (1002, "Dawit"),
            (1003, "Tigist"),
            (1004, "Hanna"),
            (1005, "Kebede")
        ]
        for acc_num, name in customers:
            self.bst.insert(acc_num, name)
            self.graph.add_customer(name)
        
        # Add transfers to graph
        self.graph.add_transfer("Almaz", "Dawit", 500)
        self.graph.add_transfer("Almaz", "Tigist", 300)
        self.graph.add_transfer("Dawit", "Hanna", 750)
        self.graph.add_transfer("Tigist", "Hanna", 200)
        self.graph.add_transfer("Kebede", "Almaz", 1000)
        
        print("✅ Initialization complete!\n")
    
    # ============================================
    # TREE OPERATIONS
    # ============================================
    
    def add_branch_or_employee(self):
        """Add a new branch or employee to the tree"""
        print("\n" + "-" * 40)
        print("🌳 ADD BRANCH / EMPLOYEE")
        print("-" * 40)
        
        if not self.tree:
            print("❌ Tree not initialized!")
            return
        
        print("Current tree:")
        self.tree.print_tree()
        
        parent_name = input("\nEnter parent node name: ").strip()
        parent_node = self.tree.find_node(parent_name)
        
        if not parent_node:
            print(f"❌ Node '{parent_name}' not found!")
            return
        
        name = input("Enter new node name: ").strip()
        if not name:
            print("❌ Name cannot be empty!")
            return
        
        position = input("Enter position (optional): ").strip()
        
        new_node = TreeNode(name, position)
        parent_node.add_child(new_node)
        
        print(f"✅ Added '{name}' under '{parent_name}'")
    
    def show_organization_tree(self):
        """Display the bank hierarchy"""
        print("\n" + "-" * 40)
        print("🏛️  BANK HIERARCHY TREE")
        print("-" * 40)
        
        if not self.tree:
            print("❌ Tree not initialized!")
            return
        
        print("\nTime Complexity: O(n) - visits all nodes")
        self.tree.print_tree()
    
    # ============================================
    # BST OPERATIONS
    # ============================================
    
    def search_customer_account(self):
        """Search for a customer in BST"""
        print("\n" + "-" * 40)
        print("🔍 SEARCH CUSTOMER ACCOUNT (BST)")
        print("-" * 40)
        
        try:
            account_number = int(input("Enter account number: "))
        except ValueError:
            print("❌ Invalid account number!")
            return
        
        print(f"\nTime Complexity: O(log n) average")
        result = self.bst.search(account_number)
        
        if result:
            print(f"✅ Customer Found:")
            print(f"  Account Number: {result.account_number}")
            print(f"  Customer Name: {result.customer_name}")
        else:
            print(f"❌ Account {account_number} not found!")
    
    def show_all_accounts(self):
        """Display all accounts (inorder traversal)"""
        print("\n" + "-" * 40)
        print("📋 ALL CUSTOMER ACCOUNTS")
        print("-" * 40)
        
        accounts = self.bst.inorder_traversal()
        
        if not accounts:
            print("❌ No accounts found!")
            return
        
        print("\nTime Complexity: O(n) - inorder traversal")
        print("\nAccount Number | Customer Name")
        print("-" * 30)
        for acc_num, name in accounts:
            print(f"{acc_num:<14} | {name}")

    # ============================================
    # GRAPH OPERATIONS
    # ============================================
    
    def add_money_transfer(self):
        """Add a money transfer connection in the graph"""
        print("\n" + "-" * 40)
        print("💸 ADD MONEY TRANSFER")
        print("-" * 40)
        
        from_customer = input("From customer: ").strip()
        to_customer = input("To customer: ").strip()
        
        try:
            amount = float(input("Amount: $"))
            if amount <= 0:
                print("❌ Amount must be positive!")
                return
        except ValueError:
            print("❌ Invalid amount!")
            return
        
        # Check if customers exist in graph
        if from_customer not in self.graph.adjacency_list:
            print(f"⚠️ '{from_customer}' not found in network. Adding as new customer.")
            self.graph.add_customer(from_customer)
            self.bst.insert(1000 + len(self.graph.adjacency_list), from_customer)
        
        if to_customer not in self.graph.adjacency_list:
            print(f"⚠️ '{to_customer}' not found in network. Adding as new customer.")
            self.graph.add_customer(to_customer)
            self.bst.insert(1000 + len(self.graph.adjacency_list), to_customer)
        
        self.graph.add_transfer(from_customer, to_customer, amount)
        print(f"✅ Transfer of ${amount:.2f} added from {from_customer} to {to_customer}")
    
    def show_all_connections(self):
        """Display the entire transfer network"""
        print("\n" + "-" * 40)
        print("🌐 CUSTOMER TRANSFER NETWORK")
        print("-" * 40)
        
        print("\nTime Complexity: O(V + E) - visits all vertices and edges")
        self.graph.print_graph()
    
    def bfs_traversal(self):
        """BFS traversal of the graph"""
        print("\n" + "-" * 40)
        print("🔍 BFS TRAVERSAL")
        print("-" * 40)
        
        if not self.graph.adjacency_list:
            print("❌ No customers in network!")
            return
        
        start = input("Enter starting customer: ").strip()
        
        print("\nTime Complexity: O(V + E)")
        result = self.graph.bfs(start)
        
        if result:
            print(f"✅ BFS starting from {start}:")
            print(f"  {' → '.join(result)}")
        else:
            print(f"❌ Customer '{start}' not found!")
    
    def dfs_traversal(self):
        """DFS traversal of the graph"""
        print("\n" + "-" * 40)
        print("🔍 DFS TRAVERSAL")
        print("-" * 40)
        
        if not self.graph.adjacency_list:
            print("❌ No customers in network!")
            return
        
        start = input("Enter starting customer: ").strip()
        
        print("\nTime Complexity: O(V + E)")
        result = self.graph.dfs(start)
        
        if result:
            print(f"✅ DFS starting from {start}:")
            print(f"  {' → '.join(result)}")
        else:
            print(f"❌ Customer '{start}' not found!")

    # ============================================
    # HEAP OPERATIONS
    # ============================================
    
    def add_urgent_transaction(self):
        """Add an urgent transaction to the priority queue"""
        print("\n" + "-" * 40)
        print("🚨 ADD URGENT TRANSACTION")
        print("-" * 40)
        
        description = input("Enter transaction description: ").strip()
        if not description:
            print("❌ Description cannot be empty!")
            return
        
        try:
            priority = int(input("Enter priority (1-100, lower = higher priority): "))
            if priority < 1 or priority > 100:
                print("❌ Priority must be between 1-100!")
                return
        except ValueError:
            print("❌ Invalid priority!")
            return
        
        customer = input("Enter customer name (optional): ").strip()
        
        print("\nTime Complexity: O(log n)")
        self.priority_queue.add_transaction(priority, description, customer)
    
    def process_urgent_transaction(self):
        """Process the highest priority transaction"""
        print("\n" + "-" * 40)
        print("🚨 PROCESS URGENT TRANSACTION")
        print("-" * 40)
        
        if self.priority_queue.is_empty():
            print("❌ No urgent transactions to process!")
            return
        
        print("\nTime Complexity: O(log n)")
        result = self.priority_queue.process_highest_priority()
        
        if result:
            priority, description, customer = result
            # Log to graph
            if customer and customer in self.graph.adjacency_list:
                print(f"📊 Logged to network: {customer}'s urgent transaction")
    
    def view_urgent_queue(self):
        """View all urgent transactions"""
        print("\n" + "-" * 40)
        print("📋 URGENT TRANSACTION QUEUE")
        print("-" * 40)
        
        if self.priority_queue.is_empty():
            print("❌ No urgent transactions in queue!")
            return
        
        print("\nTime Complexity: O(n log n)")
        queue = self.priority_queue.get_queue()
        print("\nPriority | Description")
        print("-" * 40)
        for priority, _, description, customer in queue:
            print(f"{priority:<8} | {description} {f'({customer})' if customer else ''}")

    # ============================================
    # MENU SYSTEM
    # ============================================
    
    def show_menu(self):
        print("\n" + "=" * 50)
        print("🏦 ADDIS BANK NETWORK & PRIORITY SYSTEM")
        print("=" * 50)
        print("1️⃣  Show Organization Tree")
        print("2️⃣  Add Branch / Employee")
        print("3️⃣  Search Customer Account (BST)")
        print("4️⃣  Show All Accounts")
        print("5️⃣  Add Money Transfer (Graph)")
        print("6️⃣  Show Transfer Network")
        print("7️⃣  BFS Traversal")
        print("8️⃣  DFS Traversal")
        print("9️⃣  Add Urgent Transaction (Heap)")
        print("🔟 Process Urgent Transaction")
        print("1️⃣1️⃣ View Urgent Queue")
        print("0️⃣  Exit")
        print("=" * 50)
        print("📊 Data Structures:")
        print("  - Tree: Bank Hierarchy (O(n) traversal)")
        print("  - BST: Customer Accounts (O(log n) search)")
        print("  - Graph: Transfer Network (O(V+E) traversal)")
        print("  - Heap: Urgent Transactions (O(log n) insert/pop)")
        print("=" * 50)
    
    def run(self):
        while True:
            self.show_menu()
            choice = input("\nEnter your choice: ").strip()
            
            if choice == "1":
                self.show_organization_tree()
            elif choice == "2":
                self.add_branch_or_employee()
            elif choice == "3":
                self.search_customer_account()
            elif choice == "4":
                self.show_all_accounts()
            elif choice == "5":
                self.add_money_transfer()
            elif choice == "6":
                self.show_all_connections()
            elif choice == "7":
                self.bfs_traversal()
            elif choice == "8":
                self.dfs_traversal()
            elif choice == "9":
                self.add_urgent_transaction()
            elif choice == "10":
                self.process_urgent_transaction()
            elif choice == "11":
                self.view_urgent_queue()
            elif choice == "0":
                print("\n" + "=" * 50)
                print("👋 Thank you for using Addis Bank Network System!")
                print("=" * 50)
                
                # Final summary
                print("\n📊 Final Statistics:")
                print("-" * 30)
                print(f"🏛️  Branches: Count all nodes in tree")
                print(f"👥 Customers: {len(self.graph.adjacency_list)}")
                print(f"💸 Transfers: {sum(len(conn) for conn in self.graph.adjacency_list.values()) // 2}")
                print(f"🚨 Urgent Transactions: {len(self.priority_queue.heap)}")
                print("\n💼 Addis Bank - Your Trusted Partner!")
                print("=" * 50)
                break
            else:
                print("❌ Invalid choice! Please enter 0-11.")

# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
    system = AddisBankNetwork()
    system.run()

print("\n" + "=" * 60)
print("🎉 MINI PROJECT COMPLETE!")
print("=" * 60)
