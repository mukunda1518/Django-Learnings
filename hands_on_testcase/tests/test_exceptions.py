import pytest


def f():
    return 2 // 0


def test_exception():
    with pytest.raises(ZeroDivisionError) as m:
        f()
    assert True == m