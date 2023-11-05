#!/usr/bin/python3
from console import HBNBCommand
import unittest
import sys
sys.path.append('../..')


class TestHBNBCommand(unittest.TestCase):
    """Test suite for HBNBcommand functionality"""
    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down after test execution"""
        pass

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(fake_out.getvalue(), "")

    def test_EOF(self):
        """Test the EOF command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(fake_out.getvalue(), "")

    def test_emptyline(self):
        """Test an emptyy line input"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("")
            self.assertEqual(fake_out.getvalue(), "")

    def test_help_quit(self):
        """Test the help quit command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("help quit")
            self.assertEqual(fake_out.getvalue(),
                             "Quit command to exit the program\n\n")

    def test_do_create_missing_class(self):
        """Test create command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create")
            self.assertEqual(fake_out.getvalue(), "** class name missing **\n")

    def test_do_create_invalid_class(self):
        """Test create command with an invalid class name"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create InvalidClass")
            self.assertEqual(fake_out.getvalue(),
                             "** class doesn't exist **\n")


if __name__ == '__main__':
    unittest.main()
