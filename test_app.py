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
    response = client.post('/users', data=json.dumps(user_data), content_type='application/json')
    assert response.status_code ==  201
    data = json.loads(response.data)
    assert 'id' in data
    assert len(users) ==  1

def test_update_user(client):
    user_data = {
        'firstName': 'Jane',
        'lastName': 'Doe',
        'birthYear':  1995,
        'group': 'premium'
    }
    response = client.post('/users', data=json.dumps(user_data), content_type='application/json')
    assert response.status_code ==  201
    data = json.loads(response.data)
    assert 'id' in data
    user_id = data['id']

    updated_data = {
        'firstName': 'Updated',
        'lastName': 'User',
        'birthYear':  1996,
        'group': 'admin'
    }
    response = client.patch(f'/users/{user_id}', data=json.dumps(updated_data), content_type='application/json')
    assert response.status_code ==  204
    assert users[user_id]['firstName'] == 'Updated'
    assert users[user_id]['lastName'] == 'User'
    assert users[user_id]['birthYear'] ==  1996
    assert users[user_id]['group'] == 'admin'
    
def test_delete_user(client):
    user_data = {
        'firstName': 'Delete',
        'lastName': 'Me',
        'birthYear':  2000,
        'group': 'user'
    } 
    response = client.post('/users', data=json.dumps(user_data), content_type='application/json')
    assert response.status_code ==  201
    data = json.loads(response.data)
    assert 'id' in data
    user_id = data['id']
    
    response = client.delete(f'/users/{user_id}')
    assert response.status_code ==  204
    assert user_id not in users
