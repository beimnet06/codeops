// ============================================
// Exercise 3: discountBy Factory
// ============================================

// Factory function that creates discount functions
function discountBy(rate) {
    // Returns a function that applies the discount
    return function(price) {
        return price - (price * rate);
    };
}

// Create specific discount functions
const memberPrice = discountBy(0.10); // 10% discount
const salePrice = discountBy(0.30);   // 30% discount

// ============================================
// Testing the factory
// ============================================

console.log("=== DISCOUNT FACTORY ===");

const originalPrice = 1000;

console.log(`Original price: ${originalPrice} ETB`);

// Apply member discount (10%)
const memberDiscounted = memberPrice(originalPrice);
console.log(`\nMember price (10% off): ${memberDiscounted} ETB`);
console.log(`You save: ${originalPrice - memberDiscounted} ETB`);

// Apply sale discount (30%)
const saleDiscounted = salePrice(originalPrice);
console.log(`\nSale price (30% off): ${saleDiscounted} ETB`);
console.log(`You save: ${originalPrice - saleDiscounted} ETB`);

// Test with multiple prices
console.log("\n--- Multiple Prices ---");
const prices = [500, 1000, 2000, 5000];
console.log("Prices:", prices);
console.log("\nMember prices (10% off):");
prices.forEach(price => {
    console.log(`  ${price} ETB → ${memberPrice(price)} ETB`);
});
console.log("\nSale prices (30% off):");
prices.forEach(price => {
    console.log(`  ${price} ETB → ${salePrice(price)} ETB`);
});

/*
============================================
EXPLANATION: Factory Pattern
============================================

1. discountBy is a factory function
   - It takes a rate parameter
   - It returns a NEW function

2. Each returned function remembers its rate
   - memberPrice remembers 0.10
   - salePrice remembers 0.30

3. Benefits:
   - Reusable logic
   - Each discount has its own rate
   - Easy to create new discount types

4. This is a practical use of closures!
*/