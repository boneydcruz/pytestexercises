import pytest


def is_even(input):
    if input % 2 == 0:
        return True
    return False


@pytest.mark.parametrize("input,expected", [
    (2, True),
    (3, False),
    (11, False),
])
def test_is_even(input, expected):
    assert is_even(input) == expected
