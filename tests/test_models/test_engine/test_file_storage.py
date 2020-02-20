#!/usr/bin/python3

import unittest
import pep8

from models.base_model import BaseModel
from models.engine.filestorage import FileStorage

from datetime import datetime


class TestStringMethods(unittest.TestCase):
    """
    Testing class
    """

    def setUp(self):
        self.store = FileStorage()

        test_args = {'updated_at': datetime(2019, 2, 20, 00, 01, 43, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900)}
        self.model = BaseModel(test_args)

        self.test_len = 0
        if os.path.isfile("file.json"):
            self.test_len = len(self.store.all())

    def tearDown(self):
        import os
        if os.path.isfile("file.json"):
            os.remove('file.json')

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
