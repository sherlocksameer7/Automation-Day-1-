import unittest

def add(x, y):
    return x+y

class App1(unittest.TestCase):

    def test_case_add1(self):
        a = 6
        b = 8
        c = add(a, b)
        self.assertEqual(c, a+b)


    def test_case_add2(self):
        a = 67.90
        b = 56.32
        c = add(a, b)
        self.assertEqual(a+b, c)


    def test_case_add3(self):
        a = -17
        b = -4
        c = add(a, b)
        self.assertEqual(c, a+b)   # Also with Negative also working !!!


if __name__ == "__main__":
    unittest.main()
