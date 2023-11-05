import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_amenity_name_default_value(self):
        """Test that the default value of the amenity name
        is an empty string."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_name_assignment(self):
        """Test that the amenity name can be assigned a new value."""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")


if __name__ == '__main__':
    unittest.main()
