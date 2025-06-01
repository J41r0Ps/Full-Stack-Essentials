# Exercise 1: Random Joke Generator API

## Objective

Build a FastAPI endpoint that serves random jokes, optionally filtered by category.

## Requirements

✅ Create a `main.py`  
✅ Add a GET `/joke/` endpoint  
✅ Use a list of predefined jokes, each with:
- Text
- Category (e.g., "tech", "animal", "general")

✅ If no query parameter → return a random joke  
✅ If query parameter `category` is provided → return a random joke from that category  
✅ If category does not exist → return:
```json
{ "error": "Category not found" }