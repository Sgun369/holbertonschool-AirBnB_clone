#!/usr/bin/python3
"""console module"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "Amenity",
        "City",
        "Place",
        "Review",
        "State"
    }

    def do_quit(self, arg):
        """quit command to exit console"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit console"""
        return True

    def emptyline(self):
        """doesn't execute anything"""
        pass

    def help_quit(self):
        """help quit command"""
        print("Quit command to exit the program\n")

    def do_create(self, arg=None):
        """Create an instance of class"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg)().id)
            storage.save()

    def do_show(self, arg):
        """show instance based on class name and ID"""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Destroy an instance based on class name and Id"""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Display all instances based on class name"""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)

    def do_update(self, arg):
        """update an instance attribute"""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        elif len(argl) < 3:
            print("** attribute name missing **")
        elif len(argl) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(argl[0], argl[1])
            instance = objdict[key]
            setattr(instance, argl[2], argl[3].strip('"'))
            storage.save()


def parse(arg):
    """Convert a series arguments to an argument list"""
    return list(map(str, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
