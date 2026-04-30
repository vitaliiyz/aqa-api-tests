import requests


def test_1():
    r = requests.get('https://gorest.co.in/public/v2/users')
    assert r.status_code == 200
    assert r.text == ''