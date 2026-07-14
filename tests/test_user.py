from src.aqa_api.data_generators import generate_email

from src.aqa_api.users_api import get_users, create_user, get_user_by_id, delete_user, update_user


def test_create_user(user_data):
    created_user_data = None

    try:
        rs = create_user(user_data)
        assert rs.status_code == 201, f"The status code is not 201: {rs.status_code}\n{rs.text}"

        created_user_data = rs.json()

        for key, value in user_data.items():
            assert created_user_data[key] == value, f"The {key} is not equal to {created_user_data[key]}"

        get_users_rs = get_users()
        assert get_users_rs.status_code == 200, f"The status code is not 200: {get_users_rs.status_code}\n{get_users_rs.text}"
        get_users_rs_data = get_users_rs.json()
        assert created_user_data in get_users_rs_data, f"Expected user data:{created_user_data}. Actual user data: {get_users_rs_data}"

    finally:
        if created_user_data:
            delete_rs = delete_user(created_user_data['id'])
            assert delete_rs.status_code == 204, f"The status code is not 201: {delete_rs.status_code} – {delete_rs.text}"


def test_get_user(created_user):
    get_user_by_id_rs = get_user_by_id(created_user['id'])

    assert get_user_by_id_rs.status_code == 200, f"The status code is not 200: {get_user_by_id_rs.status_code}\n{get_user_by_id_rs.text}"
    assert get_user_by_id_rs.json() == created_user, f"Expected user data:{created_user}. Actual user data: {get_user_by_id_rs.json()}"


def test_update_user(created_user):
    email = generate_email()

    update_data = created_user.copy()
    update_data.update({
        "name": "New Name",
        "gender": "female",
        "email": email,
        "status": "active"
    })

    update_rs = update_user(created_user['id'], update_data)
    assert update_rs.status_code == 200, f"The status code is not 200: {update_rs.status_code}\n{update_rs.text}"
    update_rs_data = update_rs.json()
    assert update_rs_data == update_data, f"User data in Update response: {update_rs_data} is not equal to expected:\n{update_data}"

    get_user_by_id_rs = get_user_by_id(created_user['id'])
    assert get_user_by_id_rs.status_code == 200, f"The status code is not 200: {get_user_by_id_rs.status_code}"
    get_user_by_id_rs_data = get_user_by_id_rs.json()
    assert get_user_by_id_rs_data == update_data, f"User data in Get User By Id response: {get_user_by_id_rs_data} is not equal to expected:\n{update_data}"
