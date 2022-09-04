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

    def test_updated_at(self):
        try:
            my_model = BaseModel()
            updated_at = my_model.updated_at
            my_model.save()

            self.assertNotEqual(updated_at, my_model.updated_at), \
                    "updated_at not changeing after new modification"
        except AssertionError as e:
            print(e)

    def test_instance_attributes(self):
        try:
            my_model = BaseModel()
            my_model.name = "Larvine"
            my_model.account_bal = 9999999999999

            _dict = {'name': "Larvine", 'account_bal': 9999999999999}
            
            for item in _dict.items():
                self.assertIn(item, my_model.__dict__.items()), \
                                f"{item} not an instance attribute"
        except AssertionError as e:
            print(e)

    def test_to_dict(self):
        try:
            my_model = BaseModel()
            my_model.name = "My_First_Model"
            my_model.my_number = 89

            my_model_json = my_model.to_dict()
            my_new_model = BaseModel(**my_model_json)
            
            self.assertEqual("<class 'datetime.datetime'>",\
                    type(my_new_model.created_at)), "created_at not a datetime object"
        except AssertionError as e:
            print(e)
