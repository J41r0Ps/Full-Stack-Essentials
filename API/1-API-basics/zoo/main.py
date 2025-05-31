from fastapi import FastAPI
from random import choice

app = FastAPI()

all_animals = ["badger", "lion", "wolf", "porcupine", "cheetah", "giraffe", "panda", "gorilla", "tiger", "koala",
               "jaguar", "elephant", "blue-and-yellow macaw", "hornbill", "rhinoceros", "kangaroo", "ostridge", "bison",
               "wallaby"]
print("test")
gender = ["male", "female"]


@app.get("/zoo")
def get_zoo(number: int = 5):
    if number <= 0: return {"error": f"A number above 0 must be given. Provided number : {number}"}
    elif number > len(all_animals) : return {"error": f"You asked for more animals than available. Provided number: {number} - Available number: {len(all_animals)}"}
    available_animals = all_animals.copy()
    list_animals = []

    for i in range(number):
        species = choice(available_animals)
        dict_animal = {
            "number": i + 1,
            "species": species,
            "sex": choice(gender)
        }
        list_animals.append(dict_animal)
        available_animals.remove(species)
    return {"animals":list_animals}