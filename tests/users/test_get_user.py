from src.aqa_api.users_api import get_user_by_id


def test_get_user(created_user):
    get_user_by_id_rs = get_user_by_id(created_user['id'])

    assert get_user_by_id_rs.status_code == 200, f"The status code is not 200: {get_user_by_id_rs.status_code}\n{get_user_by_id_rs.text}"
    assert get_user_by_id_rs.json() == created_user, f"Expected user data:{created_user}. Actual user data: {get_user_by_id_rs.json()}"
