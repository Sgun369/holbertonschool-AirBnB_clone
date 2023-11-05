#!/usr/bin/python3
"""City module: Contains the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """City class: Represents a\
        city with state information."""
    state_id = ""
    name = ""
