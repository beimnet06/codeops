// ============================================
// Birr Watch - App State
// ============================================

// ============================================
// localStorage Helpers
// ============================================

const STORAGE_KEY = 'birrWatchData';

function saveState() {
    try {
        const data = {
            watchlist: state.watchlist,
            lastUpdated: state.lastUpdated
        };
        localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
        console.log('💾 State saved to localStorage');
        return true;
    } catch (error) {
        console.error('❌ Error saving state:', error);
        return false;
    }
}

function loadState() {
    try {
        const stored = localStorage.getItem(STORAGE_KEY);

        if (stored === null) {
            console.log('📭 No saved state found');
            return false;
        }

        const data = JSON.parse(stored);

        if (!data || typeof data !== 'object') {
            console.warn('⚠️ Corrupt data detected, ignoring');
            return false;
        }

        if (data.watchlist && Array.isArray(data.watchlist)) {
            state.watchlist = data.watchlist;
            console.log('📂 Loaded watchlist from localStorage:', state.watchlist);
            return true;
        }

        return false;

    } catch (error) {
        console.error('❌ Error loading state:', error);
        return false;
    }
}

// ============================================
// State Object
// ============================================

const state = {
    rates: {},
    watchlist: ['USD', 'KES', 'GBP'],
    loading: false,
    error: null,
    lastUpdated: null
};

// Try to load saved watchlist
loadState();

// ============================================
// DOM References
// ============================================

const statusEl = document.getElementById('status');
const convertForm = document.getElementById('convertForm');
const amountInput = document.getElementById('amountInput');
const currencySelect = document.getElementById('currencySelect');
const resultEl = document.getElementById('result');
const watchlistEl = document.getElementById('watchlist');
const watchlistInput = document.getElementById('watchlistInput');
const addWatchBtn = document.getElementById('addWatchBtn');

// ============================================
// Load Rates from Live API
// ============================================

async function loadRates() {
    state.loading = true;
    state.error = null;
    updateStatus('loading', '⏳ Fetching live exchange rates...');

    try {
        const response = await fetch('https://api.exchangerate-api.com/v4/latest/ETB');

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();

        state.rates = data.rates;
        state.lastUpdated = new Date().toISOString();
        state.loading = false;

        updateStatus('success', `✅ Rates updated: ${Object.keys(state.rates).length} currencies loaded`);
        render();

        console.log('✅ Rates loaded successfully:', Object.keys(state.rates).length, 'currencies');

    } catch (error) {
        state.loading = false;
        state.error = error.message;
        updateStatus('error', `❌ Failed to load rates: ${error.message}`);
        console.error('❌ Error loading rates:', error);
        render();
    }
}

// ============================================
// Render Function
// ============================================

function render() {
    renderCurrencyDropdown();
    renderWatchlist();
    console.log('✅ render() complete');
}

// ============================================
// Render Currency Dropdown
// ============================================

function renderCurrencyDropdown() {
    currencySelect.innerHTML = '';

    if (state.loading) {
        const option = document.createElement('option');
        option.value = '';
        option.textContent = 'Loading currencies...';
        currencySelect.appendChild(option);
        return;
    }

    if (state.error || Object.keys(state.rates).length === 0) {
        const option = document.createElement('option');
        option.value = '';
        option.textContent = 'No rates available';
        currencySelect.appendChild(option);
        return;
    }

    const placeholder = document.createElement('option');
    placeholder.value = '';
    placeholder.textContent = 'Select currency...';
    currencySelect.appendChild(placeholder);

    const codes = Object.keys(state.rates).sort();

    codes.forEach(code => {
        const option = document.createElement('option');
        option.value = code;
        option.textContent = `${code} — ${state.rates[code].toFixed(4)}`;
        currencySelect.appendChild(option);
    });

    console.log(`✅ Dropdown populated with ${codes.length} currencies`);
}

// ============================================
// Render Watchlist
// ============================================

