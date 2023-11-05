import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.review = Review()

    def test_place_id_default_value(self):
        """Test that the default value of place_id is an empty string."""
        self.assertEqual(self.review.place_id, "")

    def test_user_id_default_value(self):
        """Test that the default value of user_id is an empty string."""
        self.assertEqual(self.review.user_id, "")

    def test_text_default_value(self):
        """Test that the default value of text is an empty string."""
        self.assertEqual(self.review.text, "")


if __name__ == '__main__':
    unittest.main()
