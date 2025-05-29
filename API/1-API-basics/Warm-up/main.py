from fastapi import FastAPI

app = FastAPI()

@app.get("/song/me")
def favorite_song_me():
    return {"artist": "Against The Current",
            "title": "Weapon"}

@app.get("/song/neighbour")
def favorite_song_neighbour():
    return {"artist": "Dua Lipa",
            "title": "Physical"}