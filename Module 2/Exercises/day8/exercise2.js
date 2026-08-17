// ============================================
// Exercise 2: Object.entries
// ============================================

// Create a customer object
const customer = {
    name: "Beimnet Tariku",
    city: "Addis Ababa",
    balance: 1500,
    phone: "+251 910 607 442",
    accountType: "Premium"
};

console.log("=== CUSTOMER OBJECT ===");
console.log(customer);

// ============================================
// Using Object.entries with for...of
// ============================================

console.log("\n📋 CUSTOMER DETAILS");
console.log("-".repeat(40));

// Method 1: Basic Object.entries
console.log("\nMethod 1: Basic");
for (const [key, value] of Object.entries(customer)) {
    console.log(`${key}: ${value}`);
}

// ============================================
// More advanced examples
// ============================================

console.log("\n📊 CUSTOMER SUMMARY");
console.log("-".repeat(40));

// Method 2: Format nicely with header
console.log("Key | Value");
console.log("-".repeat(30));
for (const [key, value] of Object.entries(customer)) {
    // Capitalize first letter of key
    const formattedKey = key.charAt(0).toUpperCase() + key.slice(1);
    console.log(`${formattedKey}: ${value}`);
}

// ============================================
// Filtering entries
// ============================================

console.log("\n🔍 Filtering Entries");
console.log("-".repeat(40));

// Print only customer info (not sensitive data)
const sensitiveKeys = ['balance'];
for (const [key, value] of Object.entries(customer)) {
    if (!sensitiveKeys.includes(key)) {
        console.log(`${key}: ${value}`);
    }
}

// ============================================
// Transforming entries
// ============================================

console.log("\n🔄 Transforming Entries");
console.log("-".repeat(40));

// Create a formatted string from entries
let formattedString = "";
for (const [key, value] of Object.entries(customer)) {
    formattedString += `${key.toUpperCase()}: ${value} | `;
}
console.log("Formatted:", formattedString.slice(0, -3));

// ============================================
// Converting entries to array
// ============================================

console.log("\n📦 Object.entries() returns an array:");
const entries = Object.entries(customer);
console.log("Entries array:", entries);
console.log("Number of entries:", entries.length);

// ============================================
// Bonus: Object.keys and Object.values
// ============================================

console.log("\n--- Related Methods ---");
console.log("Object.keys:", Object.keys(customer));
console.log("Object.values:", Object.values(customer));