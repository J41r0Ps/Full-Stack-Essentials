# Frontend: Contact Form (PHP + Bootstrap + Custom CSS)

✅ **Goal**
Create a stylish and functional contact page  
that covers everything you practiced in:
- Bootstrap 5.3 components
- Advanced CSS techniques
- JavaScript validation

---

## 🔧 Requirements

✅ **Structure**
- Use PHP as your main `.php` page (not just HTML)
- Include:
    - Bootstrap 5.3 via CDN
    - FontAwesome icons via CDN
    - External CSS file (style.css) with:
        - Custom color variables
        - Nested selectors

✅ **Page Elements**
- **Header**
    - Simple header section with the project logo or title
- **Contact Form**
    - Fields:
        - Full Name
        - Email
        - Phone Number
        - Subject (dropdown: e.g., General, Support, Feedback)
        - Message (textarea)
    - Submit button with FontAwesome icon

✅ **Styling**
- Use Bootstrap classes for:
    - Grids
    - Buttons
    - Form controls
    - Alerts (for validation messages, if needed)
- Customize at least **two things** using your own CSS variables:
    - Example: button colors, alert background, or card shadow
- Write CSS in a **nested style** (mimicking what was taught in the course)

✅ **Form Validation (JavaScript)**
- All fields required
- Email format must be valid
- Show validation feedback using Bootstrap alerts or inline messages

---

## 📁 File Structure


```
/frontend_javascript_contact/
├── index.php → main page
├── style.css → custom nested + variables CSS
```


---

## 🎨 CSS Details

✅ Use:
- CSS variables for at least:
    - Custom primary color
    - Custom secondary color

✅ Nesting (example):
```css
form {
    input, select, textarea {
        border-radius: 8px;
    }
    button {
        background-color: var(--primary-color);
    }
}
````
✅ Customize Bootstrap:

Override `.btn-primary` and `.alert-primary` with your own colors

## 🛠 Build Steps
1️⃣ Build HTML/PHP structure \
2️⃣ Add Bootstrap + FontAwesome \
3️⃣ Write custom CSS (variables + nesting) \
4️⃣ Add JavaScript form validation \
5️⃣ Prepare empty fetch() POST (to connect later)