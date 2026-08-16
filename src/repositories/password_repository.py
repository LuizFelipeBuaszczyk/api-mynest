
from sqlalchemy import text
from sqlalchemy.orm import session
from models.passwords import Passwords
from utils.contextvars import get_session

class PasswordRepository:
    
    @staticmethod
    async def list_passwords_by_owner(owner_id: int) -> list[Passwords]:
        session = get_session()

        sql = """
        SELECT id FROM passwords WHERE fk_owner = :fk_owner
        """

        return session.execute(text(sql), {'fk_owner': owner_id}).all()

    @staticmethod
    async def get_password_by_id(id: int) -> Passwords | None:
        session = get_session()

        sql = """
        SELECT id, password, fk_owner FROM passwords WHERE id = :id
        """

        response = session.execute(text(sql), {'id': id}).one_or_none()

        if not response:
            return None

        return Passwords(
            id=response[0],
            password=response[1],
            fk_owner=response[2]
        )


    @staticmethod
    async def insert_password(**data) -> Passwords:
        session = get_session()
        
        password = Passwords(
            password=data['password'],
            fk_owner=data['fk_owner']
        )

        session.add(password)
        return password

