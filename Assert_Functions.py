import unittest

class My_Second_App(unittest.TestCase):

    def test_case3(self):
        self.assertEqual("Hello", "Hello")                            # we have to give like that tooo !!!

class My_First_App(unittest.TestCase):

    def test_case1(self):
        a = 10
        b = 4
        c = a + b
        self.assertEqual(a+b, c)  # we give adding or will be in automation methods !!! and we give 14 also

    def test_case2(self):
        self.assertNotEqual("Hello", "Sameer")  # It checks the string will be in not Equal !!!

if __name__ == "__main__":     # if condition is in the import indentation !!!
    unittest.main()