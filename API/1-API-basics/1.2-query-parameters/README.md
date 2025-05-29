# Exercise 2: Using Query Parameters

## Objective

Learn how to accept and handle query parameters in a FastAPI GET request.

## Tasks

✅ In your `main.py`, add a new route:

## /items/

✅ The route should accept:
- A required `item_id` (integer)
- An optional `q` (string)

✅ Example:

## /items/?item_id=42&q=test

✅ The endpoint should return:
```json
{
    "item_id": 42,
    "q": "test"
}
