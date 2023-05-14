#!/usr/bin/python3
"""
Defines the State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Define state model subclass

    Attributes:
        name (str): The name of the state

    """
    name = ""
