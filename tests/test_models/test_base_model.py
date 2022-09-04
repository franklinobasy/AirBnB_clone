from models.base_model import BaseModel

from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    '''Class to test Base Model
    '''
    def test_id(self):
        my_model = BaseModel()
        self.assertEqual(str, type(my_model.id))

    def test_created_at(self):
        my_model = BaseModel()
        date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        self.assertEqual(my_model.created_at.strftime("%Y-%m-%dT%H:%M:%S"), date)