from math_series import __version__
from math_series.series import *

def test_version():
    assert __version__ == '0.1.0'

def test_one():
    expected=89
    actual=fibonacci(11)
    assert actual == expected

def test_two():
    expected=123
    actual=lucas(10)
    assert actual == expected

def test_three():
    expected=0
    actual=fibonacci(0)
    assert actual == expected


def test_four():
    expected=2
    actual=lucas(0)
    assert actual == expected

def test_five():
    expected=1
    actual=lucas(1)
    assert actual == expected
def test_six():
    expected=34
    actual=sum_series(9)
    assert actual == expected

def test_seven():
    expected=126
    actual=sum_series(10,4,6)
    assert actual == expected


