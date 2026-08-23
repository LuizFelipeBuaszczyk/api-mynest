from fastapi import  Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from sqlalchemy.orm import sessionmaker

from infra.database import get_engine
from utils.contextvars import set_session

class SessionDatabaseMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next) -> Response:
        
        session = sessionmaker(get_engine())
        with session() as session:
            set_session(session)

            response = await call_next(request)
            if response.status_code // 200 == 1:
                session.commit()

            return response
