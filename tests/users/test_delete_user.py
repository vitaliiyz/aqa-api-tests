from src.aqa_api.test_data import NON_EXISTING_USER_ID
from src.aqa_api.users_api import delete_user, get_user_by_id, get_users
from tests.users.user_test_helpers import non_existent_user_test


def test_delete_user_success(created_user):
    """
    Verify that deleting an existing user returns a 204 status code and that the deleted user no longer appears in the GET users response.
    """
    user_id = created_user['id']

    delete_rs = delete_user(user_id)
    assert delete_rs.status_code == 204, f"The status code is not 204: {delete_rs.status_code}\n{delete_rs.text}"

    user_rs = get_user_by_id(user_id)
    assert user_rs.status_code == 404, f"The status code is not 404: {user_rs.status_code}\n{user_rs.text}"

    users_rs = get_users()
    assert users_rs.status_code == 200, f"The status code is not 404: {users_rs.status_code}\n{users_rs.text}"
    assert created_user not in users_rs.json(), f"User has not been removed: {users_rs.text}"


def test_delete_nonexistent_user_returns_404():
    """Verify that deleting a non-existent user ID returns a 404 status
    independently without mutating or deleting shared test resources.
    """
    non_existent_user_test(get_user_by_id, NON_EXISTING_USER_ID)
