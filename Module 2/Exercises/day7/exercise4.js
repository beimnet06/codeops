// ============================================
// Exercise 4: Higher-Order applyToAll
// ============================================

// Higher-order function: takes a list and a function, applies function to each item
function applyToAll(list, fn) {
    const result = [];
    for (let i = 0; i < list.length; i++) {
        result.push(fn(list[i]));
    }
    return result;
}

// VAT function (from Exercise 1)
function vat(amount, rate = 0.15) {
    return amount * rate;
}

// Function to add VAT to a price (returns total with VAT)
function addVAT(price, rate = 0.15) {
    return price + (price * rate);
}

// ============================================
// Testing applyToAll
// ============================================

console.log("=== HIGHER-ORDER: applyToAll ===");

// Sample prices
const prices = [100, 200, 350, 500, 1000];
console.log("Original prices:", prices);

// Use applyToAll to calculate VAT for each price
const vatAmounts = applyToAll(prices, (price) => vat(price));
console.log("\nVAT amounts (15%):", vatAmounts);

// Use applyToAll to calculate total with VAT
const pricesWithVAT = applyToAll(prices, (price) => addVAT(price));
console.log("\nPrices with VAT (15%):", pricesWithVAT);

// Use applyToAll with a different VAT rate (10%)
const vatAmounts10 = applyToAll(prices, (price) => vat(price, 0.10));
console.log("\nVAT amounts (10%):", vatAmounts10);

const pricesWithVAT10 = applyToAll(prices, (price) => addVAT(price, 0.10));
console.log("Prices with VAT (10%):", pricesWithVAT10);

// ============================================
// Display as a table
// ============================================

console.log("\n--- Summary Table ---");
console.log("Price | VAT (15%) | Total (15%) | VAT (10%) | Total (10%)");
console.log("------|-----------|-------------|-----------|-------------");

for (let i = 0; i < prices.length; i++) {
    const price = prices[i];
    const vat15 = vatAmounts[i];
    const total15 = pricesWithVAT[i];
    const vat10 = vatAmounts10[i];
    const total10 = pricesWithVAT10[i];
    
    console.log(
        `${String(price).padEnd(5)} | ${String(vat15).padEnd(9)} | ${String(total15).padEnd(11)} | ${String(vat10).padEnd(9)} | ${String(total10).padEnd(11)}`
    );
}

/*
============================================
EXPLANATION: Higher-Order Functions
============================================

1. Higher-order function = a function that:
   - Takes another function as an argument, OR
   - Returns a function

2. applyToAll is a higher-order function because:
   - It takes `fn` (a function) as a parameter
   - It applies `fn` to every item in the list

3. Benefits of higher-order functions:
   - Code reusability
   - Separation of concerns
   - More readable and maintainable code

4. This is a core concept in functional programming!
*/