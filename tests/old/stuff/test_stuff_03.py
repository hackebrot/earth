import pytest

def test_numbers():
    assert 1234 == 1234


@pytest.mark.skip(reason="Outdated Python syntax")
def test_hello_world():
    # TODO: Can we remove this test?
    # print "hello world"
    pass


def test_foobar():
    assert True
