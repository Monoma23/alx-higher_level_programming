#!/usr/bin/python3
"""Almost a circle foundation"""
import json


class Base:
    """the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """this is our constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string representation of list_dictionaries ok"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json representation to a file"""
        file_name = cls.__name__ + ".json"
        nouveau_list = []
        if list_objs is not None:
            for i in list_objs:
                nouveau_list.append(cls.to_dictionary(i))
        with open(file_name, 'w') as json_file:
            json_file.write(cls.to_json_string(nouveau_list))

    def from_json_string(json_string):
        """returns a list of json string representation jojo"""
        if json_string is None or json_string == 0:
            return []
        return json.loads(json_string)
