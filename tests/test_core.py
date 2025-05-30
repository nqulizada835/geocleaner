import unittest
from geoaddresscleaner.core import standardize_address, validate_address

class TestAddressCleaner(unittest.TestCase):
    def test_standardize(self):
        self.assertEqual(
            standardize_address("123 main st, springfield, il 62704"),
            "123 Main St, Springfield, IL 62704"
        )
        self.assertEqual(
            standardize_address("123 main st springfield il 62704"),
            "123 Main St, Springfield, IL 62704"
        )
        self.assertEqual(
            standardize_address("456 oak ln, smithville tx 76520-1234"),
            "456 Oak Ln, Smithville, TX 76520-1234"
        )

    def test_validate(self):
        self.assertTrue(validate_address("123 main st, springfield, il 62704"))
        self.assertTrue(validate_address("456 oak ln, smithville tx 76520-1234"))
        self.assertFalse(validate_address("not an address"))
        self.assertFalse(validate_address("123 main st, springfield, zz 62704"))  # Invalid state

if __name__ == '__main__':
    unittest.main()
