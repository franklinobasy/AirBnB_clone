'''file_storage.py
'''
import json

class FileStorage:
    '''FileStorage class:
    that serializes instances to a JSON file and 
    deserializes JSON file to instances

    __file_path: 
        string - path to the JSON file (ex: file.json)
    __objects: 
        dictionary - empty but will store all objects by <class name>.id
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects
        '''
        
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id
        '''

        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = {}

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)
        '''

        with open(FileStorage.__file_path, 'w') as f_obj:
            json.dump(FileStorage.__objects, f_obj)

    def reload(self):
        ''' deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists
        '''

        try:
            with open(FileStorage.__file_path, 'w') as f_obj:
                FileStorage.__objects = json.load(f_obj)
        except FileNotFoundError as e:
            pass
    