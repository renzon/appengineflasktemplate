import pytest


@pytest.fixture
def home_resp(flask_client):
    resp = flask_client.get('/')
    return resp


def test_main_status(home_resp):
    assert 302 == home_resp.status_code


def test_main_status(home_resp):
    path = '/'.join(home_resp.location.split('/')[-2:])
    assert 'static/home.html' == path
