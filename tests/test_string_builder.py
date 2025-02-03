from lib.string_builder import StringBuilder

def test_StringBuilder_initial_string():
    string_builder = StringBuilder()
    assert string_builder.str == ""

def test_StringBuilder_add_string():
    string_builder = StringBuilder()
    string_builder.add("test string")
    assert string_builder.str == "test string"

def test_StringBuilder_size():
    string_builder = StringBuilder()
    string_builder.add("test string")
    assert string_builder.size() == 11

def test_StringBuilder_output():
    string_builder = StringBuilder()
    string_builder.add("test string")
    assert string_builder.output() == "test string"
