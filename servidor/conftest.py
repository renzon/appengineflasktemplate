import pytest

from core.main import app


@pytest.fixture
def flask_client():
    return app.test_client()
