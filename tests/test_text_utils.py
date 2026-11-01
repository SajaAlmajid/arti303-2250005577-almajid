import pytest
from src.text_utils import clean_text, count_words


def test_clean_text():
    text = "  Hello, World!  "
    expected = "hello, world!"
    assert clean_text(text) == expected


def test_count_words():
    text = "hello world foo bar"
    assert count_words(text) == 4