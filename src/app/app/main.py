from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from .api import weather
from .views import home

app = FastAPI()


def configure():
    configure_routing()


def configure_routing():
    app.mount('/static', StaticFiles(directory='./app/static'), name='static')
    app.include_router(home.router)
    app.include_router(weather.router)


if __name__ == '__main__':
    configure()
else:
    configure()