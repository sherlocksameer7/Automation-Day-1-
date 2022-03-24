import unittest

def check_even_or_odd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"


class My_App_Even_or_Odd(unittest.TestCase):

    def test_case_check_even_or_odd1(self):
        result = check_even_or_odd(2)
        self.assertEqual(result, "even")

    def test_case_check_even_or_odd2(self):   # test_case we put is mandatory !!! ***
        result = check_even_or_odd(5)
        self.assertEqual("odd", result)  # or we write like assertNotEqual("even", result) ***


if __name__ == "__main__":
    unittest.main()