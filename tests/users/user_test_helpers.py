def non_existent_user_test(
    send_func,
    user_id,
    request_data: dict | None = None,
):
    """Used for non-existing user tests"""
    expected_response = {"message": "Resource not found"}

    # Act
    if request_data is None:
        response = send_func(user_id)
    else:
        response = send_func(user_id, request_data)

    # Assert
    assert (
        response.status_code == 404
    ), f"Expected status code 404 for non-existent user, got {response.status_code}.\nResponse: {response.text}"
    assert (
        response.json() == expected_response
    ), f"Expected response: {expected_response}, got {response.json()}"
