import unittest 
from fax import parse_number


class TestParseNumber(unittest.TestCase):
    def test_parse_number(self):
        num1 = [
            "   ",
            "  |",
            "  |",
            "   "]
        
        num2 = [
            " _ ",
            " _|",
            "|_ ",
            "   "]

        self.assertEqual(1,parse_number(0,1, num1))
        self.assertEqual(2,parse_number(0,1, num2))