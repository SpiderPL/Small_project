import pytest

@pytest.fixture
def users():
    return [
        {"user": "user1", "age": 45},
        {"user": "user2", "age": 19}
    ]

def test_users_have_above_18_years(users):
    assert all([user['age']>=18 for user in users])