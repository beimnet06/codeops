// ============================================
// Day 7 Mini Project Demo: TeleBirr Loyalty
// ============================================

const {
    createLoyaltyAccount,
    defaultEarnRule,
    holidayEarnRule,
    premiumEarnRule
} = require('./loyalty.js');

console.log("=".repeat(60));
console.log("🏪 DAY 7 MINI PROJECT: TELEBIRR LOYALTY");
console.log("=".repeat(60));

// ============================================
// 1. Create Accounts
// ============================================

console.log("\n📋 CREATING ACCOUNTS");

const regular = createLoyaltyAccount("Beimnet Tariku");
const premium = createLoyaltyAccount("Abel Kebede", premiumEarnRule);

console.log(`✅ ${regular.getName()} (Regular)`);
console.log(`✅ ${premium.getName()} (Premium)`);

// ============================================
// 2. Earn Points
// ============================================

console.log("\n💰 EARNING POINTS");

console.log(`\n--- ${regular.getName()} (Regular) ---`);
regular.earn(100);   // 10 points (100/10)
regular.earn(250);   // 25 points

console.log(`\n--- ${premium.getName()} (Premium) ---`);
premium.earn(100);   // 30 points (100/10 * 3)
premium.earn(250);   // 75 points

// ============================================
// 3. Check Balance
// ============================================

console.log("\n📊 BALANCES");
console.log(`${regular.getName()}: ${regular.balance()} points`);
console.log(`${premium.getName()}: ${premium.balance()} points`);

// ============================================
// 4. Redeem Points
// ============================================

console.log("\n🔄 REDEEMING POINTS");

console.log(`\n${regular.getName()} redeems 20 points:`);
regular.redeem(20);
console.log(`Balance: ${regular.balance()} points`);

console.log(`\n${regular.getName()} tries to redeem 30 points:`);
regular.redeem(30);
console.log(`Balance: ${regular.balance()} points`);

// ============================================
// 5. Privacy Check
// ============================================

console.log("\n🔒 PRIVACY CHECK");
console.log(`regular.points: ${regular.points}`);      // undefined
console.log(`regular._points: ${regular._points}`);    // undefined
console.log(`regular.balance(): ${regular.balance()}`); // Works!

console.log("\n✅ Points are truly private!");

// ============================================
// 6. Holiday Rule
// ============================================

console.log("\n🎄 HOLIDAY RULE (Double Points)");

const holiday = createLoyaltyAccount("Tigist Hailu", holidayEarnRule);
holiday.earn(100);   // 20 points (double)
console.log(`${holiday.getName()}: ${holiday.balance()} points`);

// ============================================
// 7. Independent Accounts
// ============================================

console.log("\n👥 INDEPENDENT ACCOUNTS");
console.log(`${regular.getName()}: ${regular.balance()} points`);
console.log(`${premium.getName()}: ${premium.balance()} points`);
console.log(`${holiday.getName()}: ${holiday.balance()} points`);

console.log("\n✅ Each account has its own private balance!");

console.log("\n" + "=".repeat(60));
console.log("🎉 DAY 7 MINI PROJECT COMPLETE!");
console.log("=".repeat(60));