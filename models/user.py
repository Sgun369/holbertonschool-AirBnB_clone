#!/usr/bin/python3
"""User module: Contains the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class: Represents a user with:
    email, password, first name, and last name."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
