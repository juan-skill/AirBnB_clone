#!/usr/bin/python3
"""doc"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """doc"""

    def __init__(self, *args, **kwargs):
        """doc"""
        if kwargs:

            for key in kwargs.keys():
                if key == 'created_at' or key == 'updated_at':
                    kwargs[key] = datetime.strptime(
                        kwargs[key],
                        "%Y-%m-%dT%H:%M:%S.%f")

                if key != '__class__':
                    setattr(self, key, kwargs[key])

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """doc"""
        return "[{}] ({}) {}".format(
            str(type(self).__name__),
            self.id,
            self.__dict__)

    def save(self):
        """doc"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """doc"""
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = str(type(self).__name__)
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
