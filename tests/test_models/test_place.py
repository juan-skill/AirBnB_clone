#!/usr/bin/python3
"""
Test for Place Class
"""
import unittest
import pep8

from models.base_model import BaseModel
from models.place import Place

from datetime import datetime


class TestStringMethods(unittest.TestCase):
    '''
    Testing class
    '''

    @classmethod
    def setUp(cls):
        """ Set up for test"""
        cls.place = Place()
        cls.place.city_id = "5463-abcd"
        cls.place.user_id = "34222-ddcba"
        cls.place.name = "Betty Holberton"
        cls.place.longitude = 100.3

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_attributes_Place(self):
        """ Testing if amenity have attributes."""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)

    def test_is_subclass_Place(self):
        """ if Place is subclass of Basemodel"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)


if __name__ == '__main__':
    unittest.main()
