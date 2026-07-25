# ============================================
# Day 7 - Intermediate: Big-O Analysis, Linked Lists, Stack & Queue
# ============================================

print("=" * 60)
print("TASK 5: BIG-O ANALYSIS")
print("=" * 60)

import time

# 5. Big-O Analysis
print("\n--- Function 1: Find Maximum in List ---")
print("Time Complexity: O(n) - Linear time")

def find_max(numbers):
    """Find the maximum number in a list - O(n)"""
    if not numbers:
        return None
    
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Test the function
test_list = [3, 7, 2, 9, 1, 5, 8]
print(f"List: {test_list}")
print(f"Maximum: {find_max(test_list)}")

print("\n--- Function 2: Nested Loops ---")
print("Time Complexity: O(n²) - Quadratic time")

def find_duplicates(numbers):
    """Find duplicates using nested loops - O(n²)"""
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j] and numbers[i] not in duplicates:
                duplicates.append(numbers[i])
    return duplicates

# Test the function
test_list2 = [1, 2, 3, 2, 4, 5, 3, 6, 7, 1]
print(f"List: {test_list2}")
print(f"Duplicates: {find_duplicates(test_list2)}")

print("\n💡 Analysis:")
print("  find_max(): O(n) - Single loop")
print("  find_duplicates(): O(n²) - Nested loops")

print("\n" + "=" * 60)
print("TASK 6: LINKED LIST BASICS")
print("=" * 60)

# 6. Linked List Basics
class Node:
    """A simple Node class for linked list"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    """A simple LinkedList class"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, value):
        """Add a value to the end of the list - O(n)"""
        new_node = Node(value)
        self.size += 1
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def print_list(self):
        """Print all values in the list - O(n)"""
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        values = []
        while current:
            values.append(str(current.data))
            current = current.next
        print(" -> ".join(values))
    
    def get_size(self):
        """Return the size of the list - O(1)"""
        return self.size

print("\n--- Creating a Linked List ---")
my_list = LinkedList()

print("Appending values: 10, 20, 30, 40")
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("Linked List contents:")
my_list.print_list()
print(f"List size: {my_list.get_size()}")

print("\n" + "=" * 60)
print("TASK 7: STACK (LIFO)")
print("=" * 60)

# 7. Stack (LIFO)
class Stack:
    """A simple Stack implementation using a list"""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to the top of stack - O(1)"""
        self.items.append(item)
        print(f"✅ Pushed: {item}")
    
    def pop(self):
        """Remove and return item from the top - O(1)"""
        if self.is_empty():
            print("❌ Stack is empty!")
            return None
        item = self.items.pop()
        print(f"✅ Popped: {item}")
        return item
    
    def peek(self):
        """Return top item without removing - O(1)"""
        if self.is_empty():
            print("❌ Stack is empty!")
            return None
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty - O(1)"""
        return len(self.items) == 0
    
    def get_size(self):
        """Return the size of the stack - O(1)"""
        return len(self.items)
    
    def __str__(self):
        """String representation of the stack"""
        return f"Stack: {self.items}"

print("\n--- Reversing a String using Stack ---")

def reverse_string(text):
    """Reverse a string using a stack"""
    stack = Stack()
    
    # Push all characters onto the stack
    for char in text:
        stack.push(char)
    
    # Pop all characters to reverse
    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()
    
    return reversed_text

original = "Addis Ababa"
print(f"\nOriginal: {original}")
reversed_str = reverse_string(original)
print(f"Reversed: {reversed_str}")
print(f"✅ Correct reverse: {original[::-1] == reversed_str}")

print("\n--- Stack Operations Demo ---")
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(f"Stack: {stack}")
print(f"Top item (peek): {stack.peek()}")
stack.pop()
print(f"After pop: {stack}")

print("\n" + "=" * 60)
print("TASK 8: QUEUE (FIFO)")
print("=" * 60)

# 8. Queue (FIFO)
class Queue:
    """A simple Queue implementation using a list"""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to the end of queue - O(1)"""
        self.items.append(item)
        print(f"✅ Enqueued: {item}")
    
    def dequeue(self):
        """Remove and return item from the front - O(n)"""
        if self.is_empty():
            print("❌ Queue is empty!")
            return None
        item = self.items.pop(0)
        print(f"✅ Dequeued: {item}")
        return item
    
    def front(self):
        """Return front item without removing - O(1)"""
        if self.is_empty():
            print("❌ Queue is empty!")
            return None
        return self.items[0]
    
    def is_empty(self):
        """Check if queue is empty - O(1)"""
        return len(self.items) == 0
    
    def get_size(self):
        """Return the size of the queue - O(1)"""
        return len(self.items)
    
    def __str__(self):
        """String representation of the queue"""
        return f"Queue: {self.items}"

print("\n--- Simulating a Bank Queue ---")

def bank_queue_simulation():
    """Simulate customers arriving and being served"""
    queue = Queue()
    
    # Customers arrive
    customers = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    print("🏦 Bank Queue Simulation")
    print("-" * 40)
    
    for customer in customers:
        print(f"📥 {customer} arrives at the bank")
        queue.enqueue(customer)
    
    print(f"\n📋 Current queue: {queue}")
    print(f"👥 Total customers waiting: {queue.get_size()}")
    
    print("\n--- Serving Customers ---")
    while not queue.is_empty():
        customer = queue.dequeue()
        print(f"💼 Serving: {customer}")
        print(f"📊 Remaining in queue: {queue.get_size()}")
    
    print("\n✅ All customers served!")

bank_queue_simulation()

print("\n" + "=" * 60)
print("INTERMEDIATE EXERCISES COMPLETE! 🎉")
print("=" * 60)
