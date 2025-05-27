# Exercise 2: CSS Variables

## Objective

Learn to define and use CSS variables to make your styles more reusable and maintainable.

## Tasks

✅ Create an `index.html` and `style.css`  
✅ In your CSS, define variables for:
- A primary color (e.g., --primary-color)
- A secondary color (e.g., --secondary-color)
- A main font size (e.g., --main-font-size)

✅ Apply these variables in styles:
- Set the background color of a container
- Use the font size for text elements
- Apply the secondary color to links or buttons

✅ Override a variable in a child selector (for example, change the primary color inside a `.box`)

---

### 💡 Example variables:
```css
:root {
    --primary-color: #3498db;
    --secondary-color: #2ecc71;
    --main-font-size: 18px;
}
