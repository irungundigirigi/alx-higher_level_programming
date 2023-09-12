#!/usr/bin/python3
""" Defines module to create object from JSON File"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a given JSON file"""
    with open(filename) as f:
        return json.load(f)
