import pytest
from subscription.handler import app


@pytest.fixture
def client():
    return app.test_client()


def test_show_form(client):
    resp = client.get('/inscricao')
    assert 200 == resp.status_code
