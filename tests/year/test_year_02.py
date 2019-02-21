from earth import Months


def test_hello_world():
    assert "hello" + "world" == "helloworld"


def test_jan():
    assert Months.JAN.value == "January"


def test_oct():
    assert Months.OCT.value == "October"


def test_foobar():
    assert True
