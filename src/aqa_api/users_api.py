from src.aqa_api.api_client import send_request


def get_users():
    return send_request("get", "/users")


def get_user_by_id(user_id: int):
    return send_request("get", f"/users/{user_id}")


def create_user(user_data: dict):
    return send_request("post", "/users", request_body=user_data)


def delete_user(user_id: int):
    return send_request("delete", f"/users/{user_id}")


def update_user(user_id: int, update_data: dict):
    return send_request("put", f"/users/{user_id}", request_body=update_data)
