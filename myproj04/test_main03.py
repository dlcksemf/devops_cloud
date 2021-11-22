import pytest
from main03 import get_word_count, get_ch_count_except_space, get_rounded_number


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("우리는 파이썬을 즐겨요", 3),
        ("Python Family", 2),
    ],
)
def test_get_word_count(sentence, expected):
    assert get_word_count(sentence) == expected


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("우리는 파이썬을 즐겨요", 10),
        ("Python Family", 12),
    ],
)
def test_get_ch_count_except_count(sentence, expected):
    assert get_ch_count_except_space(sentence) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (123456, 123000),
        (1234, 1000),
    ],
)
def test_get_rounded_number(number, expected):
    assert get_rounded_number(number) == expected
