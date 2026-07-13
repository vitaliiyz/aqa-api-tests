import requests
from src.aqa_api.config import BASE_URL, ACCESS_TOKEN

default_headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

NEW_USER_DATA = {
    "name": "Vitality",
    "status": "active"
}


def test_get_users(users_rs):
    names = [user["name"] for user in users_rs]
    assert len(names) == 10, f"Expected len of users is 10, but actual {len(names)}"


def test_create_user(user_data):
    rs = requests.post(f"{BASE_URL}/users", json=user_data, headers=default_headers)
    assert rs.status_code == 201, f"The status code is not 201: {rs.status_code} – {rs.text}"
    user_data["id"] = rs.json()["id"]


def test_get_user(user_data):
    rs = requests.get(f"{BASE_URL}/users/{user_data['id']}", headers=default_headers)
    assert user_data == rs.json(), "User data is not found"


def test_update_user(user_data):
    rs = requests.put(f"{BASE_URL}/users/{user_data['id']}", json=NEW_USER_DATA, headers=default_headers)
    assert rs.status_code == 200, f"The status code is not 200: {rs.status_code}"

    for key, value in NEW_USER_DATA.items():
        if key in user_data:
            user_data[key] = value

    print(user_data)
    print(rs.json())
    assert user_data == rs.json(), "User data is not updated"


def test_delete_user(user_data):
    rs = requests.delete(f"{BASE_URL}/users/{user_data['id']}", headers=default_headers)
    assert rs.status_code == 204, f"The status code is not 201: {rs.status_code} – {rs.text}"
