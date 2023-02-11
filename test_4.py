import unittest
from unittest.mock import patch
from py_edamam import Edamam

class TestEdamam(unittest.TestCase):
    @patch('builtins.input', return_value='1 apple')
    def test_search_nutrient(self, mock_input):
        e = Edamam(nutrition_appid='da191792',
                   nutrition_appkey='a5d0b8aec59b4b425670b3b30e80666d')
        b = e.search_nutrient(str(input('enter food ')))
        self.assertEqual(b["calories"], 94)
        self.assertEqual(b["totalNutrients"]['FAT']['quantity'], 0.3094)
        self.assertEqual(b["totalNutrients"]['SUGAR']['quantity'], 18.9098)
        self.assertEqual(b["totalNutrients"]['PROCNT']['quantity'], 0.4732)

if __name__ == '__main__':
    unittest.main()

