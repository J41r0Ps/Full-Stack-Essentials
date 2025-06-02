from fastapi import FastAPI
import config
import database
from models import models
from queries import festival_queries as queries

app = FastAPI(docs_url=config.documentation_url)

@app.get("/")
def get_hello():
    return {"hello":"works"}
@app.post("/festivals")
def create_festival(festival: models.Festival):
    query = queries.insert_festival_query
    success = database.execute_sql_query(query,(
        festival.name,
        festival.location,
        festival.startDate,
        festival.endDate,
        festival.province,
        festival.comment,
    ))
    if success == True:
        return festival
    else:
        return {"error": "Could not insert festival"}