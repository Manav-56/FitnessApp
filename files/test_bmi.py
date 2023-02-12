import unittest
from unittest.mock import patch
from bmi import (
    MetabolicRate,
    BodyMassIndex,
    DailyCalorieNeeds,
    CalFatProtienSugarForFood,
)


class TestMetabolicRate(unittest.TestCase):
    @patch("bmi.PUT_TEXT")
    def test_bmr_cal_male(self, mock_put_text):
        weight_in_kg = 70
        height_in_cm = 170
        age = 25
        gender = "M"
        mr = MetabolicRate(weight_in_kg, height_in_cm, age, gender)
        mr.bmr_cal()
        mock_put_text.assert_called_once_with("Your Basal metabolic rate is 1642 kcal.")

    @patch("bmi.PUT_TEXT")
    def test_bmr_cal_female(self, mock_put_text):
        weight_in_kg = 60
        height_in_cm = 160
        age = 21
        gender = "F"
        mr = MetabolicRate(weight_in_kg, height_in_cm, age, gender)
        mr.bmr_cal()
        mock_put_text.assert_called_once_with("Your Basal metabolic rate is 1334 kcal.")


class TestBodyMassIndex(unittest.TestCase):
    @patch("bmi.PUT_TEXT")
    def test_bmi_index(self, mock_put_text):
        # Test underweight
        bmi = BodyMassIndex(18.0)
        bmi.bmi_index()
        mock_put_text.assert_called_once_with("You are underweight.")
        mock_put_text.reset_mock()

        # Test normal weight
        bmi = BodyMassIndex(22.0)
        bmi.bmi_index()
        mock_put_text.assert_called_once_with("You are normal weight.")
        mock_put_text.reset_mock()

        # Test overweight
        bmi = BodyMassIndex(27.0)
        bmi.bmi_index()
        mock_put_text.assert_called_once_with("You are overweight.")
        mock_put_text.reset_mock()

        # Test obese
        bmi = BodyMassIndex(32.0)
        bmi.bmi_index()
        mock_put_text.assert_called_once_with("You are obese.")


class TestDailyCalorieNeeds(unittest.TestCase):
    @patch("bmi.PUT_TEXT")
    @patch("bmi.INPUT", return_value=1)
    def test_daily_calorie_needs(self, mock_input, mock_put_text):
        weight = 80
        bmr = 1000
        calorie_needs = DailyCalorieNeeds(bmr, weight)
        calorie_needs.daily_calorie_needs()

        mock_put_text.assert_any_call(
            "Daily calorie needs for maintaning weight is 1200."
        )
        mock_put_text.assert_any_call("FOR BULKING YOUR CALORIES :")
        mock_put_text.assert_any_call("You need 350 calorie and 38 grams of fat.")
        mock_put_text.assert_any_call("You need 560 calorie and 140 grams of protein.")
        mock_put_text.assert_any_call("You need 490 calorie and 122 grams of carbs.")

        mock_put_text.assert_any_call("FOR MAINTAING YOUR CALORIES :")
        mock_put_text.assert_any_call("You need 300 calorie and 33 grams of fat.")
        mock_put_text.assert_any_call("You need 480 calorie and 120 grams of protein.")
        mock_put_text.assert_any_call("You need 420 calorie and 105 grams of carbs.")

        mock_put_text.assert_any_call("FOR LOOSING YOUR CALORIES :")
        mock_put_text.assert_any_call("You need 300 calorie and 33 grams of fat.")
        mock_put_text.assert_any_call("You need 704 calorie and 176 grams of protein.")
        mock_put_text.assert_any_call("You need 196 calorie and 49 grams of carbs.")


class TestCalFatProtienSugarForFood(unittest.TestCase):
    @patch("bmi.PUT_TEXT")
    def test_search_nutrient(self, mock_put_text):
        food = "1 apple"
        bmi_calculator = CalFatProtienSugarForFood(food)
        bmi_calculator.search_nutrient()

        expected_output = [
            "CALORIES: 94 cal",
            "FAT: 0.3094 g",
            "SUGAR: 18.9098 g",
            "PROTEIN: 0.4732 g",
        ]

        self.assertEqual(mock_put_text.call_args_list[0][0][0], expected_output[0])
        self.assertEqual(mock_put_text.call_args_list[1][0][0], expected_output[1])
        self.assertEqual(mock_put_text.call_args_list[2][0][0], expected_output[2])
        self.assertEqual(mock_put_text.call_args_list[3][0][0], expected_output[3])
