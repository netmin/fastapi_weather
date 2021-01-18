from typing import Optional

from fastapi import FastAPI
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates('app/templates')
app.mount('/static', StaticFiles(directory='./app/static'), name='static')


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('home/index.html', {'request': request})

