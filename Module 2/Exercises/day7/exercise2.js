// ============================================
// Exercise 2: makeCounter Closure
// ============================================

function makeCounter() {
    // Private variable - cannot be accessed from outside
    let count = 0;
    
    // Return a function that has access to count (closure)
    return function() {
        count++;
        return count;
    };
}

// ============================================
// Testing the closure
// ============================================

console.log("=== COUNTER CLOSURE ===");

// Create a counter
const counter = makeCounter();

console.log("Calling counter():");
console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3
console.log(counter()); // 4
console.log(counter()); // 5

console.log("\nTrying to access count from outside:");
console.log("counter.count:", counter.count); // undefined
console.log("count is not accessible directly!");

// Create a second independent counter
const counter2 = makeCounter();
console.log("\nSecond counter:");
console.log(counter2()); // 1
console.log(counter2()); // 2

console.log("\nFirst counter still has its own count:");
console.log(counter()); // 6 (continues from where it left off)

/*
============================================
EXPLANATION: Why count stays private
============================================

1. JavaScript uses Lexical Scoping:
   - The variable `count` is declared inside `makeCounter()`
   - It is NOT returned or exposed to the outside

2. Closure:
   - The inner function (returned by `makeCounter`) "closes over" `count`
   - It retains access to `count` even after `makeCounter` finishes

3. No Direct Access:
   - `count` is not a property of the returned function
   - It exists only in the closure scope
   - Outside code cannot read or modify it

4. Independent Instances:
   - Each call to `makeCounter()` creates a NEW `count` variable
   - `counter` and `counter2` have separate private counts

This is how JavaScript creates private variables using closures!
*/