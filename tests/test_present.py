import pytest
from lib.present import *

def test_Present_initial_construction():
    present = Present()
    assert present.contents == None

def test_Present_wrap_contents_not_already_set():
    present = Present()
    present.wrap("teddy bear")
    assert present.contents == "teddy bear"

def test_Present_wrap_contents_already_set():
    present = Present()
    present.wrap("teddy bear")
    with pytest.raises(Exception) as e:
        present.wrap("toy car")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_Present_unwrap_contents_not_set():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_Present_unwrap_contents_set():
    present = Present()
    present.wrap("teddy bear")
    result = present.unwrap()
    assert result == "teddy bear"
