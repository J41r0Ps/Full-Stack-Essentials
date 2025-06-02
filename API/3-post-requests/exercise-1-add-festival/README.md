# Exercise 1: Add New Festival (POST)

## Objective

Create a POST endpoint that allows adding a new festival  
to the database with full request body validation.

---

## Files to include

✅ `main.py` → FastAPI app + route  
✅ `queries.py` → SQL insert query  
✅ `models.py` → Pydantic request model

✅ You will reuse:
- `.env`
- `config.py`
- `database.py`

---

## Requirements

✅ POST `/festivals/`

✔ Request body:
```json
{
    "name": "Summer Fest",
    "location": "Brussels",
    "startDate": "2024-06-15",
    "endDate": "2024-06-17",
    "province": "Flemish Brabant",
    "comment": "Annual summer music festival"
}
