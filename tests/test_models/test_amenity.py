#!/usr/bin/python3

import unittest
import pep8

from models.base_model import BaseModel
from models.amenity import Amenity

from datetime import datetime


class TestStringMethods(unittest.TestCase):
    """
    Testing class
    """
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
