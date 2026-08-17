// ============================================
// Exercise 5: forEach with Ethiopian Cities
// ============================================

// Array of Ethiopian cities
const ethiopianCities = [
    "Addis Ababa",
    "Dire Dawa",
    "Bahir Dar",
    "Gondar",
    "Mekelle",
    "Hawassa",
    "Jimma",
    "Debre Markos",
    "Arba Minch",
    "Dessie"
];

// ============================================
// Using forEach to print cities with index
// ============================================

console.log("=== ETHIOPIAN CITIES ===");
console.log(`Total cities: ${ethiopianCities.length}\n`);

// Method 1: forEach with index parameter
console.log("Method 1: Using forEach with index:");
ethiopianCities.forEach(function(city, index) {
    console.log(`${index + 1}. ${city}`);
});

// Method 2: Arrow function with forEach (cleaner)
console.log("\nMethod 2: Using arrow function:");
ethiopianCities.forEach((city, index) => {
    console.log(`${index + 1}. ${city}`);
});

// Method 3: One-liner (most concise)
console.log("\nMethod 3: One-liner:");
ethiopianCities.forEach((city, index) => console.log(`${index + 1}. ${city}`));

// ============================================
// Additional: Filter and forEach combined
// ============================================

console.log("\n--- Cities starting with 'D' ---");
ethiopianCities
    .filter(city => city.startsWith('D'))
    .forEach((city, index) => {
        console.log(`${index + 1}. ${city}`);
    });

console.log("\n--- Cities with 6+ letters ---");
ethiopianCities
    .filter(city => city.length >= 7)
    .forEach((city, index) => {
        console.log(`${index + 1}. ${city}`);
    });

// ============================================
// Advanced: Create a formatted list
// ============================================

console.log("\n--- Formatted List ---");
let cityList = "";
ethiopianCities.forEach((city, index) => {
    cityList += `${index + 1}. ${city}\n`;
});
console.log(cityList);

/*
============================================
EXPLANATION: forEach Callback
============================================

1. forEach is a method that:
   - Takes a callback function
   - Runs the callback for each element in the array
   - Passes (element, index, array) to the callback

2. The callback parameters:
   - city: the current element
   - index: the index of the current element (0-based)

3. Common uses of forEach:
   - Printing list items
   - Modifying DOM elements
   - Accumulating data (with side effects)

4. Alternative methods:
   - map(): transforms data (returns new array)
   - filter(): filters data (returns new array)
   - reduce(): accumulates data (returns single value)
*/