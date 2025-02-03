from lib.greet import *

def test_greet_works_correctly():
    result = greet("Jack")
    assert result == "Hello, Jack!"