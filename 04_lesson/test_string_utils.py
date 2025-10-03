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
# def test_contains_negative(word, symbol):              У меня получилось 2 варианта решения, т.к. здесь выдает ошибку
#     with pytest.raises(AssertionError):                какой из них более корректный - сказать что ошибка должна быть
#         assert util.contains(word, symbol)             или поставить маркер ошибки?
@pytest.mark.xfail
def test_contains_negative(word, symbol):
    assert util.contains(word, symbol)


@pytest.mark.parametrize("word, letter", [
    ("SkyPro", "S"),
    ("SkyPro", "y"),
    ("Train", "n")
])
def test_delete_symbol_positive(word, letter):
    assert util.delete_symbol(word, letter)


@pytest.mark.parametrize("word, letter", [
    ("Socks", "u"),
    ("Moscow", "a"),
    ("Cow", "n")
])
def test_delete_symbol_negative(word, letter):
    assert util.delete_symbol(word, letter)
