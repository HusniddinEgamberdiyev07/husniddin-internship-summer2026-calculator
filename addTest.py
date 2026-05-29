from add import add
import unittest as utt

class TestAddFunction(utt.TestCase):

    def test_addPositive(self):
        self.assertEqual(add(2,2), 4)

    def test_addZero(self):
        self.assertEqual(add(2, 0), 2)

    def test_addNegative(self):
        self.assertEqual(add(2, -4), -2)

    def test_addFractions(self):
        self.assertEqual(add(1/2, 1/2), 1)


if __name__ == "__main__":
    utt.main()