function renderWatchlist() {
    watchlistEl.innerHTML = '';

    if (state.watchlist.length === 0) {
        const li = document.createElement('li');
        li.className = 'empty-message';
        li.textContent = '⭐ Add currencies to your watchlist';
        watchlistEl.appendChild(li);
        return;
    }

    state.watchlist.forEach(code => {
        const li = document.createElement('li');
        li.dataset.code = code;

        const rate = state.rates[code];
        const rateDisplay = rate ? `1 ETB = ${rate.toFixed(4)} ${code}` : 'Rate unavailable';

        li.innerHTML = `
            <span class="code">${code}</span>
            <span class="rate">${rateDisplay}</span>
            <button class="remove-btn" data-code="${code}">✕</button>
        `;

        watchlistEl.appendChild(li);
    });

    console.log(`✅ Watchlist rendered with ${state.watchlist.length} items`);
}

// ============================================
// Update Status
// ============================================

function updateStatus(type, message) {
    statusEl.textContent = message;
    statusEl.className = type;
}

// ============================================
// Convert Form Handler
// ============================================

convertForm.addEventListener('submit', function(event) {
    event.preventDefault();

    const amount = Number(amountInput.value);

    if (isNaN(amount) || amount <= 0) {
        resultEl.innerHTML = '<span class="error-text">❌ Please enter a valid positive amount.</span>';
        return;
    }

    const currency = currencySelect.value;

    if (!currency) {
        resultEl.innerHTML = '<span class="error-text">❌ Please select a target currency.</span>';
        return;
    }

    const rate = state.rates[currency];

    if (!rate) {
        resultEl.innerHTML = `<span class="error-text">❌ Rate for ${currency} not available.</span>`;
        return;
    }

    const convertedAmount = amount * rate;

    resultEl.innerHTML = `
        💱 <strong>${amount.toFixed(2)} ETB</strong> = 
        <strong class="converted">${convertedAmount.toFixed(2)} ${currency}</strong>
        <br />
        <span style="font-size: 13px; color: #64748b;">
            Rate: 1 ETB = ${rate.toFixed(4)} ${currency}
        </span>
    `;

    console.log(`✅ Converted: ${amount} ETB → ${convertedAmount.toFixed(2)} ${currency}`);
});

// ============================================
// Watchlist Functions
// ============================================

function addToWatchlist() {
    const code = watchlistInput.value.trim().toUpperCase();

    if (!code) {
        resultEl.innerHTML = '<span class="error-text">❌ Please enter a currency code.</span>';
        return;
    }

    if (!state.rates[code]) {
        resultEl.innerHTML = `<span class="error-text">❌ Currency "${code}" not found in rates.</span>`;
        return;
    }

    if (state.watchlist.includes(code)) {
        resultEl.innerHTML = `<span class="error-text">❌ "${code}" is already in your watchlist.</span>`;
        watchlistInput.value = '';
        return;
    }

    state.watchlist.push(code);
    watchlistInput.value = '';
    renderWatchlist();
    saveState();
    resultEl.innerHTML = `✅ Added <strong>${code}</strong> to watchlist.`;
    console.log(`✅ Added ${code} to watchlist`);
}

function removeFromWatchlist(code) {
    const index = state.watchlist.indexOf(code);

    if (index !== -1) {
        state.watchlist.splice(index, 1);
        renderWatchlist();
        saveState();
        resultEl.innerHTML = `✅ Removed <strong>${code}</strong> from watchlist.`;
        console.log(`✅ Removed ${code} from watchlist`);
    }
}

// ============================================
// Event Listeners
// ============================================

addWatchBtn.addEventListener('click', addToWatchlist);

watchlistInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        addToWatchlist();
    }
});

watchlistEl.addEventListener('click', function(event) {
    if (event.target.classList.contains('remove-btn')) {
        const code = event.target.dataset.code;
        if (code) {
            removeFromWatchlist(code);
        }
    }
});

// ============================================
// Load rates on page load
// ============================================

loadRates();

console.log('✅ Birr Watch fully loaded!');
console.log('📊 Watchlist:', state.watchlist);
console.log('💾 Data persists in localStorage.');