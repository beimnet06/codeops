# Day 7 Mini Project — TeleBirr Loyalty Points

A loyalty-points module for a TeleBirr shop that tracks a customer's points balance privately.

## 🔒 Privacy

The points balance is **private** — cannot be accessed directly from outside. Only exposed functions (`earn`, `redeem`, `balance`) can interact with it.

## 🚀 Usage

```javascript
const { createLoyaltyAccount } = require('./loyalty.js');

const account = createLoyaltyAccount("John Doe");
account.earn(100);               // Earn points
account.redeem(50);              // Redeem points
console.log(account.balance());  // Check balance