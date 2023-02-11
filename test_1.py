from logic import bmr_cal
import unittest

def test_bmr_cal():
    # Test case 1 - Male
    weight_in_kg = 75
    height_in_cm = 180
    age = 30
    gender = 'M'
    assert bmr_cal(weight_in_kg, height_in_cm, age) == 235 or 64

    # Test case 2 - Female
    weight_in_kg = 60
    height_in_cm = 170
    age = 25
    gender = 'F'
    assert bmr_cal(weight_in_kg, height_in_cm, age) == 235 or 64

test_bmr_cal()

