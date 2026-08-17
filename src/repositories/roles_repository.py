from sqlalchemy import text
from models.roles import Roles

from utils.contextvars import get_session

class RoleRepository:

    @staticmethod
    async def list_roles() -> list[Roles]:
        session = get_session()

        sql = """
        SELECT id, codename FROM roles
        """

        return session.execute(text(sql)).all()

    @staticmethod
    async def get_role_by_id(id: int) -> Roles | None:
        session = get_session()

        sql = """
        SELECT id, codename, description FROM roles WHERE id = :id
        """

        response = session.execute(text(sql), {'id': id}).one_or_none()

        if not response:
            return None

        return Roles(
            id=response[0],
            codename=response[1],
            description=response[2]
        )

    @staticmethod
    async def insert_role(**data) -> Roles:
        session = get_session()

        role = Roles(
            codename=data['codename'],
            description=data['description']
        )

        session.add(role)
        return role