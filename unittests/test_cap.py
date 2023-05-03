"""
Unit tests for cap.py
"""
import unittest

import cap


class TestCap(unittest.TestCase):
    """
    Unit tests to test cap.py
    """

    def test_one_word(self):
        """
        test one word
        :return:
        """
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_two_word(self):
        """
        test two word
        :return:
        """
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')


if __name__ == '__main__':
    unittest.main()
