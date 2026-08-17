// ============================================
// Day 11 Mini Project: Validated, Persistent Signup Form
// ============================================

// ============================================
// DOM References (cached once)
// ============================================
const form = document.getElementById('signupForm');
const nameInput = document.getElementById('nameInput');
const phoneInput = document.getElementById('phoneInput');
const errorArea = document.getElementById('errorArea');
const countDisplay = document.getElementById('countDisplay');
const signupList = document.getElementById('signupList');

const STORAGE_KEY = 'addisMarketSignups';

// ============================================
// Helper: Load signups from localStorage
// ============================================

function loadSignups() {
    try {
        const data = localStorage.getItem(STORAGE_KEY);

        // Guard: null data
        if (data === null) {
            return [];
        }

        // Parse JSON
        const parsed = JSON.parse(data);

        // Guard: corrupt data (not an array)
        if (!Array.isArray(parsed)) {
            console.warn('Corrupt data detected, resetting.');
            return [];
        }

        return parsed;

    } catch (error) {
        console.error('Error loading signups:', error);
        return [];
    }
}

// ============================================
// Helper: Save signups to localStorage
// ============================================

function saveSignups(signups) {
    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(signups));
        return true;
    } catch (error) {
        console.error('Error saving signups:', error);
        return false;
    }
}

// ============================================
// Helper: Validate Ethiopian phone number
// ============================================

function isValidEthiopianPhone(phone) {
    // Accepts: 0912345678 or +251912345678
    const regex = /^(?:\+251|0)9\d{8}$/;
    return regex.test(phone);
}

// ============================================
// Helper: Render signups list
// ============================================

function renderSignups() {
    const signups = loadSignups();

    // Update count
    countDisplay.textContent = signups.length;

    // Clear list
    signupList.innerHTML = '';

    if (signups.length === 0) {
        const li = document.createElement('li');
        li.className = 'empty-message';
        li.textContent = 'No signups yet. Be the first!';
        signupList.appendChild(li);
        return;
    }

    // Show last 5 signups (most recent first)
    const recent = signups.slice(-5).reverse();

    recent.forEach(entry => {
        const li = document.createElement('li');
        li.innerHTML = `
            <span class="name">${escapeText(entry.name)}</span>
            <span class="phone">${escapeText(entry.phone)}</span>
        `;
        signupList.appendChild(li);
    });
}

// ============================================
// Helper: Escape text for security
// ============================================

function escapeText(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// ============================================
// Form Submit Handler
// ============================================

form.addEventListener('submit', function(event) {
    // 1. Prevent default (no page reload)
    event.preventDefault();

    // 2. Clear previous errors
    errorArea.textContent = '';
    errorArea.className = '';

    // 3. Read trimmed values
    const name = nameInput.value.trim();
    const phone = phoneInput.value.trim();

    // 4. Validate: name at least 2 characters
    if (name.length < 2) {
        errorArea.textContent = '❌ Name must be at least 2 characters long.';
        errorArea.className = 'error';
        nameInput.focus();
        return;
    }

    // 5. Validate: phone against Ethiopian regex
    if (!isValidEthiopianPhone(phone)) {
        errorArea.textContent = '❌ Phone must be in format: 09xxxxxxxx or +2519xxxxxxxx';
        errorArea.className = 'error';
        phoneInput.focus();
        return;
    }

    // 6. Success: save to localStorage
    const signups = loadSignups();
    signups.push({
        name: name,
        phone: phone,
        signedAt: new Date().toISOString()
    });

    if (!saveSignups(signups)) {
        errorArea.textContent = '❌ Failed to save. Please try again.';
        errorArea.className = 'error';
        return;
    }

    // 7. Clear the form
    nameInput.value = '';
    phoneInput.value = '';

    // 8. Show success message
    errorArea.textContent = '✅ Signup successful! Welcome to Addis Market!';
    errorArea.className = 'success';

    // 9. Update the UI
    renderSignups();

    // 10. Focus back on name input
    nameInput.focus();

    console.log('✅ New signup:', { name, phone });
});

// ============================================
// Load and render on page load
// ============================================

renderSignups();

// ============================================
// Console Log
// ============================================

console.log('✅ Day 11 Mini Project ready!');
console.log('📝 Signup form with localStorage persistence.');
console.log('📌 Phone validation: 09xxxxxxxx or +2519xxxxxxxx');
console.log(`👥 Total signups: ${loadSignups().length}`);
console.log('💡 Data persists after page reload!');