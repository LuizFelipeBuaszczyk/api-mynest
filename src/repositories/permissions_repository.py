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

    @staticmethod
    async def get_permissions_by_ids(permission_ids: list[int]) -> set[int]:
        session = get_session()

        placeholders = ', '.join(f':permission_{i}' for i in range(len(permission_ids)))
        params = {
            f'permission_{i}': permission_id
            for i, permission_id in enumerate(permission_ids)
        }

        sql = f"""
        SELECT id FROM permissions WHERE id IN ({placeholders})
        """

        return {row[0] for row in session.execute(text(sql), params)}


