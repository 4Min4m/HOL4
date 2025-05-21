import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app.app import app
from app.database import init_db, add_name, get_names

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        init_db()  # ایجاد دیتابیس جدید برای هر تست
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Enter Your Name" in response.data

def test_name_submission(client):
    # تست ارسال نام و نمایش آن
    response = client.post('/', data={'name': 'Ali'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Ali" in response.data