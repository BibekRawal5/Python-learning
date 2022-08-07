from camel import convert

def test_convert():
    assert convert("firstName") == "first_name"
    assert convert("lastName") == "last_name"
    assert convert("howAreYou") == "how_are_you"

