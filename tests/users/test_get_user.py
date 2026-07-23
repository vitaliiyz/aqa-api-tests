from src.aqa_api.users_api import get_user_by_id


def test_get_user_success(created_user):
    # Act
    response = get_user_by_id(created_user["id"])

    # Assert Status Code
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}.\nResponse: {response.text}"
    )

    actual_user = response.json()

    # Assert Payload Fields
    assert actual_user["id"] == created_user["id"], (
        f"Expected ID: {created_user['id']}, actual: {actual_user['id']}"
    )
    assert actual_user["name"] == created_user["name"], (
        f"Expected name: '{created_user['name']}', actual: '{actual_user['name']}'"
    )
    assert actual_user["email"] == created_user["email"], (
        f"Expected email: '{created_user['email']}', actual: '{actual_user['email']}'"
    )


def test_get_nonexistent_user_returns_404():
    non_existent_id = 999999999

    response = get_user_by_id(non_existent_id)

    assert response.status_code == 404, (
        f"Expected status code 404 for non-existent user, got {response.status_code}.\nResponse: {response.text}"
    )