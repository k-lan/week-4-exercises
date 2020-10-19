import unittest
import recursion


class TestRecursion(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(recursion.fibonacci(10), 34)
        self.assertEqual(recursion.fibonacci_slow(10), 34)

        self.assertEqual(recursion.fibonacci(2), 1)
        self.assertEqual(recursion.fibonacci_slow(2), 1)

    def test_reverse(self):
        self.assertEqual(recursion.reverse("hello"), "olleh")
        self.assertEqual(recursion.reverse("how are you"), "uoy era woh")

    def test_factorial(self):
        self.assertEqual(recursion.factorial(7), 5040)
        self.assertEqual(recursion.factorial(5), 120)
        self.assertEqual(recursion.factorial(1), 1)