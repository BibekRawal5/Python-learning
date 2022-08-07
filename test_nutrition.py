from nutrition import calorie

def test_calorie():
    assert calorie("Apple") == 130
    assert calorie("Avocado") == 50
    assert calorie("Sweet Cherries") == 100
    assert calorie("Watermelon") == 80
    assert calorie("Plums") == 70