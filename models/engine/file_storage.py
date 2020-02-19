#!/usr/bin/python3
""" This Class define FileStorage Class"""

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage:
    """ Class that serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored (dictionary persistents)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary of persistent objects."""
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        FileStorage.__objects.update({key: obj})

    def save(self):
        """ Serialize __objects to the JSON file """

        JSON_dict_dump = {}
        for key in FileStorage.__objects.keys():
            JSON_dict_dump[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, mode='w', encoding='UTF-8') as f:
            json.dump(JSON_dict_dump, f)

    def reload(self):
        """ Serializes __objects to the JSON file (path: __file_path) """

        nc = {"BaseModel": BaseModel,
              "User": User,
              "Place": Place,
              "State": State,
              "City": City,
              "Amenity": Amenity,
              "Review": Review}

        try:
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                json_d_load = json.load(f)

            for key in json_d_load:

                class_obj = json_d_load[key]["__class__"]

                FileStorage.__objects[key] = nc[class_obj](**json_d_load[key])

        except Exception:
            pass
