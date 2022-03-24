
import unittest

class My_Second_App(unittest.TestCase):

    def test_case3(self):
        pass                                # we have to give like that tooo !!!

class My_First_App(unittest.TestCase):

    def test_case1(self):
        pass

    def test_case2(self):
        pass

if __name__ == "__main__":     # if condition is in the import indentation !!!
    unittest.main()