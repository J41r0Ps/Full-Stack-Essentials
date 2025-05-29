from fastapi import FastAPI
from random import randint

app = FastAPI()

@app.get("/percentage/fixedlimit")
def random_number():
    return {"percentage":randint(0,100)}

@app.get("/percentage/limits")
def random_limit_number(lower_limit: int , upper_limit:int):
    if lower_limit > upper_limit:
        return {"error":"The upper limit must be greater than the lower limit!",
                "lower limit": lower_limit,
                "upper limit": upper_limit}
    return {"percentage":randint(lower_limit,upper_limit)}

@app.get("/percentage/multiplereadings")
def random_limit_amount_number(lower_limit: int , upper_limit:int, amount: int = 1):
    if amount <= 0:
        return {"error": "The amount must be greater than 0!",
                "amount": amount}
    elif lower_limit > upper_limit:
        return {"error":"The upper limit must be greater than the lower limit!",
                "lower limit": lower_limit,
                "upper limit": upper_limit}
    percentages = []
    for i in range(amount):
        percentages.append(randint(lower_limit,upper_limit))
    return {"percentage": percentages}
