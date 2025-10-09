from fastapi import FastAPI
from git import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {"name": "peddireddy","age": 2000,"marks": {
        "maths": 2024,
        "science": 2222
    }}


@app.get('/about')
def about():
    return {"about": "I am A Best Learning with Concsistency"}


@app.get('/contat')
def contact():
    return f"Thank you Hari , For Logging In "

@app.get('/list/{id}')
def resut(id):
    return f"my Name is {id}"

@app.get('/blog')
def index1(limit):
    return f"I have entered {limit} Query Parameters "


@app.get('/logs')
def index2(limit,published: bool):
    if published:
        return f"The Published Blogs Number Count is {limit}"
    else:
        return f"The Blogs Count is {limit}"
    

class Blog(BaseModel):
    title: str
    body: str


@app.post('/blog')
def blog(request:Blog):
    return request
    return {'data': "Blog is Created Successfully"}