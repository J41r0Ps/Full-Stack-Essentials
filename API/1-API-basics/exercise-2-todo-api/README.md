# Exercise 2: Simple To-Do API

## Objective

Build a FastAPI endpoint that serves a list of to-do items with filtering and limiting.

## Requirements

✅ Create a `main.py`  
✅ Add a GET `/todos/` endpoint  
✅ Use a predefined list of to-dos:
- Each item has: `title`, `description`, `completed` (True/False)

✅ Support optional query parameters:
- `completed` (bool) → filter by completed status
- `limit` (int) → limit the number of items returned

✅ If `limit` exceeds available items → return a warning:
```json
{ "warning": "Limit exceeds available items" }
