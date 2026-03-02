import pytest
from flask.testing import FlaskClient
from ml_app import app

@pytest.fixture
def client() -> FlaskClient:
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client: FlaskClient):
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'OK'

def test_metrics(client: FlaskClient):
    response = client.get('/metrics')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'nist_checks' in json_data
