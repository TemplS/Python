from os import remove
from string import whitespace

import pytest
from string_utils import StringUtils


util = StringUtils()


@pytest.mark.parametrize("input_text, result", [
    ("skypro", "Skypro"),
    ("python", "Python")
])
def test_capitalize_positive(input_text, result):
    assert util.capitalize(input_text) == result


@pytest.mark.parametrize("input_text, result", [
    ("789sky", "789sky"),
    (" ", " ")
])
def test_capitalize_negative(input_text, result):
    assert util.capitalize(input_text) == result


@pytest.mark.parametrize("input_text, result", [
    ("   skypro", "skypro"),
        (" fort", "fort")
])
def test_trim(input_text, result):
    assert util.trim(input_text) == result


@pytest.mark.parametrize("word, symbol", [
    ("SkyPro", "P"),
    ("SkyPro", "r")
])
def test_contains_positive(word, symbol):
    assert util.contains(word, symbol)


@pytest.mark.parametrize("word, symbol", [
    ("SkyPro", "z"),
    ("SkyPro", "a")
])
@pytest.mark.xfail
def test_contains_negative(word, symbol):
    assert util.contains(word, symbol)
