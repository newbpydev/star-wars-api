
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('/blog')
# def index(published: bool, limit: int = 10,):
# def index(published: bool = True, limit: int = 10,):
def index(published: bool = True, limit: int = 10, sort: Optional[str] = None):
    # return {'data': {'name': 'Juan'}}
    if published:
        return {'data': f'{limit} published blogs from the db '}
    else:
        return {'data': f'{limit} blogs from the db '}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def show(id: int):
    return {'data': ['1', '2']}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is created with title as {request.title}'}


# if __name__ == "__main__":
#     uvicorn.run(app=app, host='127.0.0.1', port='9000')
