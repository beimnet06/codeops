// ============================================
// app.js - Main Application
// ============================================

// Import from money.js module
const { VAT, addVat, calculateVat, formatPriceWithVat } = require('./money.js');

console.log("=== TELEBIRR VAT CALCULATOR ===");
console.log("=".repeat(40));

// Display VAT rate
console.log(`\n📊 VAT Rate: ${VAT * 100}%`);

// ============================================
// Process multiple prices
// ============================================

const prices = [100, 250, 500, 1000, 2000];

console.log("\n💰 PRICE PROCESSING");
console.log("-".repeat(40));

prices.forEach(price => {
    const vat = calculateVat(price);
    const total = addVat(price);
    console.log(`${price} ETB → VAT: ${vat.toFixed(2)} ETB → Total: ${total.toFixed(2)} ETB`);
});

// ============================================
// Formatted output
// ============================================

console.log("\n📋 FORMATTED OUTPUT");
console.log("-".repeat(40));

prices.forEach(price => {
    console.log(formatPriceWithVat(price));
});

// ============================================
// Summary
// ============================================

console.log("\n📊 SUMMARY");
console.log("-".repeat(40));

const allPrices = prices;
const allTotals = allPrices.map(price => addVat(price));
const grandTotal = allTotals.reduce((sum, total) => sum + total, 0);

console.log(`Total prices: ${allPrices.length}`);
console.log(`Grand total (including VAT): ${grandTotal.toFixed(2)} ETB`);

console.log("\n" + "=".repeat(40));
console.log("✅ App running successfully!");
console.log("=".repeat(40));