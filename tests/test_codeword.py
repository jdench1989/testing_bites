from lib.check_codeword import *

def test_check_codeword_if_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_nearly_correct():
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_check_codeword_incorrect():
    result = check_codeword("spoon")
    assert result == "WRONG!"