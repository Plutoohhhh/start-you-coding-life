import pytest
import requests
from api_clients.CRUD_api_client import CURDApiClient

def test_posts():
    client = CURDApiClient()
    response = client.get_posts()

    assert response.status_code == 200,f"预期状态码为200，实际为{response.status_code}"
    date = response.json()
    assert len(date) == 100