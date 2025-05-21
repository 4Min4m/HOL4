import pytest
from app.app import app
from app.database import init_db, add_name

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        init_db()
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Enter Your Name" in response.data

def test_name_submission(client):
    response = client.post('/', data={'name': 'Ali'})
    assert response.status_code == 200
    assert b"Ali" in response.data