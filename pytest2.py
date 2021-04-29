import pytest

def div_two(x):
    return 2/x

def test_div_two():
    with pytest.raises(ZeroDivisionError):
        div_two(0)
