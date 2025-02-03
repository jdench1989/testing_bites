from lib.report_length import *

def test_report_length_5_characters():
    result = report_length("there")
    assert result == "This string was 5 characters long"

def test_report_length_mulitple_words():
    result = report_length("Several words in a string")
    assert result == "This string was 25 characters long"

def test_report_length_empty_string():
    result = report_length("")
    assert result == "This string was 0 characters long"