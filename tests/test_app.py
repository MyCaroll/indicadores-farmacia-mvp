import pytest
from app import app

def test_home_status_code():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_home_content():
    client = app.test_client()
    response = client.get('/')
    assert b"MVP Farmacia Clinica" in response.data
