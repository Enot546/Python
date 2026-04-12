import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_text, input_symbol, expected_output", [
    ("Крюк", "К", "рюк"),
    ("Крюк", "к", "Крю"),
    ("1234", "2", "134"),
    ("1234", "23", "14"),
    ("H2O", "2", "HO"),
    ]
)
def test_delete_symbol_positive(input_text, input_symbol, expected_output):
    assert string_utils.delete_symbol
    (input_text, input_symbol) == expected_output


@pytest.mark.negative
@pytest.mark.parametrize("input_text, input_symbol, expected_output", [
    ("Текст", "А", "Текст"),
    ("1234", "56", "1234"),
    ("1234", "5", "1234"),
    (" ", "", " "),
    ("  ", " ", " "),
    ("Текст", "k", "Текст"),
    ("Key", "К", "Key"),
])
def test_delete_symbol_negative(input_text, input_symbol, expected_output):
    assert string_utils.delete_symbol
    (input_text, input_symbol) == expected_output


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    (" два слова", "два слова"),
    ("слова   ", "слова   "),
    (" 1234", "1234"),
    ("12 34", "12 34"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" _ _ _", "_ _ _"),
    (" ", ""),
    ("", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_text, input_symbol, expected", [
    ("SkyPro", "S", "True"),
    ("SkyPro", "H", "False"),
    ("1234", "2", "True"),
    ("1234", "5", "False"),
    ("Крюк", "к", "True"),
    ("Крюк", "К", "True"),
])
def test_contains_positive(input_text, input_symbol, expected):
    assert string_utils.contains
    (input_text, input_symbol, expected) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_text, input_symbol, expected", [
    ("Крюк", "k", "False"),
    ("Крюк", "K", "False"),
    ("1234", "З", "False"),
])
def test_contains_negative(input_text, input_symbol, expected):
    assert string_utils.contains
    (input_text, input_symbol, expected) == expected
