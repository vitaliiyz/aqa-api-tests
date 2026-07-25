import random

from src.aqa_api.users_api import delete_user, get_user_by_id


def test_get_user_success(created_user):
    # Act
    response = get_user_by_id(created_user["id"])

    # Assert Status Code
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}.\nResponse: {response.text}"
    )

    actual_user = response.json()

    # Assert Payload Fields / Full Equality
    assert actual_user["id"] == created_user["id"], (
        f"Expected ID: {created_user['id']}, actual: {actual_user['id']}"
    )
    assert actual_user["name"] == created_user["name"], (
        f"Expected name: '{created_user['name']}', actual: '{actual_user['name']}'"
    )
    assert actual_user["email"] == created_user["email"], (
        f"Expected email: '{created_user['email']}', actual: '{actual_user['email']}'"
    )
    assert actual_user == created_user, (
        f"Expected user data: {created_user}. Actual user data: {actual_user}"
    )


def test_get_nonexistent_user_returns_404(created_user):
    user_id = created_user["id"]

    delete_rs = delete_user(user_id)
    assert delete_rs.status_code == 204, (
        f"The status code is not 204: {delete_rs.status_code}\n{delete_rs.text}"
    )

    expected_rs = {"message": "Resource not found"}

    response = get_user_by_id(user_id)
    assert response.status_code == 404, (
        f"Expected status code 404 for non-existent user, got {response.status_code}.\nResponse: {response.text}"
    )
    assert response.json() == expected_rs, (
        f"Actual response is not equal to expected: {response.json()}"
    )