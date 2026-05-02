import requests
import pytest

from src.aqa_api.config import BASE_URL, ACCESS_TOKEN


def send_request(request_method: str, endpoint: str, headers: dict | None = None):
    default_headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    if headers is not None:
        default_headers.update(headers)

    return requests.request(method=request_method, url=f"{BASE_URL}{endpoint}", headers=default_headers)


@pytest.fixture
def users_rs():
    rs = send_request("get", "/users")
    assert rs.status_code == 200

    return rs.json()