# 🌍 Country Facts Explorer

A single-page app that fetches and displays country facts using the free **restcountries.com** API.

## 🚀 Features

- Search for any country by name
- Displays: capital, population, region, currencies, languages, time zones, and flag
- Defaults to Ethiopia on first load
- Loading, success, and error states

## 📁 Files

| File | Responsibility |
|------|----------------|
| `index.html` | HTML structure |
| `styles.css` | All styling |
| `app.js` | JavaScript logic (fetch, render, states) |

## 🔗 API Used

- [restcountries.com](https://restcountries.com/v3.1/name/{country})

## 🎯 Requirements Met

| Requirement | Status |
|-------------|--------|
| Async function with `fetch` | ✅ |
| Loading state during request | ✅ |
| `res.ok` check for HTTP errors | ✅ |
| `try/catch` for network errors | ✅ |
| Render: capital, population, region, currencies, flag | ✅ |
| Default to Ethiopia on first load | ✅ |
| Population formatted with commas | ✅ |

## 🚀 How to Run

1. Open `index.html` in a browser
2. Enter a country name (default is Ethiopia)
3. Click "Search" or press Enter

## 📸 Screenshot

[Add a screenshot here]

## 📂 Project Structure
