from fastapi import FastAPI
from app.routers import todo


# Factory App
def create_app():
    app = FastAPI()

    app.include_router(todo.router)

    return app
