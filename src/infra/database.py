import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

TESTING = os.getenv('ENVIRONMENT', 'DEV').upper() == 'TEST'

def create_sqlite_engine():
    from models import Passwords, Permissions, Roles, UserRoles, Users, RolePermission

    SQLITE_DATABASE_URL = 'sqlite:///./test.db'
    return create_engine(SQLITE_DATABASE_URL, connect_args={"check_same_thread": False})


def create_postgresql_egine():
    
    POSTGRES_USER = os.getenv('POSTGRES_USER', None)
    if not POSTGRES_USER:
        raise Exception('POSTGRES_USER not defined')

    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', None)
    if not POSTGRES_PASSWORD:
        raise Exception('POSTGRES_PASSWORD NOT DEFINED')

    POSTGRES_HOST = os.getenv('POSTGRES_HOST', None)
    if not POSTGRES_HOST:
        raise Exception('POSTGRES_HOST NOT DEFINED')

    POSTGRES_PORT = os.getenv('POSTGRES_PORT', None)
    if not POSTGRES_PORT:
        raise Exception('POSTGRES_PORT NOT DEFINED')

    POSTGRES_DATABASE = os.getenv('POSTGRES_DB', None)
    if not POSTGRES_DATABASE:
        raise Exception('POSTGTRES_DB not defined')

    return create_engine(f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}")

def get_engine():
 return create_sqlite_engine() if TESTING else create_postgresql_egine()

engine = get_engine()
_session = sessionmaker(bind=get_engine(),)

def get_session():
    return _session
