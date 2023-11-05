import unittest
from unittest.mock import patch
from io import StringIO
import sys
from console import HBNBCommand


class TestHBNBCommandMethods(unittest.TestCase):
    def setUp(self):
        """Set up the HBNBCommand instance for testing"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down after testing"""
        pass

    def capture_output(self, func, *args):
        """Capture the output of the function execution"""
        captured_output = StringIO()
        sys.stdout = captured_output
        func(*args)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip()

    def test_quit_command(self):
        """Test quit command"""
        self.assertTrue(self.console.do_quit(""))

    def test_EOF_command(self):
        """Test EOF command"""
        self.assertTrue(self.console.do_EOF(""))

    def test_emptyline(self):
        """Test emptyline method"""
        self.assertIsNone(self.console.emptyline())

    def test_help_quit(self):
        """Test help for quit command"""
        captured_output = self.capture_output(self.console.help_quit)
        self.assertEqual(captured_output, "Quit command to exit the program")

    def test_create_missing_class_name(self):
        """Test create command with missing class name"""
        captured_output = self.capture_output(self.console.do_create)
        self.assertEqual(captured_output, "** class name missing **")

    def test_create_invalid_class_name(self):
        """Test create command with invalid class name"""
        captured_output = self.capture_output(
            self.console.do_create, "InvalidClassName")
        self.assertEqual(captured_output, "** class doesn't exist **")

    def test_create_valid_class(self):
        """Test create command with valid class name"""
        captured_output = self.capture_output(self.console.do_create, "User")
        self.assertTrue(captured_output)  # Ensure that an ID is generated

    def test_show_missing_class_name(self):
        """Test show command with missing class name"""
        captured_output = self.capture_output(self.console.do_show, "")
        self.assertEqual(captured_output, "** class name missing **")


if __name__ == '__main__':
    unittest.main()
