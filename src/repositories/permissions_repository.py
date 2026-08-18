from sqlalchemy import text
from models.permissions import Permissions

from utils.contextvars import get_session

class PermissionRepository:

    @staticmethod
    async def list_permissions() -> list[Permissions]:
        session = get_session()

        sql = """
        SELECT id, codename, description FROM permissions
        """

        return session.execute(text(sql)).all()
