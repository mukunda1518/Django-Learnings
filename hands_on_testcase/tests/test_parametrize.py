# https://docs.pytest.org/en/7.1.x/how-to/parametrize.html#parametrizemark
import pytest


@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


# For whole module/file or class we can use in below format
# pytestmark = pytest.mark.parametrize("n, expected", [(1, 2), (3, 4)])


@pytest.mark.parametrize("n, expected", [(1, 2), (3, 4)])
class TestClass:

    def test_sample_case(self, n, expected):
        assert n + 1 == expected

    def test_werid_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected
