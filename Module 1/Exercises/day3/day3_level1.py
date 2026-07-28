
print("=" * 60)
print("TASK 1: LISTS & TUPLES")
print("=" * 60)

print("\n--- Lists ---")

favorite_foods = ["Injera", "Doro Wat", "Tibs", "Kitfo", "Shiro", "Firfir"]
print(f"My favorite foods: {favorite_foods}")

print(f"First food: {favorite_foods[0]}")
print(f"Last food: {favorite_foods[-1]}")

favorite_foods.append("Beyainatu")
print(f"After adding Beyainatu: {favorite_foods}")

removed_food = favorite_foods.pop(1)  # Removes "Doro Wat"
print(f"Removed: {removed_food}")
print(f"After removing second food: {favorite_foods}")

ethiopia_coordinates = (8.9806, 38.7578)
latitude, longitude = ethiopia_coordinates
print(f"\n--- Tuples ---")
print(f"Ethiopia coordinates: ({latitude}, {longitude})")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")

print("\n" + "=" * 60)
print("TASK 2: DICTIONARIES")
print("=" * 60)

print("\n--- Dictionaries ---")

student = {
    "name": "Beimnet Tariku",
    "age": 22,
    "grade": "A",
    "city": "Addis Ababa",
    "department": "Computer Science"
}

print(f"Student dictionary: {student}")

print(f"\nStudent Name: {student['name']}")
print(f"Department: {student['department']}")
print(f"Grade: {student['grade']}")

student["phone"] = "0910607442"
print(f"\nAfter adding phone: {student}")

student["grade"] = "A+"
print(f"After updating grade: {student}")

print("\n" + "=" * 60)
print("TASK 3: SETS")
print("=" * 60)

print("\n--- Sets ---")

names_list = ["Beimnet", "Abel", "Sara", "Beimnet", "Dawit", "Sara", "Kebede"]
print(f"List with duplicates: {names_list}")

names_set = set(names_list)
print(f"Set without duplicates: {names_set}")

names_set.add("Meron")
print(f"After adding Meron: {names_set}")

print("\n" + "=" * 60)
print("LEVEL 1 COMPLETE! 🎉")
print("=" * 60)
