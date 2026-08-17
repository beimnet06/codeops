// ============================================
// Exercise 1: map, filter, reduce
// ============================================

// Array of ETB prices
const prices = [200, 450, 800, 1200, 300, 1500, 500, 2500, 700, 100];

console.log("=== PRICE PROCESSING ===");
console.log("Original prices:", prices);

// 1. map: Add 15% VAT to each price
const pricesWithVAT = prices.map(price => price * 1.15);
console.log("\n1. Prices with 15% VAT:", pricesWithVAT.map(p => p.toFixed(2)));

// 2. filter: Keep only prices under 1000 ETB
const under1000 = pricesWithVAT.filter(price => price < 1000);
console.log("\n2. Prices under 1000 ETB:", under1000.map(p => p.toFixed(2)));

// 3. reduce: Calculate grand total
const grandTotal = under1000.reduce((total, price) => total + price, 0);
console.log(`\n3. Grand total: ${grandTotal.toFixed(2)} ETB`);

// ============================================
// One-liner approach (chaining)
// ============================================

console.log("\n--- One-liner (chaining) ---");
const result = prices
    .map(price => price * 1.15)
    .filter(price => price < 1000)
    .reduce((total, price) => total + price, 0);

console.log(`Grand total (chained): ${result.toFixed(2)} ETB`);

// ============================================
// Detailed breakdown
// ============================================

console.log("\n--- Detailed Breakdown ---");
console.log("Step 1: Add VAT (15%)");
prices.forEach((price, i) => {
    console.log(`  ${price} → ${(price * 1.15).toFixed(2)}`);
});

console.log("\nStep 2: Filter under 1000");
const filtered = prices.map(p => p * 1.15).filter(p => p < 1000);
filtered.forEach(p => {
    console.log(`  ${p.toFixed(2)} (under 1000)`);
});

console.log(`\nStep 3: Grand total = ${result.toFixed(2)} ETB`);
