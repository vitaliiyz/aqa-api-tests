import random

from src.aqa_api.users_api import get_user_by_id, delete_user


def test_get_user(created_user):
    get_user_by_id_rs = get_user_by_id(created_user['id'])

    assert get_user_by_id_rs.status_code == 200, f"The status code is not 200: {get_user_by_id_rs.status_code}\n{get_user_by_id_rs.text}"
    assert get_user_by_id_rs.json() == created_user, f"Expected user data:{created_user}. Actual user data: {get_user_by_id_rs.json()}"


def test_get_nonexistent_user(created_user):
    user_id = created_user["id"]

    delete_rs = delete_user(user_id)
    assert delete_rs.status_code == 204, f"The status code is not 204: {delete_rs.status_code}\n{delete_rs.text}"

    expected_rs = {
        "message": "Resource not found"
    }

    get_user_by_id_rs = get_user_by_id(user_id)
    assert get_user_by_id_rs.status_code == 404, f"The status code is not 404: {get_user_by_id_rs.status_code}\n{get_user_by_id_rs.text}"
    assert get_user_by_id_rs.json() == expected_rs, f"Actual response is not equal to expected: {get_user_by_id_rs.json()}"
