import unittest

def check_divisible_by_7(x):
    if x % 7 == 0:
        return True
    else:
        return False

class Check_Divisible_by_7(unittest.TestCase):

    def test_case_1_check_divisible_by_7(self):
        result = check_divisible_by_7(14)
        self.assertTrue(result)

    def test_case_2_check_divisible_by_7(self):
        result = check_divisible_by_7(6)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()