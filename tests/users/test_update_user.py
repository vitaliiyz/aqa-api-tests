from src.aqa_api.data_generators import generate_email

from src.aqa_api.users_api import get_user_by_id, update_user


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
