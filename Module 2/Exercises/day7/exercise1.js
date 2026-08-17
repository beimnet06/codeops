// ============================================
// Exercise 1: VAT Function
// ============================================

// 1. Regular function with default parameter
function vat(amount, rate = 0.15) {
    return amount * rate;
}

// 2. Arrow function with implicit return
const vatArrow = (amount, rate = 0.15) => amount * rate;

// ============================================
// Testing the functions
// ============================================

console.log("=== VAT CALCULATOR ===");

// Test regular function
console.log("Regular function:");
console.log(`VAT on 100 ETB (15%): ${vat(100)} ETB`);
console.log(`VAT on 200 ETB (15%): ${vat(200)} ETB`);
console.log(`VAT on 500 ETB (10%): ${vat(500, 0.10)} ETB`);

console.log("\nArrow function (implicit return):");
console.log(`VAT on 100 ETB (15%): ${vatArrow(100)} ETB`);
console.log(`VAT on 200 ETB (15%): ${vatArrow(200)} ETB`);
console.log(`VAT on 500 ETB (10%): ${vatArrow(500, 0.10)} ETB`);

console.log("\n✅ Both functions produce the same result!");