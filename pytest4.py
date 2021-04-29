import pytest

testdata = [('1', '2', 3), ('2','3',5), ('8', '-6', 2)]

@pytest.mark.parametrize("a,b,expected", testdata)
def test_sum_string_numbers(a, b, expected):
    assert int(a) + int(b) == expected