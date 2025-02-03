import pytest
from lib.password_checker import *

def test_PasswordChecker_initial_construction():
    checker = PasswordChecker()
    assert isinstance(checker, object) == True

def test_PasswordChecker_length_greater_than_8():
    checker = PasswordChecker()
    result = checker.check("verylongpassword")
    assert result == True

def test_PasswordChecker_length_equals_8():
    checker = PasswordChecker()
    result = checker.check("12345678")
    assert result == True

def test_PasswordChecker_length_less_than_8():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check("1234")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ chaarcters."

def test_PasswordChecker_empty_string_input():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check("")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ chaarcters."