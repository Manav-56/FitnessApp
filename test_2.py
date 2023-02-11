from logic import bmi_index
import unittest


class TestBMICalculator(unittest.TestCase):
    def test_calculate_bmi(self):
        bmi = 18.5
        expected_result = 'You are underweight.'
        result = bmi_index(bmi)
        self.assertEqual(result, expected_result)

    def test_bmi_index(self):
        # Test underweight
        bmi = 17.5
        expected_result = 'You are underweight.'
        result = bmi_index(bmi)
        self.assertEqual(result, expected_result)

        # Test normal weight
        bmi = 22.5
        expected_result = 'You are normal weight.'
        result = bmi_index(bmi)
        self.assertEqual(result, expected_result)

        # Test overweight
        bmi = 27.5
        expected_result = 'You are overweight.'
        result = bmi_index(bmi)
        self.assertEqual(result, expected_result)

        # Test obese
        bmi = 32.5
        expected_result = 'You are obese.'
        result = bmi_index(bmi)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
