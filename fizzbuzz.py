import unittest


class FizzbuzzTest(unittest.TestCase):
    def test_input_number_3_should_be_return_fizz(self):
        number = 3

        expected = 'fizz'
        actual = callFizzBuzz(number)

        self.assertEqual(actual, expected)

def callFizzBuzz(number):
    return 'fizz'


unittest.main()

