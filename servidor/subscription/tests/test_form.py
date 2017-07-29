def test_show_form(flask_client):
    resp = flask_client.get('/inscricao')
    assert 200 == resp.status_code
