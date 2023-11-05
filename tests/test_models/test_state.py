import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_state_name_default_value(self):
        """Test that the default value of the state name is an empty string."""
        state = State()
        self.assertEqual(state.name, "")

    def test_state_name_assignment(self):
        """Test that the state name can be assigned correctly."""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")


if __name__ == '__main__':
    unittest.main()
