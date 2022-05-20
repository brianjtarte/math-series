import pytest

from math_series.series import fibonacci, lucas, sum_series


def test_number_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_number_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_number_fifteen():
    actual = fibonacci(15)
    expected = 610
    assert actual == expected


# Lucas tests

def test_number_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_number_lucas_negative():
    actual = lucas(-1)
    expected = "ERROR!"
    assert actual == expected


def test_number_lucas_twentyfive():
    actual = lucas(25)
    expected = 167761
    assert actual == expected


def test_sum_series_a():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_b():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_sum_series_fib():
    actual = sum_series(8,0,1)
    expected = 21
    assert actual == expected

def test_sum_series_luc():
    actual = sum_series(8,2,1)
    expected = 47
    assert actual == expected
