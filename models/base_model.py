#!/usr/bin/python3
"""
base_model module: Defines the BaseModel class.
"""
import models
import uuid
from datetime import datetime
from models.engine.file_storage import storage


class BaseModel:
    """
    BaseModel class: Represents a base model with common attributes and methods
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        It assigns a unique ID, creation time, and update time to the instance.
        """
        if kwargs:
            if "__class__" in kwargs:
                kwargs.pop("__class__")
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    if isinstance(value, str):
                        value = datetime.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel object.
        Format: "[ClassName] (id) {attribute_dict}"
        """

        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the BaseModel object to a dictionary for serialization.

        Returns:
            dict: A dictionary containing the object's attributes and metadata.
        """

        class_name = self.__class__.__name__
        return {
            '__class__': class_name,
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            **self.__dict__
        }
