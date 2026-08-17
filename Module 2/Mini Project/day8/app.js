// ============================================
// app.js - Main Application
// ============================================

// Import modules
const transactions = require('./transactions.js');
const {
    getCredits,
    getDebits,
    calculateTotal,
    generateReceipts,
    generateSummary,
    updateTransactionAmount
} = require('./report.js');

console.log("=".repeat(60));
console.log("🏪 TELEBIRR TRANSACTION REPORT");
console.log("=".repeat(60));

// ============================================
// 1. Display all transactions
// ============================================

console.log("\n📋 ALL TRANSACTIONS");
console.log("-".repeat(40));
console.log("ID | Customer | Amount | Type");
console.log("-".repeat(40));
transactions.forEach(({ id, customer, amount, type }) => {
    console.log(`${id} | ${customer} | ${amount} ETB | ${type}`);
});

// ============================================
// 2. Filter: Credits vs Debits
// ============================================

console.log("\n💰 CREDITS (Money In)");
console.log("-".repeat(40));
const credits = getCredits(transactions);
credits.forEach(({ customer, amount }) => {
    console.log(`${customer}: +${amount} ETB`);
});
console.log(`Total Credits: ${calculateTotal(credits)} ETB`);

console.log("\n💸 DEBITS (Money Out)");
console.log("-".repeat(40));
const debits = getDebits(transactions);
debits.forEach(({ customer, amount }) => {
    console.log(`${customer}: -${amount} ETB`);
});
console.log(`Total Debits: ${calculateTotal(debits)} ETB`);

// ============================================
// 3. Receipts (with destructuring)
// ============================================

console.log("\n🧾 RECEIPTS");
console.log("-".repeat(40));
const receipts = generateReceipts(transactions);
receipts.forEach(receipt => console.log(receipt));

// ============================================
// 4. Summary using reduce
// ============================================

console.log("\n📊 SUMMARY REPORT");
console.log("-".repeat(40));
const summary = generateSummary(transactions);
console.log(`Total Transactions: ${summary.totalTransactions}`);
console.log(`Credits: ${summary.totalCredits} (${summary.totalCreditAmount} ETB)`);
console.log(`Debits: ${summary.totalDebits} (${summary.totalDebitAmount} ETB)`);
console.log(`Net Balance: ${summary.netBalance} ETB`);

// ============================================
// 5. Spread: Update a transaction without mutating
// ============================================

console.log("\n🔄 SPREAD UPDATE (Immutable)");
console.log("-".repeat(40));

// Original transaction
const originalTransaction = transactions[0];
console.log(`Original: ${originalTransaction.customer} - ${originalTransaction.amount} ETB`);

// Update amount using spread
const updatedTransaction = updateTransactionAmount(originalTransaction, 750);
console.log(`Updated: ${updatedTransaction.customer} - ${updatedTransaction.amount} ETB`);

// Verify original unchanged
console.log(`Original still: ${transactions[0].customer} - ${transactions[0].amount} ETB`);
console.log("✅ Original transaction unchanged!");

// ============================================
// 6. Final Summary
// ============================================

console.log("\n" + "=".repeat(60));
console.log("🎉 TELEBIRR TRANSACTION REPORT COMPLETE!");
console.log("=".repeat(60));