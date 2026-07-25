from src.aqa_api.users_api import get_user_by_id


def test_get_user_success(created_user):
    """Verify that an existing user can be successfully retrieved by ID
    and all fields match the full user schema contract.
    """
    # Act
    response = get_user_by_id(created_user["id"])

    # Assert Status Code
    assert response.status_code == 200, (
        f"Expected status code 200, got {response.status_code}.\nResponse: {response.text}"
    )

    # Assert Full Schema/Payload Equality (covers id, name, email, gender, status)
    assert response.json() == created_user, (
        f"Expected user data: {created_user}. Actual user data: {response.json()}"
    )


def test_get_nonexistent_user_returns_404():
    """Verify that requesting a non-existent user ID returns a 404 status
    independently without mutating or deleting shared test resources.
    """
    non_existent_id = 999999999
    expected_response = {"message": "Resource not found"}

    # Act
    response = get_user_by_id(non_existent_id)

    # Assert
    assert response.status_code == 404, (
        f"Expected status code 404 for non-existent user, got {response.status_code}.\nResponse: {response.text}"
    )
    assert response.json() == expected_response, (
        f"Expected response: {expected_response}, got {response.json()}"
    )