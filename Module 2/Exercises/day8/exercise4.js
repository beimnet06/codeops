// ============================================
// Exercise 4: Spread Operator
// ============================================

// Original customer object
const customer = {
    name: "Beimnet Tariku",
    city: "Gondar",
    balance: 1500,
    accountType: "Premium"
};

console.log("=== ORIGINAL CUSTOMER ===");
console.log(customer);

// ============================================
// 1. Create updated copy with spread
// ============================================

// Update city and add phone field
const updatedCustomer = {
    ...customer,
    city: "Addis Ababa",
    phone: "+251 910 607 442"
};

console.log("\n📋 UPDATED CUSTOMER (Spread)");
console.log(updatedCustomer);

// ============================================
// 2. Verify original is unchanged
// ============================================

console.log("\n🔍 ORIGINAL VS UPDATED");
console.log("-".repeat(40));
console.log("Original city:", customer.city);        // Gondar
console.log("Updated city:", updatedCustomer.city);  // Addis Ababa
console.log("\nOriginal phone:", customer.phone);    // undefined
console.log("Updated phone:", updatedCustomer.phone); // +251 910 607 442
console.log("\n✅ Original object is unchanged!");

// ============================================
// 3. Multiple updates with spread
// ============================================

console.log("\n🔄 MULTIPLE UPDATES");
console.log("-".repeat(40));

const customerV1 = { ...customer };
const customerV2 = { ...customerV1, city: "Addis Ababa" };
const customerV3 = { ...customerV2, phone: "+251 910 607 442" };
const customerV4 = { ...customerV3, balance: 2000, accountType: "VIP" };

console.log("v1:", customerV1);
console.log("v2:", customerV2);
console.log("v3:", customerV3);
console.log("v4:", customerV4);

// ============================================
// 4. Spread with multiple objects
// ============================================

console.log("\n📦 MERGING WITH SPREAD");
console.log("-".repeat(40));

const contactInfo = {
    phone: "+251 910 0000002",
    email: "beimnettariku871@gmail.com"
};

const addressInfo = {
    city: "Addis Ababa",
    subcity: "Bole",
    country: "Ethiopia"
};

const mergedCustomer = {
    ...customer,
    ...contactInfo,
    ...addressInfo
};

console.log("Merged customer:", mergedCustomer);

// ============================================
// 5. Spread vs Object.assign
// ============================================

console.log("\n🔄 SPREAD VS OBJECT.ASSIGN");
console.log("-".repeat(40));

// Spread (modern)
const withSpread = { ...customer, city: "Addis Ababa", phone: "+251 910 607 442" };

// Object.assign (older)
const withAssign = Object.assign({}, customer, {
    city: "Addis Ababa",
    phone: "+251 910 607 442"
});

console.log("Spread result:", withSpread);
console.log("Object.assign result:", withAssign);
console.log("✅ Both produce the same result!");

// ============================================
// 6. Spread with arrays (bonus)
// ============================================

console.log("\n📊 SPREAD WITH ARRAYS");
console.log("-".repeat(40));

const originalArray = [1, 2, 3, 4, 5];
const newArray = [...originalArray, 6, 7, 8];

console.log("Original array:", originalArray);
console.log("New array:", newArray);
console.log("✅ Original array is unchanged!");