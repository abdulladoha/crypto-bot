import unittest
from email_validation import is_valid

class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid("test@example.com"))
        self.assertTrue(is_valid("valid@example.com"))

    def test_invalid_emails(self):
        self.assertFalse(is_valid("invalid@gmail"))
        self.assertFalse(is_valid("invalid"))
        self.assertFalse(is_valid("te#st@example.com"))

if __name__ == "__main__":
    unittest.main()
        