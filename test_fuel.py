from fuel import indicator

def test_indicator():
    assert indicator("2/3") == 67
    assert indicator("1/80") == "E"
    assert indicator("3/2") == "F"
    assert indicator("1/2") == 50