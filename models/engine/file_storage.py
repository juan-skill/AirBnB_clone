#!/usr/bin/python3
"""doc"""


from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
#from models import *
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
        """doc"""
        return FileStorage.__objects

    def new(self, obj):
        """doc"""
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        FileStorage.__objects.update({key: obj})

    def save(self):
        """ Serialize __objects to the JSON file """
        #print('FileStorage.__objects ===',FileStorage.__objects)

        JSON_dict_dump = {}
        for key in FileStorage.__objects.keys():
            JSON_dict_dump[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, mode='w', encoding='UTF-8') as f:
            json.dump(JSON_dict_dump, f)

    def reload(self):
        """doc"""

        nc = {"BaseModel": BaseModel,
              "User": User,
              "Place": Place,
              "State": State,
              "City": City,
              "Amenity": Amenity,
              "Review": Review}

        try:
            with open(FileStorage.__file_path, mode='r', encoding="UTF-8") as f:
                json_d_load = json.load(f)
                #json_d_load = json.load(f)
                #print('json_d_load', json_d_load, end='\n\n')

            for key in json_d_load:
                #print('key===', key, end='\n\n')
                #print('json_d_load[key]===', json_d_load[key], end='\n\n')
                #print('json_d_load[key]["__class__"]===', json_d_load[key]['__class__'], end='\n\n')

                # Access Nested Dictionary Items
                class_obj = json_d_load[key]["__class__"]
                # Explicit Type Conversion  (required type) (expressio)
                #                           (type(obj)) (**kwargs)
                FileStorage.__objects[key] = nc[class_obj](**json_d_load[key])


        except Exception:
            pass
