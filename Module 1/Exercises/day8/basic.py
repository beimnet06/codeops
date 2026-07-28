
print("=" * 60)
print("TASK 1: RECURSION BASICS - FACTORIAL")
print("=" * 60)


def factorial_recursive(n):
    Calculate factorial using recursion - O(n)
    Base case: n <= 1 returns 1
    Recursive case: n * factorial(n-1)
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    Calculate factorial using iteration - O(n)
    Uses a loop to multiply numbers from 1 to n
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("\n--- Testing Factorial Functions ---")
test_numbers = [0, 1, 5, 7, 10]

for num in test_numbers:
    rec_result = factorial_recursive(num)
    iter_result = factorial_iterative(num)
    print(f"Factorial of {num}:")
    print(f"  Recursive: {rec_result}")
    print(f"  Iterative: {iter_result}")
    print(f"  Match: {'✅' if rec_result == iter_result else '❌'}")
    print()

print("💡 Recursive vs Iterative:")
print("  - Recursive: Elegant but uses stack memory (O(n) space)")
print("  - Iterative: More memory efficient (O(1) space)")

print("\n" + "=" * 60)
print("TASK 2: RECURSION WITH LISTS - SUM LIST")
print("=" * 60)


def sum_list_recursive(numbers):
    Calculate sum of list using recursion - O(n)
    Base case: empty list returns 0
    Recursive case: first + sum of rest
    if not numbers:
        return 0
    return numbers[0] + sum_list_recursive(numbers[1:])

def sum_list_iterative(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("\n--- Testing Sum List Functions ---")
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"List: {test_list}")
print(f"Recursive sum: {sum_list_recursive(test_list)}")
print(f"Iterative sum: {sum_list_iterative(test_list)}")
print(f"Built-in sum: {sum(test_list)}")
print("✅ All methods match!")

print("\n" + "=" * 60)
print("TASK 3: LINEAR SEARCH")
print("=" * 60)


def linear_search(arr, target):
    Linear search algorithm - O(n)
    Scans array from start to end
    Returns index if found, -1 if not found
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print("\n--- Testing Linear Search ---")
test_arr = [3, 7, 2, 9, 1, 5, 8, 4, 6]
print(f"Array: {test_arr}")

search_targets = [5, 10, 2]

for target in search_targets:
    result = linear_search(test_arr, target)
    if result != -1:
        print(f"✅ Found {target} at index {result}")
    else:
        print(f"❌ {target} not found in array")

print("\n💡 Linear Search Analysis:")
print("  - Time Complexity: O(n)")
print("  - Space Complexity: O(1)")
print("  - Works on unsorted arrays")
print("  - Simple but slow for large datasets")

print("\n" + "=" * 60)
print("TASK 4: BINARY SEARCH")
print("=" * 60)


def binary_search(arr, target):
    Binary search algorithm - O(log n)
    Requires sorted array
    Uses divide and conquer approach
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        print(f"  Checking index {mid}: {arr[mid]}")
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

print("\n--- Testing Binary Search ---")
sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(f"Sorted Array: {sorted_arr}")

search_targets = [7, 12, 20]

for target in search_targets:
    print(f"\nSearching for {target}:")
    result = binary_search(sorted_arr, target)
    if result != -1:
        print(f"✅ Found {target} at index {result}")
    else:
        print(f"❌ {target} not found")

print("\n💡 Why Binary Search Needs Sorted Array:")
print("  - Divides search space in half based on comparison")
print("  - Without sorting, can't determine which half to search")
print("  - Relies on the property: all elements in left half < all in right half")
print("\n📊 Binary Search Analysis:")
print("  - Time Complexity: O(log n)")
print("  - Space Complexity: O(1)")
print("  - Much faster than linear search for large datasets")

print("\n" + "=" * 60)
print("TASK 5: BUBBLE SORT")
print("=" * 60)


def bubble_sort(arr):
    Bubble Sort algorithm - O(n²)
    Repeatedly swaps adjacent elements if out of order
    Each pass pushes largest element to the end
    n = len(arr)
    arr_copy = arr.copy()  # Don't modify original
    print(f"\nOriginal array: {arr_copy}")
    print("Starting Bubble Sort...\n")
    
    for i in range(n):
        swapped = False
        print(f"Pass {i + 1}:")
        
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
                print(f"  Swapped {arr_copy[j]} and {arr_copy[j + 1]}")
        
        print(f"  Array after pass {i + 1}: {arr_copy}")
        
        if not swapped:
            print("  No swaps made - array is sorted!")
            break
    
    print(f"\n✅ Final sorted array: {arr_copy}")
    return arr_copy

print("\n--- Testing Bubble Sort ---")
test_arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(test_arr)

print("\n" + "=" * 60)
print("BASIC EXERCISES COMPLETE! 🎉")
print("=" * 60)
