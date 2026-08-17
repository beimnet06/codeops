// ============================================
// report.js - Report Generator Module
// ============================================

/**
 * Get all credit transactions
 */
function getCredits(transactions) {
    return transactions.filter(({ type }) => type === "credit");
}

/**
 * Get all debit transactions
 */
function getDebits(transactions) {
    return transactions.filter(({ type }) => type === "debit");
}

/**
 * Calculate total amount for a list of transactions
 */
function calculateTotal(transactions) {
    return transactions.reduce((sum, { amount }) => sum + amount, 0);
}

/**
 * Format a receipt string
 */
function formatReceipt({ id, customer, amount, type }) {
    const emoji = type === "credit" ? "💰" : "💸";
    return `${emoji} Receipt #${id}: ${customer} - ${type === "credit" ? "+" : "-"}${amount} ETB`;
}

/**
 * Generate all receipts
 */
function generateReceipts(transactions) {
    return transactions.map(transaction => formatReceipt(transaction));
}

/**
 * Create a summary report
 */
function generateSummary(transactions) {
    const credits = getCredits(transactions);
    const debits = getDebits(transactions);
    
    return {
        totalTransactions: transactions.length,
        totalCredits: credits.length,
        totalDebits: debits.length,
        totalCreditAmount: calculateTotal(credits),
        totalDebitAmount: calculateTotal(debits),
        netBalance: calculateTotal(credits) - calculateTotal(debits)
    };
}

/**
 * Update a transaction amount using spread (immutable)
 */
function updateTransactionAmount(transaction, newAmount) {
    return {
        ...transaction,
        amount: newAmount
    };
}

// Export all functions
module.exports = {
    getCredits,
    getDebits,
    calculateTotal,
    formatReceipt,
    generateReceipts,
    generateSummary,
    updateTransactionAmount
};