from fastapi import FastAPI

app= FastAPI()

@app.post('/blog')
def blog(title,age):
    return {'title': title, 'age': age}