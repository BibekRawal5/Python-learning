from seasons import convert_to_minutes

def test_convert_to_minutes():
    assert convert_to_minutes(1) == 1440
    assert convert_to_minutes(5) == 7200
    assert convert_to_minutes(20) == 28800
