import pytest

from appengine_config import app



@pytest.fixture
def flask_client():
    return app.test_client()
