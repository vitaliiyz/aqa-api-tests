import pytest

from src.aqa_api.test_data import REQUIRED_USER_FIELDS
from src.aqa_api.users_api import create_user, delete_user


def test_create_user_success(user_data):
    """Verify that creating a user returns 201 and returned fields match request data."""
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

    finally:
        if created_user_data:
            delete_rs = delete_user(created_user_data["id"])
            assert (
                delete_rs.status_code == 204
            ), f"The status code is not 204: {delete_rs.status_code} – {delete_rs.text}"


@pytest.mark.parametrize("field", REQUIRED_USER_FIELDS)
def test_create_user_blank_required_field_returns_422(user_data, field):
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


@pytest.mark.parametrize("field", REQUIRED_USER_FIELDS)
def test_create_user_missing_required_field_returns_422(user_data, field):
    """Verify that creating a user with a missing required field returns 422 Unprocessable Entity."""
    del user_data[field]
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


def test_create_user_email_already_exists_returns_422(created_user):
    """Verify that creating a user with an existing email returns 422 Unprocessable Entity."""

    new_user_data = {
        "name": "New User",
        "email": created_user["email"],
        "gender": "female",
        "status": "active",
    }

    expected_rs = [{"field": "email", "message": "has already been taken"}]

    rs = create_user(new_user_data)

    assert (
        rs.status_code == 422
    ), f"The status code is not 422: {rs.status_code} – {rs.text}"
    assert rs.json() == expected_rs, f"{rs.json()} is not equal to expected"
