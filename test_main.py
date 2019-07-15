import unittest

target = __import__("lambda-handler")
validate = target.validate
calculate = target.calculateNumeral

class TestValidation(unittest.TestCase):
    def test_invalid_numeral(self):
        """
        Test that invalid characters in a numeral are caught and fail validation
        """
        numeral = "o"
        response = validate(numeral)
        self.assertFalse(response['statusCode'] == 200, numeral + " should not be valid numeral")

        numeral = "abc"
        response = validate(numeral)
        self.assertFalse(response['statusCode'] == 200, numeral + " should not be valid numeral")

    def test_invalid_sequence(self):
        """
        Test that invalid sequences of numeral are caught during validation
        """
        numeral = "IVX"
        response = validate(numeral)
        self.assertFalse(response['statusCode'] == 200, numeral + " should not be a valid numeral sequence")

        numeral = "VXV"
        response = validate(numeral)
        self.assertFalse(response['statusCode'] == 200, numeral + " should not be a valid numeral sequence")

        numeral = "VXL"
        response = validate(numeral)
        self.assertFalse(response['statusCode'] == 200, numeral + " should not be a valid numeral sequence")

        numeral = "LC"
        response = validate(numeral)
        self.assertFalse(response['statusCode'] == 200, numeral + " should not be a valid numeral sequence")

class TestCalculation(unittest.TestCase):
    def test_single_numeral(self):
        """
        Test that single numeral have the proper value
        """
        numeral = "I"
        response = calculate(numeral)
        self.assertEqual(response['body'], 1)

        numeral = "V"
        response = calculate(numeral)
        self.assertEqual(response['body'], 5)

        numeral = "X"
        response = calculate(numeral)
        self.assertEqual(response['body'], 10)

        numeral = "L"
        response = calculate(numeral)
        self.assertEqual(response['body'], 50)

        numeral = "C"
        response = calculate(numeral)
        self.assertEqual(response['body'], 100)

        numeral = "D"
        response = calculate(numeral)
        self.assertEqual(response['body'], 500)

        numeral = "M"
        response = calculate(numeral)
        self.assertEqual(response['body'], 1000)

    def test_subtraction(self):
        """
        Test subtraction scenarios
        """
        numeral = "IV"
        response = calculate(numeral)
        self.assertEqual(response['body'], 4)

        numeral = "IX"
        response = calculate(numeral)
        self.assertEqual(response['body'], 9)

        numeral = "IL"
        response = calculate(numeral)
        self.assertEqual(response['body'], 49)

        numeral = "IC"
        response = calculate(numeral)
        self.assertEqual(response['body'], 99)

        numeral = "ID"
        response = calculate(numeral)
        self.assertEqual(response['body'], 499)

        numeral = "IM"
        response = calculate(numeral)
        self.assertEqual(response['body'], 999)

        numeral = "XL"
        response = calculate(numeral)
        self.assertEqual(response['body'], 40)

        numeral = "XC"
        response = calculate(numeral)
        self.assertEqual(response['body'], 90)

        numeral = "XD"
        response = calculate(numeral)
        self.assertEqual(response['body'], 490)

        numeral = "XM"
        response = calculate(numeral)
        self.assertEqual(response['body'], 990)

        numeral = "CD"
        response = calculate(numeral)
        self.assertEqual(response['body'], 400)

        numeral = "CM"
        response = calculate(numeral)
        self.assertEqual(response['body'], 900)

        numeral = "MCDXCIV"
        response = calculate(numeral)
        self.assertEqual(response['body'], 1494)

    def test_addition(self):
        """
        Test addition scenarios
        """
        numeral = "MDCLXVI"
        response = calculate(numeral)
        self.assertEqual(response['body'], 1666)

        numeral = "IIIV"
        response = calculate(numeral)
        self.assertFalse(response['statusCode'] == 200, numeral + " should not be a valid numeral sequence")

        numeral = "IXXC"
        response = calculate(numeral)
        self.assertFalse(response['statusCode'] == 200, numeral + " should not be a valid numeral sequence")

if __name__ == '__main__':
    unittest.main()