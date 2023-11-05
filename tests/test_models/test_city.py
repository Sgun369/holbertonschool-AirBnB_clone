#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test class for the city model"""
    def setUp(self):
        """Set up test"""
        self.city = City()

    def test_state_id_default_value(self):
        """Test default state ID value"""
        self.assertEqual(self.city.state_id, "")

    def test_name_default_value(self):
        """Test default name value"""
        self.assertEqual(self.city.name, "")

    def test_state_id_assignment(self):
        """Tet state ID assignment"""
        self.city.state_id = "CA"
        self.assertEqual(self.city.state_id, "CA")

    def test_name_assignment(self):
        """Test name assignment"""
        self.city.name = "San Francisco"
        self.assertEqual(self.city.name, "San Francisco")


if __name__ == '__main__':
    unittest.main()
