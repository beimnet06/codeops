
print("=" * 60)
print("TASK 1: TREE BASICS")
print("=" * 60)

class TreeNode:
    
    def __init__(self, name, position=""):
        self.name = name
        self.position = position
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        return child
    
    def print_tree(self, level=0):
        indent = "  " * level
        position_info = f" ({self.position})" if self.position else ""
        print(f"{indent}├── {self.name}{position_info}")
        
        for child in self.children:
            child.print_tree(level + 1)

print("\n--- Building Bank Hierarchy Tree ---")
head_office = TreeNode("Head Office", "Main Branch")

bole_branch = TreeNode("Bole Branch", "Manager")
head_office.add_child(bole_branch)

teller1 = TreeNode("Teller 1", "Teller")
teller2 = TreeNode("Teller 2", "Teller")
loan_officer = TreeNode("Loan Officer", "Loan Officer")
bole_branch.add_child(teller1)
bole_branch.add_child(teller2)
bole_branch.add_child(loan_officer)

piassa_branch = TreeNode("Piassa Branch", "Manager")
head_office.add_child(piassa_branch)

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

class BSTNode:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
            return
        
        self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
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
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None:
            return False
        
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def print_tree(self):
        print("\n--- BST Structure ---")
        self._print_recursive(self.root, 0)
    
    def _print_recursive(self, node, level):
        if node is None:
            return
        
        self._print_recursive(node.right, level + 1)
        print("  " * level + f"├── {node.value}")
        self._print_recursive(node.left, level + 1)

print("\n--- Creating BST with values: 50, 30, 70, 20, 40, 60 ---")
bst = BinarySearchTree()
values = [50, 30, 70, 20, 40, 60]
for val in values:
    bst.insert(val)

bst.print_tree()
print(f"\n📊 Inorder Traversal: {bst.inorder_traversal()}")

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

class Graph:
    
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2, amount=0):
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)
        
        self.adjacency_list[vertex1].append({"to": vertex2, "amount": amount})
        self.adjacency_list[vertex2].append({"to": vertex1, "amount": amount})
    
    def get_connections(self, vertex):
        return self.adjacency_list.get(vertex, [])
    
    def print_graph(self):
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

print("\n--- Building Customer Transfer Network ---")
graph = Graph()

customers = ["Almaz", "Dawit", "Tigist", "Hanna"]
for customer in customers:
    graph.add_vertex(customer)

graph.add_edge("Almaz", "Dawit", 500)
graph.add_edge("Almaz", "Tigist", 300)
graph.add_edge("Dawit", "Hanna", 750)
graph.add_edge("Tigist", "Hanna", 200)

graph.print_graph()

print("\n💡 Graph Analysis:")
print("  - Vertices: Customers")
print("  - Edges: Money transfers")
print("  - Undirected Graph (transfers can be both ways)")
print("  - Time Complexity: O(V + E) to traverse")

print("\n" + "=" * 60)
print("TASK 4: HEAP BASICS")
print("=" * 60)

import heapq

print("\n--- Priority Queue for Urgent Transactions ---")
print("Using Python's heapq (Min-Heap by priority number)")

heap = []

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
