def test_main_status(flask_client):
    resp = flask_client.get('/')
    assert 200 == resp.status_code
