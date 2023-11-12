#!/usr/bin/python3
"""
base_model module: Defines the BaseModel class.
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class: Represents a base model with common attributes and methods
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        If instantiated with keyword arguments (kwargs),
        it reconstructs the object from a dictionary representation.
        Otherwise, it assigns a unique ID, creation time,
        and update time to the instance and adds it to the storage.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current
        datetime and saves the changes to the storage.

        This method updates the 'updated_at' attribute of the object with the
        current datetime and then triggers the storage to save the changes.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the BaseModel object to a dictionary for serialization.

        Returns:
            dict: A dictionary containing the object's attributes and metadata,
            suitable for serialization.
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
