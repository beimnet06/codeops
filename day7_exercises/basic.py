# ============================================
# Day 7 - Basic: Big-O Notation & Linear Structures
# ============================================

print("=" * 60)
print("TASK 1: BIG-O NOTATION")
print("=" * 60)

print("""
📊 Big-O Notation Examples:

1. Accessing an element in a Python list by index:
   ✅ O(1) - Constant time
   Explanation: Direct access to memory address

2. Searching for an element in a list using 'in':
   ⚠️ O(n) - Linear time
   Explanation: May need to scan entire list

3. Inserting at the beginning of a list:
   🔴 O(n) - Linear time
   Explanation: Shifts all elements to the right

4. Dictionary lookup by key:
   ✅ O(1) - Constant time (average case)
   Explanation: Uses hash table
""")

print("=" * 60)
print("TASK 2: COMPARE COMPLEXITIES")
print("=" * 60)

print("""
📈 Complexity Ranking (Fastest to Slowest for n = 1,000,000):

1️⃣ O(1) - Constant Time
   → Fastest! Always takes the same time
   Example: Access list[0], dict lookup

2️⃣ O(log n) - Logarithmic Time
   → Very fast! Doubles input = +1 step
   Example: Binary search

3️⃣ O(n) - Linear Time
   → Grows proportionally with input
   Example: Searching a list

4️⃣ O(n²) - Quadratic Time
   → Slowest! Grows exponentially
   Example: Nested loops

💡 For n = 1,000,000:
   O(1) = 1 operation
   O(log n) ≈ 20 operations
   O(n) = 1,000,000 operations
   O(n²) = 1,000,000,000,000 operations
""")

print("=" * 60)
print("TASK 3: ARRAYS / LISTS")
print("=" * 60)

# 3. Arrays / Lists
print("\n--- Working with Lists ---")

# Create a list of 10 student names
students = ["Alice", "Bob", "Charlie", "David", "Eva", 
            "Frank", "Grace", "Henry", "Ivy", "Jack"]
print(f"Original list: {students}")

# Accessing by index (O(1))
print(f"\nAccessing by index:")
print(f"  First student: {students[0]}")
print(f"  Last student: {students[-1]}")
print(f"  Middle student: {students[4]}")

# Adding at the end (O(1))
print(f"\nAdding at the end:")
students.append("Kevin")
print(f"  After append: {students}")

# Inserting at position 0 (O(n))
print(f"\nInserting at position 0:")
students.insert(0, "Zara")
print(f"  After insert: {students}")

print("\n" + "=" * 60)
print("TASK 4: HASHMAPS (DICTIONARIES)")
print("=" * 60)

# 4. Hashmaps (Dictionaries)
print("\n--- Working with Dictionaries ---")

# Create a dictionary with 5 students
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eva": 88
}

print(f"Original dictionary: {student_grades}")

# Add a new student (O(1))
print(f"\nAdding a new student:")
student_grades["Frank"] = 90
print(f"  After adding: {student_grades}")

# Update a grade (O(1))
print(f"\nUpdating a grade:")
student_grades["Alice"] = 90
print(f"  After update: {student_grades}")

# Check if a student exists (O(1))
print(f"\nChecking if student exists:")
print(f"  'Alice' exists: {'Alice' in student_grades}")
print(f"  'Zara' exists: {'Zara' in student_grades}")

# Get grade with default (O(1))
print(f"\nGetting grades:")
print(f"  Alice's grade: {student_grades.get('Alice', 'Not found')}")
print(f"  Zara's grade: {student_grades.get('Zara', 'Not found')}")

print("\n" + "=" * 60)
print("BASIC EXERCISES COMPLETE! 🎉")
print("=" * 60)
