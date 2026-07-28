
print("=" * 60)
print("TASK 8: FILE READING & WRITING")
print("=" * 60)

print("\n--- File Reading & Writing ---")

def write_students_to_file(filename="students.txt"):
    try:
        with open(filename, 'w') as file:
            file.write("Student Name,Score\n")
            students = [
                ("Beimnet Tariku", 95),
                ("Abel Kebede", 85),
                ("Sara Hailu", 78),
                ("Dawit Mekonnen", 92),
                ("Meron Taddesse", 88)
            ]
            
            for name, score in students:
                file.write(f"{name},{score}\n")
        
        print(f"✅ Successfully wrote 5 students to {filename}")
        return True
    except Exception as e:
        print(f"❌ Error writing to file: {e}")
        return False

def read_students_and_calculate_average(filename="students.txt"):
    try:
        total_score = 0
        count = 0
        students = []
        
        with open(filename, 'r') as file:
            next(file)
            
            for line in file:
                name, score = line.strip().split(',')
                students.append((name, int(score)))
                total_score += int(score)
                count += 1
        
        if count == 0:
            print("⚠️ No students found in the file.")
            return
        
        average = total_score / count
        
        print(f"\n📊 Student Scores:")
        print("-" * 30)
        for name, score in students:
            print(f"  {name}: {score}")
        print("-" * 30)
        print(f"📈 Average Score: {average:.2f}")
        print(f"📝 Total Students: {count}")
        
    except FileNotFoundError:
        print(f"❌ File '{filename}' does not exist!")
        print("💡 Please run the write function first.")
    except Exception as e:
        print(f"❌ Error reading file: {e}")

print("\n--- Writing students to file ---")
write_students_to_file()

print("\n--- Reading students from file ---")
read_students_and_calculate_average()

print("\n" + "=" * 60)
print("TASK 9: ERROR HANDLING")
print("=" * 60)

print("\n--- Error Handling with try/except ---")

def calculate_division():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        result = num1 / num2
        print(f"✅ {num1} ÷ {num2} = {result}")
        
    except ValueError:
        print("❌ Error: Please enter numeric values only!")
    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero!")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    finally:
        print("🔹 Calculation attempt completed")

calculate_division()

print("\n" + "=" * 60)
print("TASK 10: INVENTORY MANAGER")
print("=" * 60)

print("\n--- Inventory Manager ---")

inventory = {}

def add_product():
    print("\n" + "-" * 40)
    print("📦 ADD NEW PRODUCT")
    print("-" * 40)
    
    product_name = input("Enter product name: ").strip()
    
    if not product_name:
        print("❌ Product name cannot be empty!")
        return
    
    if product_name in inventory:
        print(f"⚠️ '{product_name}' already exists!")
        update = input("Do you want to update quantity? (y/n): ").lower()
        if update == 'y':
            update_quantity()
        return
    
    try:
        quantity = int(input("Enter quantity: "))
        if quantity < 0:
            print("❌ Quantity cannot be negative!")
            return
        
        inventory[product_name] = quantity
        print(f"✅ '{product_name}' added successfully with quantity {quantity}!")
        
    except ValueError:
        print("❌ Invalid input! Please enter a number.")

def update_quantity():
    print("\n" + "-" * 40)
    print("🔄 UPDATE QUANTITY")
    print("-" * 40)
    
    if not inventory:
        print("⚠️ Inventory is empty! Please add a product first.")
        return
    
    product_name = input("Enter product name: ").strip()
    
    if product_name not in inventory:
        print(f"❌ '{product_name}' not found in inventory!")
        return
    
    try:
        new_quantity = int(input("Enter new quantity: "))
        if new_quantity < 0:
            print("❌ Quantity cannot be negative!")
            return
        
        inventory[product_name] = new_quantity
        print(f"✅ '{product_name}' updated to quantity {new_quantity}!")
        
    except ValueError:
        print("❌ Invalid input! Please enter a number.")

def view_products():
    print("\n" + "-" * 40)
    print("📋 INVENTORY LIST")
    print("-" * 40)
    
    if not inventory:
        print("📭 Inventory is empty!")
        return
    
    print(f"{'Product':<20} {'Quantity':<10}")
    print("-" * 30)
    for product, quantity in inventory.items():
        print(f"{product:<20} {quantity:<10}")
    print("-" * 30)
    print(f"Total products: {len(inventory)}")

def save_to_file():
    print("\n" + "-" * 40)
    print("💾 SAVE INVENTORY")
    print("-" * 40)
    
    if not inventory:
        print("⚠️ Inventory is empty! Nothing to save.")
        return
    
    try:
        filename = input("Enter filename to save (default: inventory.txt): ").strip()
        if not filename:
            filename = "inventory.txt"
        
        with open(filename, 'w') as file:
            file.write("Product,Quantity\n")
            for product, quantity in inventory.items():
                file.write(f"{product},{quantity}\n")
        
        print(f"✅ Inventory saved successfully to {filename}!")
        
    except Exception as e:
        print(f"❌ Error saving to file: {e}")

def load_from_file():
    print("\n" + "-" * 40)
    print("📂 LOAD INVENTORY")
    print("-" * 40)
    
    filename = input("Enter filename to load (default: inventory.txt): ").strip()
    if not filename:
        filename = "inventory.txt"
    
    try:
        with open(filename, 'r') as file:
            next(file)
            
            loaded_count = 0
            for line in file:
                product, quantity = line.strip().split(',')
                inventory[product] = int(quantity)
                loaded_count += 1
        
        print(f"✅ Loaded {loaded_count} products from {filename}!")
        
    except FileNotFoundError:
        print(f"❌ File '{filename}' does not exist!")
    except Exception as e:
        print(f"❌ Error loading file: {e}")

print("\n📦 Welcome to the Inventory Manager!")
print("Manage your products and quantities easily.\n")

while True:
    print("\n" + "=" * 40)
    print("📋 INVENTORY MENU")
    print("=" * 40)
    print("1️⃣  Add New Product")
    print("2️⃣  Update Quantity")
    print("3️⃣  View All Products")
    print("4️⃣  Save to File")
    print("5️⃣  Load from File")
    print("6️⃣  Exit")
    print("=" * 40)
    
    choice = input("\nEnter your choice (1-6): ").strip()
    
    if choice == "1":
        add_product()
    
    elif choice == "2":
        update_quantity()
    
    elif choice == "3":
        view_products()
    
    elif choice == "4":
        save_to_file()
    
    elif choice == "5":
        load_from_file()
    
    elif choice == "6":
        print("\n" + "=" * 40)
        print("👋 Thank you for using Inventory Manager!")
        print("=" * 40)
        
        if inventory:
            print("\n📊 FINAL INVENTORY:")
            print("-" * 30)
            for product, quantity in inventory.items():
                print(f"  {product}: {quantity}")
        
        break
    
    else:
        print("❌ Invalid choice! Please enter 1, 2, 3, 4, 5, or 6.")

print("\n" + "=" * 60)
print("🎉 LEVEL 3 COMPLETE!")
print("=" * 60)
