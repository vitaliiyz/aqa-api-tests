from src.aqa_api.users_api import (
    create_user,
    delete_user,
    get_user_by_id,
    get_users,
    update_user,
)


def test_create_user_without_token_returns_401(user_data):
    """POST /users without Authorization header should return 401 Unauthorized"""
    response = create_user(user_data, headers={})

    assert response.status_code == 401, (
        f"Expected status code 401 without token, got {response.status_code}.\n"
        f"Response text: {response.text}"
    )

    actual_json = response.json()
    assert (
        actual_json.get("message") == "Authentication failed"
    ), f"Expected 'Authentication failed' error message, got {actual_json}"


def test_create_user_with_invalid_token_returns_401(user_data):
    """POST /users with invalid token should return 401 Unauthorized"""
    invalid_headers = {"Authorization": "Bearer invalid_token_12345"}

    response = create_user(user_data, headers=invalid_headers)

    assert response.status_code == 401, (
        f"Expected status code 401 with invalid token, got {response.status_code}.\n"
        f"Response text: {response.text}"
    )


def test_delete_user_without_token_returns_404(created_user):
    """DELETE /users/{id} without token should return 404 Resource not found in GoRest"""
    response = delete_user(created_user["id"], headers={})

    assert response.status_code == 404, (
        f"Expected status code 404 when deleting without token, got {response.status_code}.\n"
        f"Response text: {response.text}"
    )

    actual_json = response.json()
    assert (
        actual_json.get("message") == "Resource not found"
    ), f"Expected 'Resource not found' error message, got {actual_json}"


def test_update_user_without_token_returns_404(created_user):
    """PUT /users/{id} without token should return 404 Resource not found in GoRest"""
    update_payload = {"name": "Unauthorized Update"}

    response = update_user(created_user["id"], update_payload, headers={})

    assert response.status_code == 404, (
        f"Expected status code 404 when updating without token, got {response.status_code}.\n"
        f"Response text: {response.text}"
    )

    actual_json = response.json()
    assert (
        actual_json.get("message") == "Resource not found"
    ), f"Expected 'Resource not found' error message, got {actual_json}"


def test_get_users_without_token_returns_200():
    """Public read access: GET /users is accessible without token (200 OK)"""
    response = get_users(headers={})

    assert response.status_code == 200, (
        f"Expected public GET /users to return 200 OK without token, got {response.status_code}.\n"
        f"Response text: {response.text}"
    )


def test_get_user_without_token_returns_404(created_user):
    """GET /users/{id} without token returns 404 in GoRest API for unauthenticated scoping"""
    response = get_user_by_id(created_user["id"], headers={})

    assert response.status_code == 404, (
        f"Expected GET /users/id without token to return 404, got {response.status_code}.\n"
        f"Response text: {response.text}"
    )

    actual_json = response.json()
    assert (
        actual_json.get("message") == "Resource not found"
    ), f"Expected 'Resource not found' error message, got {actual_json}"