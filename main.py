from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="MyNest API"
)

app.include_router(router)