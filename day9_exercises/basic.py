# ============================================
# Day 9 - Basic: Trees, BST, Graphs & Heaps
# ============================================

print("=" * 60)
print("TASK 1: TREE BASICS")
print("=" * 60)

# 1. Tree Basics
class TreeNode:
    """A simple TreeNode class for building hierarchical structures"""
    
    def __init__(self, name, position=""):
        self.name = name
        self.position = position
        self.children = []
    
    def add_child(self, child):
        """Add a child node - O(1)"""
        self.children.append(child)
        return child
    
    def print_tree(self, level=0):
        """Print the tree with indentation - O(n)"""
        indent = "  " * level
        position_info = f" ({self.position})" if self.position else ""
        print(f"{indent}├── {self.name}{position_info}")
        
        for child in self.children:
            child.print_tree(level + 1)

print("\n--- Building Bank Hierarchy Tree ---")
# Build the bank hierarchy
head_office = TreeNode("Head Office", "Main Branch")

# Bole Branch
bole_branch = TreeNode("Bole Branch", "Manager")
head_office.add_child(bole_branch)

# Add employees under Bole Branch
teller1 = TreeNode("Teller 1", "Teller")
teller2 = TreeNode("Teller 2", "Teller")
loan_officer = TreeNode("Loan Officer", "Loan Officer")
bole_branch.add_child(teller1)
bole_branch.add_child(teller2)
bole_branch.add_child(loan_officer)

# Piassa Branch
piassa_branch = TreeNode("Piassa Branch", "Manager")
head_office.add_child(piassa_branch)

# Add employees under Piassa Branch
teller3 = TreeNode("Teller 3", "Teller")
teller4 = TreeNode("Teller 4", "Teller")
piassa_branch.add_child(teller3)
piassa_branch.add_child(teller4)

print("\n🏦 Bank Hierarchy Tree:")
head_office.print_tree()

print("\n💡 Tree Analysis:")
print("  - Root: Head Office")
print("  - Nodes: Branches and Employees")
print("  - Leaves: Tellers and Loan Officers")
print("  - Depth: 3 levels")
print("  - Time Complexity: O(n) to traverse")

print("\n" + "=" * 60)
print("TASK 2: BINARY SEARCH TREE")
print("=" * 60)

# 2. Binary Search Tree
class BSTNode:
    """Node for Binary Search Tree"""
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary Search Tree implementation"""
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert a value into BST - O(log n) average"""
        if self.root is None:
            self.root = BSTNode(value)
            return
        
        self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Helper recursive insert - O(log n) average"""
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        """Search for a value in BST - O(log n) average"""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Helper recursive search - O(log n) average"""
        if node is None:
            return False
        
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def inorder_traversal(self):
        """Inorder traversal - O(n)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper inorder traversal - O(n)"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def print_tree(self):
        """Print BST in a tree format - O(n)"""
        print("\n--- BST Structure ---")
        self._print_recursive(self.root, 0)
    
    def _print_recursive(self, node, level):
        """Helper recursive print - O(n)"""
        if node is None:
            return
        
        self._print_recursive(node.right, level + 1)
        print("  " * level + f"├── {node.value}")
        self._print_recursive(node.left, level + 1)

# Test BST
print("\n--- Creating BST with values: 50, 30, 70, 20, 40, 60 ---")
bst = BinarySearchTree()
values = [50, 30, 70, 20, 40, 60]
for val in values:
    bst.insert(val)

bst.print_tree()
print(f"\n📊 Inorder Traversal: {bst.inorder_traversal()}")

# Search tests
print("\n--- Searching BST ---")
search_values = [40, 100]

for val in search_values:
    found = bst.search(val)
    if found:
        print(f"✅ Found: {val}")
    else:
        print(f"❌ Not Found: {val}")

print("\n💡 BST Analysis:")
print("  - Insert: O(log n) average")
print("  - Search: O(log n) average")
print("  - Inorder Traversal: O(n)")
print("  - Sorted output: Yes (inorder traversal)")

print("\n" + "=" * 60)
print("TASK 3: GRAPH BASICS")
print("=" * 60)

# 3. Graph Basics
class Graph:
    """Simple Graph implementation with adjacency list"""
    
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph - O(1)"""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2, amount=0):
        """Add an edge between two vertices - O(1)"""
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)
        
        self.adjacency_list[vertex1].append({"to": vertex2, "amount": amount})
        self.adjacency_list[vertex2].append({"to": vertex1, "amount": amount})
    
    def get_connections(self, vertex):
        """Get all connections for a vertex - O(1)"""
        return self.adjacency_list.get(vertex, [])
    
    def print_graph(self):
        """Print the graph - O(V + E)"""
        print("\n📊 Customer Money Transfer Network:")
        print("-" * 40)
        
        for vertex, connections in self.adjacency_list.items():
            if connections:
                transfers = []
                for conn in connections:
                    transfers.append(f"{conn['to']} (${conn['amount']})")
                print(f"  {vertex} → {', '.join(transfers)}")
            else:
                print(f"  {vertex} → No connections")
        
        print(f"\n📊 Total Customers: {len(self.adjacency_list)}")
        total_edges = sum(len(conn) for conn in self.adjacency_list.values()) // 2
        print(f"📊 Total Transfers: {total_edges}")

# Build the graph
print("\n--- Building Customer Transfer Network ---")
graph = Graph()

# Add customers (vertices)
customers = ["Almaz", "Dawit", "Tigist", "Hanna"]
for customer in customers:
    graph.add_vertex(customer)

# Add money transfers (edges)
graph.add_edge("Almaz", "Dawit", 500)
graph.add_edge("Almaz", "Tigist", 300)
graph.add_edge("Dawit", "Hanna", 750)
graph.add_edge("Tigist", "Hanna", 200)

# Print the graph
graph.print_graph()

print("\n💡 Graph Analysis:")
print("  - Vertices: Customers")
print("  - Edges: Money transfers")
print("  - Undirected Graph (transfers can be both ways)")
print("  - Time Complexity: O(V + E) to traverse")

print("\n" + "=" * 60)
print("TASK 4: HEAP BASICS")
print("=" * 60)

# 4. Heap Basics
import heapq

print("\n--- Priority Queue for Urgent Transactions ---")
print("Using Python's heapq (Min-Heap by priority number)")

# Create a heap (priority queue)
# Lower number = higher priority
heap = []

# Add urgent transactions
# Format: (priority, description)
transactions = [
    (5000, "Big Loan Request"),
    (200, "Small Deposit"),
    (10000, "Fraud Alert")
]

print("\n📋 Adding transactions:")
for priority, description in transactions:
    heapq.heappush(heap, (priority, description))
    print(f"  Added: Priority {priority} - {description}")

print(f"\n📊 Current heap: {heap}")

# Pop the highest priority item (lowest number)
print("\n--- Processing Transactions ---")
print("📤 Processing highest priority transaction:")

while heap:
    priority, description = heapq.heappop(heap)
    print(f"  ✅ Processing: {description} (Priority: {priority})")
    if heap:
        print(f"  📊 Next in queue: {heap[0][1]} (Priority: {heap[0][0]})")

print("\n💡 Heap Analysis:")
print("  - Priority 1: Highest priority (smallest number)")
print("  - Insert: O(log n)")
print("  - Remove (pop): O(log n)")
print("  - Peek (view top): O(1)")
print("  - Useful for: Emergency transactions, alerts, scheduling")

print("\n" + "=" * 60)
print("BASIC EXERCISES COMPLETE! 🎉")
print("=" * 60)
