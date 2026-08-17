// ============================================
// Weather App - JavaScript
// ============================================

// ============================================
// DOM References
// ============================================

const cityInput = document.getElementById('cityInput');
const searchBtn = document.getElementById('searchBtn');
const statusEl = document.getElementById('status');
const weatherData = document.getElementById('weatherData');
const errorEl = document.getElementById('error');
const cityName = document.getElementById('cityName');
const temp = document.getElementById('temp');
const condition = document.getElementById('condition');
const humidity = document.getElementById('humidity');
const wind = document.getElementById('wind');
const feelsLike = document.getElementById('feelsLike');

// ============================================
// API Function
// ============================================

async function getWeather(city) {
    // Show loading
    statusEl.textContent = '⏳ Loading weather data...';
    weatherData.classList.add('hidden');
    errorEl.classList.add('hidden');

    try {
        const url = `https://goweather.herokuapp.com/weather/${encodeURIComponent(city)}`;
        const response = await fetch(url);

        // Check res.ok
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();

        // Check if city was found
        if (data.temperature === undefined || data.temperature === null) {
            throw new Error('City not found. Please check the spelling.');
        }

        // Display weather
        displayWeather(data, city);

    } catch (error) {
        // Show error
        errorEl.textContent = `❌ ${error.message}`;
        errorEl.classList.remove('hidden');
        statusEl.textContent = '❌ Something went wrong';
        console.error('Error:', error);
    }
}

// ============================================
// Display Weather Data
// ============================================

function displayWeather(data, city) {
    // Extract data
    const tempC = data.temperature || 'N/A';
    const conditionText = data.description || 'No description';
    const humidityVal = data.humidity || 'N/A';
    const windVal = data.wind || 'N/A';

    // Extract feels like from forecast if available
    let feelsLikeVal = 'N/A';
    if (data.forecast && data.forecast.length > 0) {
        feelsLikeVal = data.forecast[0].temperature || 'N/A';
    }

    // Update DOM
    cityName.textContent = city.charAt(0).toUpperCase() + city.slice(1);
    temp.textContent = tempC;
    condition.textContent = conditionText;
    humidity.textContent = humidityVal;
    wind.textContent = windVal;
    feelsLike.textContent = feelsLikeVal;

    // Show weather data
    weatherData.classList.remove('hidden');
    statusEl.textContent = `✅ Weather data loaded for ${city}`;

    console.log('✅ Weather data loaded:', { city, tempC, conditionText });
}

// ============================================
// Event Listeners
// ============================================

searchBtn.addEventListener('click', function() {
    const city = cityInput.value.trim();
    if (city) {
        getWeather(city);
    } else {
        errorEl.textContent = '❌ Please enter a city name.';
        errorEl.classList.remove('hidden');
        statusEl.textContent = '⚠️ Enter a city name';
    }
});

cityInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        searchBtn.click();
    }
});

// ============================================
// Default City on Load
// ============================================

// Load weather for Addis Ababa by default
cityInput.value = 'Addis Ababa';
getWeather('Addis Ababa');

console.log('✅ Weather App ready!');
console.log('🌤️ Default city: Addis Ababa');