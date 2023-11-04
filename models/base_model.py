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

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        It assigns a unique ID, creation time, and update time to the instance.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the BaseModel object to a dictionary for serialization.

        Returns:
            dict: A dictionary containing the object's attributes and metadata.
        """
        return {
            'my_number': self.__dict__.get('my_number'),
            'name': self.__dict__.get('name'),
            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at.isoformat(),
            'id': self.id,
            'created_at': self.created_at.isoformat()
        }
