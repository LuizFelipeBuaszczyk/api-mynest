from fastapi import FastAPI
from routes import router

from middlewares.session_db_middleware import SessionDatabaseMiddleware
from exceptions.handler import app_handler_exception
# from exceptions.base_exceptions import APPException TODO Posteriormente criar outro método handler

app = FastAPI(
    title="MyNest API"
)

app.include_router(router)
app.add_middleware(SessionDatabaseMiddleware)
app.add_exception_handler(Exception, app_handler_exception)

