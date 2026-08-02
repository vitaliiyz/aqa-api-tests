import requests
from src.aqa_api.config import ACCESS_TOKEN, BASE_URL


def send_request(
    request_method: str,
    endpoint: str,
    headers: dict | None = None,
    request_body: dict | None = None,
    params: dict | None = None,
) -> requests.Response:
    """
    Sends an HTTP request to the specified endpoint with optional body, params, and headers.
    If custom headers are not provided (None), default headers with Bearer token are used.
    """
    # If headers are not explicitly provided (None), fallback to default authorized headers
    if headers is None:
        request_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {ACCESS_TOKEN}",
        }
    else:
        # Use provided custom headers as-is (e.g. {} for unauthorized requests or invalid tokens)
        request_headers = headers

    return requests.request(
        method=request_method,
        url=f"{BASE_URL}{endpoint}",
        headers=request_headers,
        json=request_body,
        params=params,
    )