
print("=" * 60)
print("TASK 4: LIST OPERATIONS")
print("=" * 60)

print("\n--- List Operations ---")

numbers = [10, 25, 40, 15, 60, 30]
print(f"Original list: {numbers}")

print("\nNumbers greater than 30:")
for num in numbers:
    if num > 30:
        print(f"  {num}")

numbers.sort()
print(f"\nSorted list: {numbers}")

total_sum = sum(numbers)
average = total_sum / len(numbers)
print(f"Sum: {total_sum}")
print(f"Average: {average:.2f}")

print("\n" + "=" * 60)
print("TASK 5: DICTIONARY OPERATIONS")
print("=" * 60)

print("\n--- Dictionary Operations ---")

products = {
    "Injera": 50.00,
    "Doro Wat": 120.00,
    "Tibs": 150.00,
    "Kitfo": 180.00,
    "Shiro": 70.00
}

print("📋 Product Price List:")
print("-" * 30)
for product, price in products.items():
    print(f"  {product}: ${price:.2f}")
print("-" * 30)

user_product = input("\nEnter a product name to check price: ")

price = products.get(user_product, "Product not found!")
if price == "Product not found!":
    print(f"❌ {price}")
else:
    print(f"✅ {user_product} costs ${price:.2f}")

print("\n" + "=" * 60)
print("TASK 6: LIST COMPREHENSION")
print("=" * 60)

print("\n--- List Comprehension ---")

numbers_1_20 = [num for num in range(1, 21)]
print(f"Numbers 1 to 20: {numbers_1_20}")

even_numbers = [num for num in range(1, 31) if num % 2 == 0]
print(f"Even numbers 1 to 30: {even_numbers}")

odd_numbers = [num for num in range(1, 11) if num % 2 != 0]
print(f"Odd numbers 1 to 10: {odd_numbers}")

print("\n" + "=" * 60)
print("TASK 7: MODULES & IMPORT")
print("=" * 60)

print("\n--- Modules & Import ---")
print("Creating utils.py file with add_tax function...")

with open('utils.py', 'w') as f:
    f.write('''# ============================================

def add_tax(price, rate=0.15):
    Calculate price with tax included.
    
    Parameters:
    - price: Original price
    - rate: Tax rate (default: 0.15 = 15%)
    
    Returns:
    - Price with tax included
    tax = price * rate
    total = price + tax
    return total

if __name__ == "__main__":
    print("Testing add_tax function:")
    print(f"Price $100 with 15% tax: ${add_tax(100):.2f}")
    print(f"Price $200 with 10% tax: ${add_tax(200, 0.10):.2f}")
''')

print("✅ utils.py created successfully!")

try:
    from utils import add_tax
    
    print("\nTesting add_tax function:")
    print(f"Price $100 with 15% tax: ${add_tax(100):.2f}")
    print(f"Price $200 with 10% tax: ${add_tax(200, 0.10):.2f}")
    print(f"Price $50 with 15% tax: ${add_tax(50):.2f}")
    
except ImportError as e:
    print(f"❌ Error importing utils: {e}")

print("\n" + "=" * 60)
print("LEVEL 2 COMPLETE! 🎉")
print("=" * 60)
