from src.aqa_api.config import BASE_URL, ACCESS_TOKEN

import requests


def send_request(request_method: str, endpoint: str, headers: dict | None = None,
                 request_body: dict | None = None, params: dict | None = None) -> requests.Response:
    default_headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    if headers is not None:
        default_headers.update(headers)

    return requests.request(
        method=request_method,
        url=f"{BASE_URL}{endpoint}",
        headers=default_headers,
        json=request_body,
        params=params
    )