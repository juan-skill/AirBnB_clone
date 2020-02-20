#!/usr/bin/python3

import unittest
import pep8
import uuid
from models.base_model import BaseModel
from models.user import User

from datetime import datetime


class TestStringMethods(unittest.TestCase):
    '''
    Testing class
    '''

    my_model = BaseModel()

    def setUp(self):
        ''' Verify the persistent structur file.'''
        try:
            remove("file.json")
        except:
            pass

    def tearDown(self):
        ''' '''
        try:
            remove("file.json")
        except:
            pass

    def test_Base_Model(self):
        '''Sets the object instance.'''
        self.my_model.name = "Holberton"
        self.my_model.my_number = 89


    def test_types_obj(self):
        '''Test object type'''
        self.assertTrue(type(self.my_model),
                        "<class 'models.base_model.BaseModel'>")

    def test_types(self):
        '''Test type values of object'''
        self.assertTrue(type(self.my_model.created_at),
                        "<class 'datetime.datetime'>")
        self.assertEqual(str(type(self.my_model.updated_at)),
                         "<class 'datetime.datetime'>")


    def test_no_send_argument(self):
        '''Test if we sent argument to init '''
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        self.assertEqual("""__init__() missing 1 required"""+
                         """ positional argument: 'self'""", str(e.exception))

    def test_id_uniq(self):
        '''Test if the unique id '''
        all_objs = []
        for i in range(34):
            all_objs.append(BaseModel().id)
        self.assertEqual(len(all_objs), len(set(all_objs)))

    def test_to_dict_method(self):
        '''Test correspondig values of obj '''
        new_dict = self.my_model.to_dict()
        self.assertEqual(new_dict["id"], self.my_model.id)
        self.assertEqual(new_dict["name"], self.my_model.name)
        self.assertEqual(new_dict["updated_at"], self.my_model.updated_at.isoformat())
        self.assertEqual(new_dict["created_at"], self.my_model.created_at.isoformat())


    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
