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

    def test_instance_attributes(self):
        my_model = BaseModel()
        my_model.name = "Larvine"
        my_model.account_bal = 9999999999999
        _dict = {'name': "Larvine", 'account_bal': 9999999999999}
        
        for item in _dict.items():
            self.assertIn(item, my_model.__dict__.items()), f"{item} not an instance attribute"