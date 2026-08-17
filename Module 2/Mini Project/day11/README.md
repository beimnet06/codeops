# 📝 Addis Market Signup Form

A validated, persistent signup form for Addis Market.

## 🚀 What It Does

- Accepts a **name** (at least 2 characters)
- Accepts an **Ethiopian phone number** (09xxxxxxxx or +2519xxxxxxxx)
- Shows **clear error messages** for invalid input
- **Saves valid entries** to localStorage as JSON
- **Restores entries** on page reload
- Shows **total signups** and **recent signups** list

## 📁 Files

| File | Responsibility |
|------|----------------|
| `index.html` | HTML structure |
| `styles.css` | All styling |
| `app.js` | JavaScript logic |
| `README.md` | This file |

## 🎯 Features

- ✅ `preventDefault` on submit
- ✅ Input values trimmed before validation
- ✅ Name: at least 2 characters
- ✅ Phone: regex `^(?:\+251|0)9\d{8}$`
- ✅ Clear error messages with `textContent`
- ✅ localStorage persistence with JSON
- ✅ Null and corrupt data handling with `try/catch`

## 🚀 How to Run

1. Open `index.html` in a browser
2. Fill in your name and phone
3. Click **Sign Up**
4. Valid entries are saved and displayed

## 📸 Screenshot

[Add a screenshot here]

## 📂 Project Structure
