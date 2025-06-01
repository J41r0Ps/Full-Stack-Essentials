from fastapi import FastAPI
import random
app = FastAPI()

jokes = [
    {"text": "Why do programmers prefer dark mode? Because light attracts bugs!", "category": "tech"},
    {"text": "Why did the database break up with the application? It had too many connections.", "category": "tech"},
    {"text": "What do you call a bear with no teeth? A gummy bear.", "category": "animal"},
    {"text": "Why did the chicken join a band? Because it had the drumsticks.", "category": "animal"},
    {"text": "I'm reading a book on anti-gravity. It's impossible to put down!", "category": "general"},
    {"text": "Did you hear about the mathematician who’s afraid of negative numbers? He'll stop at nothing to avoid them.", "category": "general"},
    {"text": "Why did the dog sit in the shade? Because it didn’t want to be a hot dog.", "category": "animal"},
    {"text": "Why was the JavaScript developer sad? Because they didn’t Node how to Express themselves.", "category": "tech"},
]

@app.get("/joke")
def get_joke(category : str = None):
    if category:
        filtered_jokes = []
        for joke in jokes:
            if joke["category"] == category:
                filtered_jokes.append(joke)
        if not filtered_jokes:
            return {"error":"Category not found"}
        return random.choice(filtered_jokes)
    return random.choice(jokes)