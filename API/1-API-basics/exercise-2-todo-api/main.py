from fastapi import FastAPI

todos = [
    {"title": "Learn FastAPI", "description": "Complete the FastAPI tutorial", "completed": False},
    {"title": "Write report", "description": "Finish the API section report", "completed": True},
    {"title": "Exercise", "description": "Go for a 30 min walk", "completed": False},
    {"title": "Read book", "description": "Read 20 pages of a novel", "completed": True},
    {"title": "Clean room", "description": "Organize desk and vacuum", "completed": False},
]

app = FastAPI()

@app.get("/todos")
def get_todos(limit: int = None, completed : bool = False):
    filtered = todos
    if completed is not None:
        for todo in todos:
            if todo["completed"] == completed : filtered.append(todo)

    if limit is not None:
        if limit > len(filtered):
            return {"warning": "Limit exceeds available items"}
        filtered = filtered[:limit]

    return {"todos": filtered}