def non_existent_user_test(func):
    """Used for non-existing user tests"""
    non_existent_id = 999999999
    expected_response = {"message": "Resource not found"}

    # Act
    response = func(non_existent_id)

    # Assert
    assert response.status_code == 404, (
        f"Expected status code 404 for non-existent user, got {response.status_code}.\nResponse: {response.text}"
    )
    assert response.json() == expected_response, (
        f"Expected response: {expected_response}, got {response.json()}"
    )
