from logic import bmi_index
import pytest


@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (31, 'You are obese.'),
                             (29, 'You are overweight.'),
                             (16, 'You are underweight.')
                         ]
                         )
def test_calc_square(test_input, expected_output):
    result = bmi_index(test_input)
    assert result == expected_output

