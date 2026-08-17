# 🛒 Addis Market - Shopping List

A single-page interactive shopping list app for Ethiopian markets.

## 🚀 Features

- Add items with name and ETB price
- Click row to toggle "bought" state
- Delete items with a single click
- Live running total updates automatically

## 📁 Files

| File | Responsibility |
|------|----------------|
| `index.html` | HTML structure |
| `styles.css` | All styling |
| `app.js` | JavaScript logic |

## 🔧 How It Works

- **Event Delegation**: A single listener on the `<ul>` handles all delete and toggle actions
- **preventDefault**: The form adds items without refreshing the page
- **createElement**: Items are rendered using `createElement` and `appendChild` (no `innerHTML` strings)
- **State Management**: Items stored in an array, re-rendered on updates

## 🎯 Requirements Met

| Requirement | Status |
|-------------|--------|
| Add item with name and price | ✅ |
| `preventDefault` on form submit | ✅ |
| Validation for both fields | ✅ |
| Render with `createElement` (not `innerHTML`) | ✅ |
| Single delegated listener on parent | ✅ |
| Toggle "bought" class on row click | ✅ |
| Live running total updates | ✅ |
| Cache DOM references once | ✅ |

## 📸 Screenshot

[Add a screenshot here]

## 📂 Project Structure
