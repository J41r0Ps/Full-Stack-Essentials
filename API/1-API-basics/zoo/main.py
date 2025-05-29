from fastapi import FastAPI
from random import randint
from random import choice

all_animals = ["badger", "lion", "wolf", "porcupine", "cheetah", "giraffe", "panda", "gorilla", "tiger", "koala", "jaguar", "elephant", "blue-and-yellow macaw", "hornbill", "rhinoceros", "kangaroo", "ostridge", "bison", "wallaby"]

gender = ["male","female"]

app = FastAPI()

@app.get("/zoo")
def zoo(amount : int = 1 ):
    animals = []
    for i in range(amount):
        animal = {"number": i+1,
                  "species": choice(all_animals),
                  "sex": choice(gender)}
        animals.append(animal)
    return {"animals":animals}