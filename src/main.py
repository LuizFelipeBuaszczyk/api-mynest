from fastapi import FastAPI
from routes import router
from middlewares.session_db_middleware import SessionDatabaseMiddleware

app = FastAPI(
    title="MyNest API"
)

app.include_router(router)
app.add_middleware(SessionDatabaseMiddleware)

