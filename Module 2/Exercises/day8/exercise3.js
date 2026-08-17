// ============================================
// Exercise 3: Destructuring
// ============================================

// Create a customer object
const customer = {
    name: "Beimnet Tariku",
    city: "Addis Ababa",
    balance: 1500,
    phone: "+251 900 00 00 00",
    accountType: "Premium"
};

console.log("=== CUSTOMER OBJECT ===");
console.log(customer);

// ============================================
// 1. Destructure name and city in one line
// ============================================

const { name, city } = customer;

console.log("\n📋 DESTRUCTURED VALUES");
console.log("-".repeat(30));
console.log(`Name: ${name}`);
console.log(`City: ${city}`);

// ============================================
// 2. Destructure with default values
// ============================================

const { country = "Ethiopia" } = customer;
console.log(`Country: ${country} (default value)`);

// ============================================
// 3. Destructure and rename variables
// ============================================

const { name: customerName, city: customerCity } = customer;
console.log(`\nRenamed: ${customerName} from ${customerCity}`);

// ============================================
// 4. Function with parameter destructuring
// ============================================

// Function that destructures the name property
function greet({ name }) {
    return `👋 Hello, ${name}! Welcome to TeleBirr!`;
}

console.log("\n--- greet() function ---");
console.log(greet(customer));
console.log(greet({ name: "Abel Kebede" }));
console.log(greet({ name: "Tigist Hailu" }));

// ============================================
// 5. Function with multiple destructured params
// ============================================

function displayCustomer({ name, city, balance }) {
    console.log(`\nCustomer: ${name}`);
    console.log(`Location: ${city}`);
    console.log(`Balance: ${balance} ETB`);
}

console.log("\n--- displayCustomer() function ---");
displayCustomer(customer);

// ============================================
// 6. Destructuring in callback (forEach)
// ============================================

console.log("\n--- Destructuring in callback ---");
const customers = [
    { name: "Beimnet", city: "Addis Ababa", balance: 1500 },
    { name: "Abel", city: "Dire Dawa", balance: 800 },
    { name: "Tigist", city: "Bahir Dar", balance: 2000 }
];

// Destructure in forEach callback
customers.forEach(({ name, city }) => {
    console.log(`${name} lives in ${city}`);
});

// ============================================
// 7. Nested destructuring (bonus)
// ============================================

const customerWithAddress = {
    name: "Beimnet Tariku",
    address: {
        city: "Addis Ababa",
        subcity: "Bole",
        houseNumber: "123"
    }
};

const { address: { city: addressCity, subcity } } = customerWithAddress;
console.log(`\nNested destructuring: ${subcity}, ${addressCity}`);