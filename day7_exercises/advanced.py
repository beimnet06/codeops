# ============================================
# Day 7 - Advanced: Performance Comparison & Data Structure Selection
# ============================================

print("=" * 60)
print("TASK 9: PERFORMANCE COMPARISON")
print("=" * 60)

import time
from collections import deque
import random

# 9. Performance Comparison
print("\n--- Comparing Search Performance: List vs Dictionary ---")

def time_search():
    """Compare search time between list and dictionary"""
    
    # Create data
    size = 10000
    data_list = list(range(size))
    data_dict = {i: f"value_{i}" for i in range(size)}
    
    # Search for random items
    search_items = random.sample(range(size), 1000)
    
    # List search (O(n))
    start_time = time.time()
    for item in search_items:
        _ = item in data_list
    list_time = time.time() - start_time
    
    # Dictionary search (O(1))
    start_time = time.time()
    for item in search_items:
        _ = item in data_dict
    dict_time = time.time() - start_time
    
    print(f"📊 Search Performance (n={size}):")
    print(f"  List search (O(n)): {list_time:.6f} seconds")
    print(f"  Dictionary search (O(1)): {dict_time:.6f} seconds")
    
    # Avoid division by zero
    if dict_time > 0:
        print(f"  Dictionary is {list_time/dict_time:.2f}x faster!")
    else:
        print(f"  Dictionary is significantly faster (almost instant)!")

time_search()

print("\n--- Comparing Insertion Performance: List vs Deque ---")

def time_insertion():
    """Compare insertion at beginning between list and deque"""
    
    size = 10000
    
    # List insertion at beginning (O(n))
    start_time = time.time()
    my_list = []
    for i in range(size):
        my_list.insert(0, i)
    list_time = time.time() - start_time
    
    # Deque insertion at beginning (O(1))
    start_time = time.time()
    my_deque = deque()
    for i in range(size):
        my_deque.appendleft(i)
    deque_time = time.time() - start_time
    
    print(f"\n📊 Insertion Performance (n={size}):")
    print(f"  List insert at beginning (O(n)): {list_time:.6f} seconds")
    print(f"  Deque appendleft (O(1)): {deque_time:.6f} seconds")
    
    if deque_time > 0:
        print(f"  Deque is {list_time/deque_time:.2f}x faster!")
    else:
        print(f"  Deque is significantly faster (almost instant)!")

time_insertion()

print("\n" + "=" * 60)
print("TASK 10: CHOOSE THE RIGHT STRUCTURE")
print("=" * 60)

print("""
🔍 Data Structure Selection Guide:

Scenario 1: Checking if a username is already taken
✅ Best Choice: Dictionary (Set or Dict)
📊 Justification: O(1) average lookup time
💡 Implementation: 
   - usernames = set()  # Fast membership test
   - if username in usernames:  # O(1)

Scenario 2: Processing tasks in the order they arrive (customer support)
✅ Best Choice: Queue (FIFO)
📊 Justification: O(1) enqueue and dequeue
💡 Implementation:
   - from collections import deque
   - tasks.append(task)  # Add to end
   - task = tasks.popleft()  # Remove from front

Scenario 3: Implementing "Undo" feature in a text editor
✅ Best Choice: Stack (LIFO)
📊 Justification: O(1) push and pop operations
💡 Implementation:
   - undo_stack.append(action)  # Save action
   - last_action = undo_stack.pop()  # Undo last

Scenario 4: Storing student IDs for fast lookup
✅ Best Choice: Dictionary or Set
📊 Justification: O(1) average lookup time
💡 Implementation:
   - student_ids = {}  # id -> student_data
   - if student_id in student_ids:  # Fast O(1)
""")

print("\n" + "=" * 60)
print("TASK 11: LINKED LIST VS ARRAY")
print("=" * 60)

# 11. Linked List vs Array
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListWithRemove:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data):
        new_node = LinkedListNode(data)
        self.size += 1
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def remove_middle(self):
        """Remove the middle element - O(n)"""
        if self.head is None:
            return None
        
        if self.size == 1:
            data = self.head.data
            self.head = None
            self.size = 0
            return data
        
        middle_index = self.size // 2
        
        if middle_index == 0:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data
        
        current = self.head
        prev = None
        for i in range(middle_index):
            prev = current
            current = current.next
        
        data = current.data
        prev.next = current.next
        self.size -= 1
        return data
    
    def to_list(self):
        """Convert linked list to Python list for display"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

def remove_middle_from_list(py_list):
    """Remove middle element from Python list - O(n)"""
    if not py_list:
        return None
    
    middle_index = len(py_list) // 2
    return py_list.pop(middle_index)

print("\n--- Testing Array (Python List) ---")
array = [1, 2, 3, 4, 5, 6, 7]
print(f"Original array: {array}")
removed = remove_middle_from_list(array)
print(f"Removed: {removed}")
print(f"After removal: {array}")

print("\n--- Testing Linked List ---")
ll = LinkedListWithRemove()
for i in range(1, 8):
    ll.append(i)
print(f"Original linked list: {ll.to_list()}")
removed = ll.remove_middle()
print(f"Removed: {removed}")
print(f"After removal: {ll.to_list()}")

print("""
📊 Trade-offs: Linked List vs Array

| Operation | Array (Python List) | Linked List |
|-----------|-------------------|-------------|
| Access by index | O(1) ✅ | O(n) ❌ |
| Insert at end | O(1) ✅ | O(1) if tail tracked |
| Insert at beginning | O(n) ❌ | O(1) ✅ |
| Remove middle | O(n) | O(n) |
| Memory | Contiguous | Scattered |
| Cache efficiency | High ✅ | Low ❌ |

💡 When to use:
- Array: When you need fast random access
- Linked List: When you need fast insertions/deletions at ends
""")

print("\n" + "=" * 60)
print("ADVANCED EXERCISES COMPLETE! 🎉")
print("=" * 60)
