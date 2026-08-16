from sqlalchemy.orm import Session
from contextvars import ContextVar

SESSION: ContextVar[Session | None] = ContextVar('session', default=None)
CURRENT_USER: ContextVar[int | None] = ContextVar('current_user', default=None)

def set_session(session: Session):
    SESSION.set(session)

def get_session() -> Session:
    session =  SESSION.get('session')

    if not isinstance(session, Session):
        raise Exception("Session is not defined.")

    return session

def set_current_user(user_id: int):
    CURRENT_USER.set(user_id)

def get_current_user() -> int:
    user_id =  CURRENT_USER.get('current_user')

    if not isinstance(user_id, int):
        raise Exception("Current user is not defined.")
    
    return user_id

