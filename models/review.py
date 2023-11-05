#!/usr/bin/python3
"""Review module: Contains the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class: Represents a user review of a place."""
    place_id = ""
    user_id = ""
    text = ""
