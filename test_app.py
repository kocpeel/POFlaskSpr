import pytest
import json
from app import app, users


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_all_users(client):
    response = client.get('/users')
    assert response.status_code ==  200
    data = json.loads(response.data)
    assert isinstance(data['users'], dict)


def test_create_user(client):
    user_data = {
        'firstName': 'John',
        'lastName': 'Doe',
        'birthYear':  1990,
        'group': 'user'
    }
