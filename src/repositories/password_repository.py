
from utils.logger import get_logger

from sqlalchemy import text
from models.passwords import Passwords
from utils.contextvars import get_session

logger = get_logger(__name__)

class PasswordRepository:
    
    @staticmethod
    async def list_passwords_by_owner(owner_id: int) -> list[Passwords]:
        logger.info("selecting all passwords by owner")
        session = get_session()

        sql = """
        SELECT id, name FROM passwords WHERE fk_owner = :fk_owner
        """

        return session.execute(text(sql), {'fk_owner': owner_id}).all()

    @staticmethod
    async def get_password_by_id(id: int) -> Passwords | None:
        logger.info("select password by id")
        session = get_session()

        sql = """
        SELECT id, password, name, description, fk_owner FROM passwords WHERE id = :id
        """

        response = session.execute(text(sql), {'id': id}).one_or_none()

        if not response:
            return None

        return Passwords(
            id=response[0],
            password=response[1],
            name=response[2],
            description=response[3],
            fk_owner=response[4]
        )


    @staticmethod
    async def insert_password(**data) -> Passwords:
        logger.info("insert password data in db")
        session = get_session()

        password = Passwords(
            password=data['password'],
            name=data['name'],
            description=data['description'],
            fk_owner=data['fk_owner']
        )

        session.add(password)
        return password

