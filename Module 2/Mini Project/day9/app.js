// ============================================
// Addis Market - Shopping List App
// ============================================

// ============================================
// Cache DOM references (query once, reuse)
// ============================================
const form = document.getElementById('itemForm');
const itemNameInput = document.getElementById('itemName');
const itemPriceInput = document.getElementById('itemPrice');
const itemList = document.getElementById('itemList');
const totalAmount = document.getElementById('totalAmount');

// ============================================
// State
// ============================================
let items = [];

// ============================================
// Functions
// ============================================

/**
 * Calculate and update the total price of all items
 */
function updateTotal() {
    const total = items.reduce((sum, item) => sum + item.price, 0);
    totalAmount.textContent = total.toFixed(2);
}

/**
 * Render the shopping list (create elements, not innerHTML)
 */
function renderList() {
    // Clear the list (but keep the empty message if needed)
    const emptyMsg = itemList.querySelector('.empty-message');
    itemList.innerHTML = '';

    if (items.length === 0) {
        // Show empty message
        const li = document.createElement('li');
        li.className = 'empty-message';
        li.textContent = '📭 No items yet. Add your first item above!';
        itemList.appendChild(li);
        return;
    }

    // Render each item as a row using createElement
    items.forEach((item, index) => {
        // Create <li>
        const li = document.createElement('li');
        li.dataset.index = index;

        // If item is bought, add the class
        if (item.bought) {
            li.classList.add('bought');
        }

        // ----- Item Info (name + price + badge) -----
        const itemInfo = document.createElement('div');
        itemInfo.className = 'item-info';

        // Name span
        const nameSpan = document.createElement('span');
        nameSpan.className = 'item-name';
        nameSpan.textContent = item.name;

        // Price span
        const priceSpan = document.createElement('span');
        priceSpan.className = 'item-price';
        priceSpan.textContent = `${item.price.toFixed(2)} ETB`;

        // Bought badge
        const badge = document.createElement('span');
        badge.className = 'bought-badge';
        badge.textContent = '✅ Bought';

        // Assemble item info
        itemInfo.appendChild(nameSpan);
        itemInfo.appendChild(priceSpan);
        itemInfo.appendChild(badge);

        // ----- Delete Button -----
        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'delete-btn';
        deleteBtn.textContent = '✕ Delete';
        deleteBtn.dataset.index = index;

        // ----- Assemble row -----
        li.appendChild(itemInfo);
        li.appendChild(deleteBtn);

        // ----- Add to list -----
        itemList.appendChild(li);
    });
}

/**
 * Add a new item
 */
function addItem(name, price) {
    const newItem = {
        name: name.trim(),
        price: parseFloat(price),
        bought: false
    };

    items.push(newItem);
    renderList();
    updateTotal();
}

/**
 * Delete an item by index
 */
function deleteItem(index) {
    items.splice(index, 1);
    renderList();
    updateTotal();
}

/**
 * Toggle bought state by index
 */
function toggleBought(index) {
    items[index].bought = !items[index].bought;
    renderList();
}

/**
 * Reset the form
 */
function resetForm() {
    itemNameInput.value = '';
    itemPriceInput.value = '';
    itemNameInput.focus();
}

// ============================================
// Event Listeners
// ============================================

// ----- Form Submission (add item) -----
form.addEventListener('submit', function(event) {
    // 1. Prevent page refresh
    event.preventDefault();

    // 2. Read and validate inputs
    const name = itemNameInput.value.trim();
    const price = parseFloat(itemPriceInput.value);

    if (name === '') {
        alert('Please enter an item name!');
        itemNameInput.focus();
        return;
    }

    if (isNaN(price) || price <= 0) {
        alert('Please enter a valid price (positive number)!');
        itemPriceInput.focus();
        return;
    }

    // 3. Add the item
    addItem(name, price);

    // 4. Clear the form
    resetForm();

    console.log(`✅ Added: ${name} - ${price.toFixed(2)} ETB`);
});

// ----- SINGLE DELEGATED LISTENER on the list container -----
// Handles BOTH delete and toggle (buy) actions
itemList.addEventListener('click', function(event) {
    // Find the closest <li> (the row)
    const li = event.target.closest('li');

    // If no <li> or it's the empty message, ignore
    if (!li || li.classList.contains('empty-message')) {
        return;
    }

    // Get the index from the dataset
    const index = parseInt(li.dataset.index, 10);

    // If index is invalid, ignore
    if (isNaN(index) || index < 0 || index >= items.length) {
        return;
    }

    // ----- Check what was clicked -----
    const isDeleteBtn = event.target.classList.contains('delete-btn');

    if (isDeleteBtn) {
        // DELETE: Remove the item
        const itemName = items[index].name;
        deleteItem(index);
        console.log(`🗑️ Removed: ${itemName}`);
    } else {
        // TOGGLE: Click anywhere else on the row toggles "bought" state
        toggleBought(index);
        const item = items[index];
        console.log(`🔄 Toggled: ${item.name} → ${item.bought ? '✅ Bought' : '❌ Not bought'}`);
    }
});

// ----- Allow Enter key to submit (built into form) -----

// ============================================
// Initial Render
// ============================================
renderList();
updateTotal();

console.log('🛒 Addis Market Shopping List ready!');
console.log(`📊 Initial items: ${items.length}`);
console.log('💡 Click a row to toggle "bought" state');
console.log('💡 Click Delete to remove an item');