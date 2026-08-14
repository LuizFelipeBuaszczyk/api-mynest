from sqlalchemy.orm import Session
from contextvars import ContextVar

SESSION: ContextVar[Session | None] = ContextVar('session', default=None)

def set_session(session: Session):
    SESSION.set(session)

def get_session() -> Session:
    session =  SESSION.get('session')

    if not isinstance(session, Session):
        raise Exception("Session is not defined.")

    return session
