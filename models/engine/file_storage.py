#!/usr/bin/python3
"""Defines the FileStorage class."""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import json


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f, indent=2)

    def reload(self):
        """Deserializes the JSON file to instances in __objects."""
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                loaded_data = json.load(f)
                for key, value in loaded_data.items():
                    obj_id = key.split(".")[1]
                    # Extract and remove the class name
                    obj_class = value.pop("__class__")
                    # Create an instance using the class name and data
                    obj_instance = globals()[obj_class](**value)
                    obj_instance.id = obj_id  # Set the object's ID separately
                    # Store the instance in __objects
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass  # file is not found
