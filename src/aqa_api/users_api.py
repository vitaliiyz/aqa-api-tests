from src.aqa_api.api_client import send_request


def get_users(headers: dict = None):
    return send_request("get", "/users", headers=headers)


def get_user_by_id(user_id: int, headers: dict = None):
    return send_request("get", f"/users/{user_id}", headers=headers)


def create_user(user_data: dict, headers: dict = None):
    return send_request("post", "/users", request_body=user_data, headers=headers)


def delete_user(user_id: int, headers: dict = None):
    return send_request("delete", f"/users/{user_id}", headers=headers)


def update_user(user_id: int, update_data: dict, headers: dict = None):
    return send_request("put", f"/users/{user_id}", request_body=update_data, headers=headers)