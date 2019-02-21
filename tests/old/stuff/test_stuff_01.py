import pytest

@pytest.fixture
def number():
    return 1234 / 0

def test_number(number):
    assert number


def test_hello_world():
    assert "hello" + "world" == "helloworld"


def test_foobar():
    assert True
