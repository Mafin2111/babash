import pytest
from calculator.core import add, subtract, multiply, divide
def test_add():
    assert add(2, 3) == 5
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
