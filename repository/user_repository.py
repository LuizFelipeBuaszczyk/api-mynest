from sqlalchemy import select
from sqlalchemy.orm import Session
from model.user import User

class UserRepository:
    _session: Session

    def __init__(self, session):
        self._session = session 

    async def find_user_by_username(self, username: str) -> User:
        stmt = (
            select(User)
            .where(
                User.username == username
            )
        )

        return self._session.execute(stmt).scalar_one_or_none()
        