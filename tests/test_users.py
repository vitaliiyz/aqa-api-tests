import requests
from src.aqa_api.config import BASE_URL, ACCESS_TOKEN


def test_get_users(users_rs):
    names = [user["name"] for user in users_rs]

    assert len(names) == 10

    user_2 = users_rs[1]

    assert user_2["name"] == "Aalok Shah"
    assert user_2["status"] == "active"
