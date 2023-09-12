#!/usr/bin/python3
""" Define string to json function """
import json

def to_json_string(my_obj):
    """ return JSON representation of string"""
    return json.dump(my_obj)

