// ============================================
// Country Facts Explorer - App
// ============================================

// ============================================
// DOM References (cached once)
// ============================================
const form = document.getElementById('searchForm');
const countryInput = document.getElementById('countryInput');
const resultsDiv = document.getElementById('results');

// ============================================
// API Base URL
// ============================================
const API_URL = 'https://restcountries.com/v3.1/name/';

// ============================================
// Helper: Format population with commas
// ============================================
function formatPopulation(population) {
    return population.toLocaleString();
}

// ============================================
// Helper: Format currencies
// ============================================
function formatCurrencies(currencies) {
    if (!currencies) return 'N/A';
    const names = Object.values(currencies).map(c => c.name);
    return names.join(', ');
}

// ============================================
// Helper: Get flag emoji
// ============================================
function getFlag(countryData) {
    return countryData.flags?.emoji || '🏳️';
}

// ============================================
// Render Functions
// ============================================

// --- IDLE State ---
function renderIdle() {
    resultsDiv.innerHTML = `
        <div class="idle-state">
            <span class="icon">🔍</span>
            <h3>Search for a country</h3>
            <p>Enter a country name above to get started.</p>
        </div>
    `;
}

// --- LOADING State ---
function renderLoading() {
    resultsDiv.innerHTML = `
        <div class="loading-state">
            <div class="spinner"></div>
            <span>Loading country data...</span>
        </div>
    `;
}

// --- ERROR State ---
function renderError(message) {
    resultsDiv.innerHTML = `
        <div class="error-state">
            <span class="icon">❌</span>
            <h3>Something went wrong</h3>
            <p>${message}</p>
        </div>
    `;
}

// --- SUCCESS State ---
function renderCountry(data) {
    // The API returns an array, take the first result
    const country = data[0];

    const name = country.name.common;
    const officialName = country.name.official;
    const flag = getFlag(country);
    const capital = country.capital?.[0] || 'N/A';
    const population = formatPopulation(country.population);
    const region = country.region || 'N/A';
    const subregion = country.subregion || '';
    const currencies = formatCurrencies(country.currencies);
    const languages = country.languages ? Object.values(country.languages).join(', ') : 'N/A';
    const timezones = country.timezones?.[0] || 'N/A';

    const regionDisplay = subregion ? `${region} (${subregion})` : region;

    resultsDiv.innerHTML = `
        <div class="country-card">
            <span class="flag">${flag}</span>
            <div class="country-name">${name}</div>
            <div class="official-name">${officialName}</div>
            <hr class="divider" />
            <div class="fact-grid">
                <div class="fact-item">
                    <div class="label">Capital</div>
                    <div class="value">${capital}</div>
                </div>
                <div class="fact-item">
                    <div class="label">Population</div>
                    <div class="value">${population}</div>
                </div>
                <div class="fact-item">
                    <div class="label">Region</div>
                    <div class="value">${regionDisplay}</div>
                </div>
                <div class="fact-item">
                    <div class="label">Currencies</div>
                    <div class="value">${currencies}</div>
                </div>
                <div class="fact-item">
                    <div class="label">Languages</div>
                    <div class="value">${languages}</div>
                </div>
                <div class="fact-item">
                    <div class="label">Time Zone</div>
                    <div class="value">${timezones}</div>
                </div>
            </div>
        </div>
    `;
}

// ============================================
// Fetch Country Data
// ============================================

async function fetchCountry(countryName) {
    // Show LOADING state
    renderLoading();

    try {
        // Build URL with proper encoding
        const url = `${API_URL}${encodeURIComponent(countryName)}`;

        // 1. Fetch from API
        const response = await fetch(url);

        // 2. Check HTTP status (res.ok)
        if (!response.ok) {
            if (response.status === 404) {
                throw new Error(`"${countryName}" not found. Please check the spelling.`);
            } else {
                throw new Error(`HTTP Error ${response.status}: ${response.statusText}`);
            }
        }

        // 3. Parse JSON
        const data = await response.json();

        // 4. Validate data
        if (!data || data.length === 0) {
            throw new Error(`No data found for "${countryName}".`);
        }

        // 5. Render the country data
        renderCountry(data);

        console.log(`✅ Fetched data for: ${countryName}`);

    } catch (error) {
        // 6. Show ERROR state
        renderError(error.message);
        console.error('❌ Error:', error.message);
    }
}

// ============================================
// Event Handlers
// ============================================

// --- Form Submit ---
form.addEventListener('submit', function(event) {
    event.preventDefault();

    const countryName = countryInput.value.trim();

    if (countryName === '') {
        renderError('Please enter a country name.');
        return;
    }

    fetchCountry(countryName);
});

// --- Allow Enter key (built into form) ---

// ============================================
// Initial Load: Default to Ethiopia
// ============================================

// Load Ethiopia on page load
fetchCountry('Ethiopia');

// ============================================
// Console Log
// ============================================

console.log('🌍 Country Facts Explorer ready!');
console.log('📌 Default country: Ethiopia');
console.log('💡 Search for any country to get its facts.');
console.log('🔗 API: restcountries.com');