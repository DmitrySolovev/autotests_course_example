import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a,b,res', [
    pytest.param(10, 5, 2, marks=pytest.mark.smoke),
    pytest.param(6, 2, 3, marks=pytest.mark.skip('bad')),
    (15, 5, 3)
    ])
def test_division_two_number(a, b, res):
    assert all_division(a, b) == res

