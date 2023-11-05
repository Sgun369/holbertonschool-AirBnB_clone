#:=!/usr/bin/python3
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_state_id_default_value(self):
        self.assertEqual(self.city.state_id, "")

    def test_name_default_value(self):
        self.assertEqual(self.city.name, "")

    def test_state_id_assignment(self):
        self.city.state_id = "CA"
        self.assertEqual(self.city.state_id, "CA")

    def test_name_assignment(self):
        self.city.name = "San Francisco"
        self.assertEqual(self.city.name, "San Francisco")

if __name__ == '__main__':
    unittest.main()
