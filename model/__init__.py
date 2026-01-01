import os
from dotenv import load_dotenv 
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

load_dotenv()

def _get_url_db() -> str:
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT')
    database = os.getenv('POSTGRES_DB')

    return f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(_get_url_db())

Base = declarative_base()
Session = sessionmaker(engine)