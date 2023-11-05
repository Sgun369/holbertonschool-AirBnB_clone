#/usrr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(fake_out.getvalue(), "")

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(fake_out.getvalue(), "")

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("")
            self.assertEqual(fake_out.getvalue(), "")

    def test_help_quit(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("help quit")
            self.assertEqual(fake_out.getvalue(), "Quit command to exit the program\n\n")

    def test_do_create_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create")
            self.assertEqual(fake_out.getvalue(), "** class name missing **\n")

    def test_do_create_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create InvalidClass")
            self.assertEqual(fake_out.getvalue(), "** class doesn't exist **\n")


if __name__ == '__main__':
    unittest.main()
