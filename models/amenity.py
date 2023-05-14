#!/usr/bin/python3
"""
Module for Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Define amenity subclass

    Attributes:
        name(str): amenity name

    """
    name = ""
