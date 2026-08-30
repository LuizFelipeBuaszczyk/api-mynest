from utils.logger import get_logger

from sqlalchemy import text, select
from models.users import Users
from utils.contextvars import get_session

logger = get_logger(__name__)

class UserRepository:

    @staticmethod
    async def exists_superuser() -> bool:
        logger.info("exists super user in db")
        session = get_session()
        
        sql = """
        select exists (SELECT 1 FROM users WHERE is_superuser = true) 
        """

        result = session.execute(text(sql)).one()
        
        return result[0]

    @staticmethod
    async def exists_user_by_username(username: str) -> bool:
        logger.info("exists user by username")
        session = get_session()
        
        sql = """
        select exists (SELECT 1 FROM users WHERE username = :username) 
        """

        result = session.execute(text(sql), {'username': username}).one()
        
        return result[0]

    @staticmethod
    async def insert_user(**data) -> Users:
        logger.info("creating user in db")
        session = get_session()
        
        user = Users(
            username=data['username'],
            password=data['password'],
            email=data['email'],
            is_superuser=data['is_superuser']
        )
        session.add(user)
        return user

    @staticmethod
    async def get_user_by_username(username: str) -> Users | None:
        logger.info("selecting user by username")
        session = get_session()

        statement = select(Users).where(Users.username == username)
        return session.execute(statement).scalar_one_or_none()

    @staticmethod
    async def get_user_by_id(user_id: int) -> Users | None:
        logger.info("selecting user by id")
        session = get_session()

        statement = select(Users).where(Users.id == user_id)
        return session.execute(statement).scalar_one_or_none()

    @staticmethod
    async def is_superuser(user_id: int) -> bool:
        logger.info("select user is super user")
        session = get_session()

        sql = """
        SELECT is_superuser FROM users WHERE id = :user_id
        """

        result = session.execute(text(sql), {'user_id': user_id}).scalar_one_or_none()
        return bool(result)

    @staticmethod
    async def list_permission_codenames_by_user_id(user_id: int) -> set[str]:
        logger.info("list permissions by user")
        session = get_session()

        sql = """
        SELECT DISTINCT p.codename
        FROM user_roles ur
        JOIN role_permissions rp ON rp.fk_role = ur.fk_role
        JOIN permissions p ON p.id = rp.fk_permission
        WHERE ur.fk_user = :user_id
        """

        return {row[0] for row in session.execute(text(sql), {'user_id': user_id})}

    @staticmethod
    async def user_has_permission_by_codename(user_id: int, codename: str) -> bool:
        logger.info("select user by permission codename")
        session = get_session()

        sql = """
        SELECT 1 
        FROM user_roles ur
        JOIN role_permissions rp ON rp.fk_role = ur.fk_role
        JOIN permissions p ON p.id = rp.fk_permission
        WHERE p.codename = :codename
            AND r.fk_user = :user_id
        """

        result = session.execute(text(sql), {'codename': codename, 'user_id': user_id}).scalar_one_or_none()
        return bool(result)

