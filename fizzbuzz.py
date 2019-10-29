import unittest


class FizzbuzzTest(unittest.TestCase):
    def test_input_number_3_should_be_return_fizz(self):
        number = 3

        expected = 'fizz'
        actual = callFizzBuzz(number)

        self.assertEqual(actual, expected)

    def test_input_number_6_should_be_return_fizz(self):
        number = 6

        expected = 'fizz'
        actual = callFizzBuzz(number)

        self.assertEqual(actual, expected)

    def test_input_number_5_should_return_buzz(self):
        number = 5

        expected = 'buzz'
        actual = callFizzBuzz(number)

        self.assertEqual(actual, expected)

    def test_input_number_15_should_return_buzz(self):
        number = 15

        expected = 'fizzbuzz'
        actual = callFizzBuzz(number)

        self.assertEqual(actual, expected)

    def test_input_number_20_should_return_buzz(self):
        number = 20

        expected = 'buzz'
        actual = callFizzBuzz(number)

        self.assertEqual(actual, expected)

    def test_input_number_30_should_return_FizzBuzz(self):
        number = 30

        expected = 'fizzbuzz'
        actual = callFizzBuzz(number)

        self.assertEqual(actual, expected)

    def test_input_number_45_should_retuern_Fizzbuzz(self):
        number = 45

        expected = 'fizzbuzz'
        actual = callFizzBuzz(number)

        self.assertEqual(actual, expected)

    def test_input_number_60_should_return_Fizzbuzz(self):
        number = 60

        expected = 'fizzbuzz'
        actual = callFizzBuzz(number)

        self.assertEqual(actual, expected)

def callFizzBuzz(number):
    if number % 3 == 0  and number % 5 == 0:
        return 'fizzbuzz'
    if number % 5 == 0:
        return 'buzz'
    if number % 3 == 0:
        return 'fizz'

unittest.main()

