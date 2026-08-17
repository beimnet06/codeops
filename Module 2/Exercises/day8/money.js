// ============================================
// money.js - Module
// ============================================

// Constant: VAT rate
const VAT = 0.15;

// Function: Add VAT to a price
function addVat(price) {
    return price + (price * VAT);
}

// Function: Calculate VAT amount (bonus)
function calculateVat(price) {
    return price * VAT;
}

// Function: Get price with VAT formatted (bonus)
function formatPriceWithVat(price) {
    const total = addVat(price);
    return `${price} ETB + ${(price * VAT).toFixed(2)} ETB VAT = ${total.toFixed(2)} ETB`;
}

// Export all functions and constants
module.exports = {
    VAT,
    addVat,
    calculateVat,
    formatPriceWithVat
};