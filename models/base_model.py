#!/usr/bin/python3

'''Base Class for all models
'''
from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''Base Model class
    '''
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        to_dict = {}
        for key, value in self.__dict__.items():
            to_dict[key] = value
        
        to_dict['__class__'] = self.__class__.__name__
        to_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.now()
        to_dict['update_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return to_dict
