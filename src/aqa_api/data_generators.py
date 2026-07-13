from uuid import uuid4


def generate_email():
    return f"test_user_{uuid4().hex[:10]}@example.com"
