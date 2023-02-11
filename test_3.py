import unittest
from unittest.mock import patch
from bmi import daily_calorie_needs


class TestDailyCalorieNeeds(unittest.TestCase):
    @patch('builtins.input', return_value='1')
    def test_activity_level_1(self, mock_input):
        bmr = 2000
        weight = 100
        expected = 2400
        self.assertEqual(daily_calorie_needs(bmr, weight), expected)

    @patch('builtins.input', return_value='6')
    def test_activity_level_6(self, mock_input):
        bmr = 2000
        weight = 100
        expected = 3000
        self.assertEqual(daily_calorie_needs(bmr, weight), expected)

    @patch('builtins.input', return_value='4')
    def test_activity_level_4(self, mock_input):
        bmr = 2000
        weight = 100
        expected = 2750
        self.assertEqual(daily_calorie_needs(bmr, weight), expected)


if __name__ == '__main__':
    unittest.main()
