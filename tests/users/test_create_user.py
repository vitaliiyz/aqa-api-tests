import pytest

from src.aqa_api.test_data import REQUIRED_USER_FIELDS
from src.aqa_api.users_api import create_user, delete_user, get_users


def test_create_user_success(user_data):
    """Verify that creating a user returns 201 Created, contains expected fields, and appears in the user list."""
    created_user_data = None

    try:
        rs = create_user(user_data)
        assert (
            rs.status_code == 201
        ), f"The status code is not 201: {rs.status_code}\n{rs.text}"

        created_user_data = rs.json()

        for key, value in user_data.items():
            assert (
                created_user_data[key] == value
            ), f"The {key} is not equal to {created_user_data[key]}"

        get_users_rs = get_users()
        assert (
            get_users_rs.status_code == 200
        ), f"The status code is not 200: {get_users_rs.status_code}\n{get_users_rs.text}"

        get_users_rs_data = get_users_rs.json()
        assert (
            created_user_data in get_users_rs_data
        ), f"Expected user data:{created_user_data}. Actual user data: {get_users_rs_data}"

    finally:
        if created_user_data:
            delete_rs = delete_user(created_user_data["id"])
            assert (
                delete_rs.status_code == 204
            ), f"The status code is not 204: {delete_rs.status_code} – {delete_rs.text}"


@pytest.mark.parametrize("field", REQUIRED_USER_FIELDS)
def test_create_user_missing_required_field_returns_422(user_data, field):
    """Verify that creating a user with a blank required field returns 422 Unprocessable Entity."""
    user_data[field] = ""
    expected_rs = [
        {
            "field": field,
            "message": (
                "can't be blank, can be male of female"
                if field == "gender"
                else "can't be blank"
            ),
        }
    ]

    rs = create_user(user_data)
    assert (
        rs.status_code == 422
    ), f"The status code is not 422: {rs.status_code} – {rs.text}"
    assert rs.json() == expected_rs, f"{rs.json()} is not equal to expected"
