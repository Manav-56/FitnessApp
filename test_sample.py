from pywebio.input import input, FLOAT
from pywebio.output import put_text
from py_edamam import Edamam
import unittest
from unittest.mock import patch
from logic import bmr_cal,bmi_index,daily_calorie_needs,logic

def test_bmr_calculation():
    with patch("builtins.input", return_value=70.0):
        weight_in_kg = input("Enter Your Weight In Kilogram ", type=FLOAT)
    with patch("builtins.input", return_value=180.0):
        height_in_cm = input("Enter Your Height In Centimeter ", type=FLOAT)
    with patch("builtins.input", return_value=30.0):
        age = input("Enter Your Age ", type=FLOAT)
    with patch("builtins.input", return_value='M'):
        gender = (input("Enter M For Male and F For Female ")).upper()
    e = Edamam(nutrition_appid='da191792', nutrition_appkey='a5d0b8aec59b4b425670b3b30e80666d')
    bmr = bmr_cal(weight_in_kg, height_in_cm, age)
    assert bmr == 1780, f"Expected 1780, but got {bmr}"

def test_bmi_index_calculation():
    with patch("builtins.input", return_value=22.0):
        bmi = input("Enter your BMI: ", type=FLOAT)
    e = Edamam(nutrition_appid='da191792', nutrition_appkey='a5d0b8aec59b4b425670b3b30e80666d')
    bmi_category = bmi_index(bmi)
    assert bmi_category == 'You are normal weight.', f"Expected 'You are normal weight.', but got {bmi_category}"

def test_daily_calorie_needs_calculation():
    with patch("builtins.input", return_value=1800.0):
        bmr = input("Enter your BMR: ", type=FLOAT)
    with patch("builtins.input", return_value=70.0):
        weight = input("Enter your weight: ", type=FLOAT)
    with patch("builtins.input", return_value=3):
        activity_level = int(input("From 1-6 Select your activity level "))
    e = Edamam(nutrition_appid='da191792', nutrition_appkey='a5d0b8aec59b4b425670b3b30e80666d')
    required_calories = daily_calorie_needs(bmr, weight)
    assert required_calories == 2112, f"Expected 2112, but got {required_calories}"


