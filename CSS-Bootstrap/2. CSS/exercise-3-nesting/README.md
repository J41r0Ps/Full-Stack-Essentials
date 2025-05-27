# Exercise 3: CSS Nesting

## Objective

Practice writing nested CSS selectors to structure your styles more cleanly.

## Tasks

✅ Create an `index.html` and `style.css`  
✅ In your HTML, set up:
- A `.card` container
    - Inside, a `.card-title`
    - A `.card-content` with a `<p>` element
    - A `.card-footer` with a `<button>`

✅ In your CSS, use **nested selectors** (following course style — no SCSS, just combined selectors) to:
- Style `.card` and its child elements
- Make sure `.card-title` is larger and bold
- Style the `<p>` only inside `.card-content`
- Add hover effects on the `<button>` only inside `.card-footer`

---

### 💡 Example selector:
```css
.card .card-content p {
    color: darkgray;
}
