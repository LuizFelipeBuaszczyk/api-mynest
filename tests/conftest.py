import os
import pytest
os.environ['ENVIRONMENT'] = 'TEST'

from dotenv import load_dotenv
load_dotenv()

from fastapi.testclient import TestClient
from infra.database import Base, engine

@pytest.fixture
def client():
    from main import app
    with TestClient(app) as c:
        yield c

@pytest.fixture(autouse=True)
def setup_and_teardown_db():

    Base.metadata.create_all(bind=engine)

    yield   # Test runs here
    
    engine.dispose()


