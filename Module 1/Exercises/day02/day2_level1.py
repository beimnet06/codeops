
full_name = "Beimnet Tariku"
age = 25
height = 5.9
is_student = True
favorite_food = "Injera"

print(f"Hello! My name is {full_name}.")
print(f"I am {age} years old and {height} feet tall.")
print(f"It is {is_student} that I am a student.")
print(f"My favorite food is {favorite_food}!")

print("\n--- Arithmetic Operations ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\n📊 Results for {num1} and {num2}:")
print(f"➕ Sum: {num1 + num2}")
print(f"➖ Difference: {num1 - num2}")
print(f"✖️ Product: {num1 * num2}")
print(f"➗ Division: {num1 / num2}")
print(f"➗ Floor Division: {num1 // num2}")
print(f"🔢 Remainder: {num1 % num2}")

print("\n--- Type Conversion ---")
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print(f"🎂 You are {age} years old in {current_year}!")

print("\n--- Grade Checker ---")
score = float(input("Enter your score (0-100): "))

if score >= 50:
    print("✅ Pass")
else:
    print("❌ Fail")
