import unittest
import postfixthreefour


class TestPostfix(unittest.TestCase):
    def test_postfix_convert(self):  # Testing threefour postfix converter
        self.assertEqual(postfixthreefour.infix_to_postfix("A*B+C*D"), "A B * C D * +")
        self.assertEqual(postfixthreefour.infix_to_postfix("A**B // C"), "A B ** C //")
        self.assertEqual(postfixthreefour.infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"),
                         "A B + C * D E - F G + * -")
        self.assertEqual(postfixthreefour.infix_to_postfix("6 // 1.5"), "6 1.5 //")

    def test_postfix_calc(self):
        self.assertEqual(postfixthreefour.infix_calc("5 * 3 // 6.0"), 2.0)
