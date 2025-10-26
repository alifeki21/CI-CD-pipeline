import pytest
from app.app import app

def test_home_status_code():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
