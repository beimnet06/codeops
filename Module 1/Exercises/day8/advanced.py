
print("=" * 60)
print("TASK 6: RECURSIVE PROBLEMS")
print("=" * 60)


def reverse_string_recursive(text):
    Reverse a string using recursion - O(n)
    Base case: empty string returns empty string
    Recursive case: last char + reverse of rest
    if not text:
        return ""
    return text[-1] + reverse_string_recursive(text[:-1])

def count_occurrences_recursive(arr, target):
    Count occurrences of target in list using recursion - O(n)
    Base case: empty list returns 0
    Recursive case: count in first element + count in rest
    if not arr:
        return 0
    count = 1 if arr[0] == target else 0
    return count + count_occurrences_recursive(arr[1:], target)

print("\n--- Testing String Reversal ---")
test_strings = ["hello", "python", "recursion", "Addis Ababa"]

for text in test_strings:
    reversed_text = reverse_string_recursive(text)
    print(f"Original: {text}")
    print(f"Reversed: {reversed_text}")
    print(f"Correct? {reversed_text == text[::-1]}")
    print()

print("\n--- Testing Count Occurrences ---")
test_list = [1, 2, 3, 2, 4, 2, 5, 2, 6, 2]
print(f"List: {test_list}")
target = 2
count = count_occurrences_recursive(test_list, target)
print(f"Number of {target}s: {count}")
print(f"Built-in count: {test_list.count(target)}")
print(f"✅ Match!")

print("\n" + "=" * 60)
print("TASK 7: SORTING COMPARISON")
print("=" * 60)


def selection_sort(arr):
    Selection Sort - O(n²)
    Finds minimum element and places it at the beginning
    arr_copy = arr.copy()
    n = len(arr_copy)
    swaps = 0
    comparisons = 0
    
    print(f"\n--- Selection Sort ---")
    print(f"Original: {arr_copy}")
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        
        if i != min_idx:
            arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
            swaps += 1
            print(f"  Pass {i+1}: {arr_copy}")
    
    print(f"✅ Sorted: {arr_copy}")
    print(f"📊 Comparisons: {comparisons}")
    print(f"📊 Swaps: {swaps}")
    return arr_copy

def insertion_sort(arr):
    Insertion Sort - O(n²)
    Builds sorted array by inserting elements one by one
    arr_copy = arr.copy()
    n = len(arr_copy)
    swaps = 0
    comparisons = 0
    
    print(f"\n--- Insertion Sort ---")
    print(f"Original: {arr_copy}")
    
    for i in range(1, n):
        key = arr_copy[i]
        j = i - 1
        
        while j >= 0 and arr_copy[j] > key:
            comparisons += 1
            arr_copy[j + 1] = arr_copy[j]
            swaps += 1
            j -= 1
        
        if j >= 0:
            comparisons += 1  # For the failed comparison
            
        arr_copy[j + 1] = key
        print(f"  Pass {i}: {arr_copy}")
    
    print(f"✅ Sorted: {arr_copy}")
    print(f"📊 Comparisons: {comparisons}")
    print(f"📊 Swaps: {swaps}")
    return arr_copy

def bubble_sort_count(arr):
    Bubble Sort with counting - O(n²)
    arr_copy = arr.copy()
    n = len(arr_copy)
    swaps = 0
    comparisons = 0
    
    print(f"\n--- Bubble Sort ---")
    print(f"Original: {arr_copy}")
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swaps += 1
                swapped = True
        print(f"  Pass {i+1}: {arr_copy}")
        
        if not swapped:
            break
    
    print(f"✅ Sorted: {arr_copy}")
    print(f"📊 Comparisons: {comparisons}")
    print(f"📊 Swaps: {swaps}")
    return arr_copy

print("\n--- Testing Sorting Algorithms on Same List ---")
test_arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array: {test_arr}")

print("\n" + "=" * 40)
selection_sort(test_arr)

print("\n" + "=" * 40)
insertion_sort(test_arr)

print("\n" + "=" * 40)
bubble_sort_count(test_arr)

print("\n" + "=" * 40)
print("📊 SORTING ALGORITHMS COMPARISON")
print("=" * 40)
print("""
| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |

💡 When to use:
- Bubble Sort: Educational purposes, simple to implement
- Selection Sort: When memory is limited (minimum swaps)
- Insertion Sort: When data is nearly sorted, small datasets

print("\n" + "=" * 60)
print("TASK 8: TWO POINTER TECHNIQUE")
print("=" * 60)


def find_pair_with_sum(arr, target):
    Find two numbers in sorted array that sum to target - O(n)
    Uses two pointers: one at start, one at end
    if not arr:
        return None
    
    left = 0
    right = len(arr) - 1
    pairs_found = []
    
    print(f"Searching for pair with sum = {target}")
    print(f"Array: {arr}")
    print("\nTwo Pointer Process:")
    
    while left < right:
        current_sum = arr[left] + arr[right]
        print(f"  Left[{left}]={arr[left]}, Right[{right}]={arr[right]}, Sum={current_sum}")
        
        if current_sum == target:
            pairs_found.append((arr[left], arr[right]))
            print(f"  ✅ Found pair: {arr[left]} + {arr[right]} = {target}")
            left += 1
            right -= 1
        elif current_sum < target:
            print(f"  Sum < {target}, moving left pointer")
            left += 1
        else:
            print(f"  Sum > {target}, moving right pointer")
            right -= 1
    
    return pairs_found

print("\n--- Testing Two Pointer Technique ---")
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
targets = [10, 15, 7]

for target in targets:
    print(f"\n" + "=" * 40)
    pairs = find_pair_with_sum(sorted_array, target)
    if pairs:
        print(f"✅ Found {len(pairs)} pair(s): {pairs}")
    else:
        print(f"❌ No pairs found with sum {target}")

print("\n" + "=" * 60)
print("ADVANCED EXERCISES COMPLETE! 🎉")
print("=" * 60)
