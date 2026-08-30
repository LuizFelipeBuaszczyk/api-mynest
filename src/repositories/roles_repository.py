from utils.logger import get_logger

from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from models.roles import Roles

from utils.contextvars import get_session
from exceptions.roles_exception import RolePermissionAlreadyExistsException

logger = get_logger(__name__)

class RoleRepository:

    @staticmethod
    async def list_roles() -> list[Roles]:
        logger.info("selecting roles")
        session = get_session()

        sql = """
        SELECT id, codename FROM roles
        """

        return session.execute(text(sql)).all()

    @staticmethod
    async def get_role_by_id(id: int) -> Roles | None:
        logger.info("selecting role by id")
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
        logger.info("creating roles in db")
        session = get_session()

        role = Roles(
            codename=data['codename'],
            description=data['description']
        )

        session.add(role)
        return role

    @staticmethod
    async def find_association_permissions(role_id: int, permission_ids: list[int]) -> set[int]:
        session = get_session()

        if not permission_ids:
            return set()

        placeholders = ', '.join(f':permission_{i}' for i in range(len(permission_ids)))
        params = {
            f'permission_{i}': permission_id
            for i, permission_id in enumerate(permission_ids)
        }
        params['role_id'] = role_id

        sql = f"""
        SELECT fk_permission FROM role_permissions
        WHERE fk_role = :role_id AND fk_permission IN ({placeholders})
        """

        return {row[0] for row in session.execute(text(sql), params)}

    @staticmethod
    async def list_permissions_by_role_id(role_id: int) -> list[int]:
        logger.info("selecting permissions by role")
        session = get_session()

        sql = """
        SELECT fk_permission FROM role_permissions WHERE fk_role = :role_id
        """

        return [row[0] for row in session.execute(text(sql), {'role_id': role_id})]

    @staticmethod
    async def insert_role_permissions(role_id: int, permission_ids: list[int]) -> None:
        logger.info("creating role_permission association")
        session = get_session()

        if not permission_ids:
            return

        placeholders = ', '.join(f'(:role_id, :permission_{i})' for i in range(len(permission_ids)))
        params = {
            f'permission_{i}': permission_id
            for i, permission_id in enumerate(permission_ids)
        }
        params['role_id'] = role_id

        sql = f"""
        INSERT INTO role_permissions (fk_role, fk_permission) VALUES {placeholders}
        """

        try:
            session.execute(text(sql), params)
        except IntegrityError:
            raise RolePermissionAlreadyExistsException()
