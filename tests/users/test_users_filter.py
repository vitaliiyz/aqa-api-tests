"""
Tests for filtering users by status and name (GET /users)
"""

import pytest

from src.aqa_api.users_api import get_users


class TestUsersFiltering:
    """Testing user filtering parameters"""

    def test_filter_users_by_status(self):
        """Filter users by status (active / inactive)"""
        status_to_test = "active"
        response = get_users(params={"status": status_to_test})

        assert (
            response.status_code == 200
        ), f"The status code is not 200: {response.status_code}\n{response.text}"

        users = response.json()
        assert isinstance(users, list), "Response data should be a list"

        for user in users:
            assert (
                user.get("status") == status_to_test
            ), f"User {user['id']} has status '{user.get('status')}', expected '{status_to_test}'"

    def test_filter_users_by_name(self):
        """Filter users by name (partial match)"""
        all_users_response = get_users()
        assert all_users_response.status_code == 200
        all_users = all_users_response.json()

        if not all_users:
            pytest.skip("No users available in the system to test name filtering")

        target_name = all_users[0]["name"].split()[0]

        response = get_users(params={"name": target_name})
        assert (
            response.status_code == 200
        ), f"The status code is not 200: {response.status_code}\n{response.text}"

        filtered_users = response.json()
        assert isinstance(filtered_users, list)

        for user in filtered_users:
            assert (
                target_name.lower() in user.get("name", "").lower()
            ), f"User name '{user.get('name')}' does not contain expected substring '{target_name}'"
