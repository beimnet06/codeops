// ============================================
// Day 7 Mini Project: TeleBirr Loyalty Points
// ============================================

function createLoyaltyAccount(customerName, earnRule = defaultEarnRule) {
    // PRIVATE: Cannot be accessed from outside
    let points = 0;
    let totalSpent = 0;
    
    function defaultEarnRule(amount) {
        return Math.floor(amount / 10);
    }
    
    function calculatePoints(amount, rule) {
        return rule(amount);
    }
    
    return {
        getName: function() {
            return customerName;
        },
        
        getTotalSpent: function() {
            return totalSpent;
        },
        
        earn: function(amount) {
            if (amount <= 0) {
                console.log("❌ Amount must be positive");
                return false;
            }
            
            const earnedPoints = calculatePoints(amount, earnRule);
            points += earnedPoints;
            totalSpent += amount;
            
            console.log(`✅ ${customerName} earned ${earnedPoints} points`);
            return earnedPoints;
        },
        
        redeem: function(amount) {
            if (amount <= 0) {
                console.log("❌ Redeem amount must be positive");
                return false;
            }
            
            if (amount > points) {
                console.log(`❌ Insufficient points! Have ${points}, need ${amount}`);
                return false;
            }
            
            points -= amount;
            console.log(`✅ ${customerName} redeemed ${amount} points`);
            return true;
        },
        
        balance: function() {
            return points;
        }
    };
}

// Earn Rules (Higher-Order Functions)
function defaultEarnRule(amount) {
    return Math.floor(amount / 10);
}

function holidayEarnRule(amount) {
    return Math.floor(amount / 10) * 2;
}

function premiumEarnRule(amount) {
    return Math.floor(amount / 10) * 3;
}

module.exports = {
    createLoyaltyAccount,
    defaultEarnRule,
    holidayEarnRule,
    premiumEarnRule
};