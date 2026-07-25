import pytest

from src.aqa_api.data_generators import generate_email
from src.aqa_api.test_data import BASE_USER_DATA
from src.aqa_api.users_api import get_users, create_user, delete_user


@pytest.fixture(scope="function")
def user_data():
    data = BASE_USER_DATA.copy()
    data["email"] = generate_email()
    return data


@pytest.fixture
def users_rs():
    rs = get_users()
    assert rs.status_code == 200, f"The status code is not 200: {users_rs.status_code}\n{users_rs.text}"

    return rs.json()


@pytest.fixture
def created_user(user_data):
    rs = create_user(user_data)
    assert rs.status_code == 201

    created_data = rs.json()
    print("\nUser is created")

    yield created_data

    delete_rs = delete_user(created_data['id'])

    assert delete_rs.status_code in (204,
                                     404), f"The status code is not 204 or 404: {delete_rs.status_code}\n{delete_rs.text}"

    print("\nUser is removed")
