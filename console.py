#!/usr/bin/python3
'''Entry point of the command interpreter
'''
import cmd
import json

import models
from models import BaseModel, User


class HBNBCommand(cmd.Cmd):
    '''Shell for database
    '''

    prompt = '(hbnb) '
    model_list = ['BaseModel', 'User']
    

    @classmethod
    def handle_errors(cls, args, **kwargs):
        if not args:
            args = ()
        else:
            args = tuple(args.split(" "))

        n  = len(args)
        if n < 1:
            print("** class name missing **")
            return True

        if args[0] not in HBNBCommand.model_list:
            print("** class doesn't exist **")
            return True

        if 'command' not in  kwargs:
            return False

        for arg in kwargs.values():
            if arg in ['create', 'show', 'destroy', 'all']:
                if n < 2:
                    print("** instance id missing **")
                    return True
            elif arg in ['update']:
                if n < 2:
                    print("** instance id missing **")
                    return True
                elif n < 3:
                    print("** attribute name missing **")
                    return True
                elif n < 4:
                    print("** value missing **")
                    return True
                
        return False

    def do_quit(self, args):
        ''' command to quit the interpreter'''

        return True

    def help_quit(self):
        doc = '''
        This command quits the interpreter
        Usage:
            (hbnb) quit
        '''

        print(doc)

    def do_EOF(self, args):
        '''Handles end of line'''

        return True

    def help_EOF(self):
        doc = '''
        This command handles EOF
        Usage:
            (hnbn) <Ctrl-d>
        '''

        print(doc)

    def do_create(self, args):
        '''
        Creates a new instance of a class, saves it to JSON
        file, prints the instance id

        Args:
            args: class name to instantiate

        Example:
            (hbnb) create BaseModel

            93605ea4-0fc7-4593-a2d5-002348057cd1
        '''
        
        if HBNBCommand.handle_errors(args):
            return

        args =args.split(" ")
        obj = eval(args[0])()
        obj.save()
        print(obj.id)

    def help_create(self):
        doc = '''Creates a new instance of a class, saves it to JSON
        file, prints the instance id

        Args:
            args: class name to instantiate

        Example:
            (hbnb) create BaseModel

            93605ea4-0fc7-4593-a2d5-002348057cd1
        '''
        print(doc)

    def do_show(self, args):
        ''' 
        Prints the string representation of an instance
        based on the class name and id
        '''

        if HBNBCommand.handle_errors(args, command = 'show'):
            return

        args = args.split(" ")
        try:
            with open("file.json", 'r') as f_obj:
                data = json.load(f_obj)

            for k, v in data.items():
                key = k.split(".")
                
                if key[0] == args[0] and key[1] == args[1]:
                    obj = eval(args[0])(**v)
                    print(obj)
                    return
        except FileNotFoundError:
            pass

        print("** no instance found **")

    def help_show(self):
        doc = '''
        Prints the string representation of an instance
        based on the class name and id

        Args:
            model: Class model of instance to show
            id: id of instance
        '''

        print(doc)

    def do_destroy(self, args):
        '''
        Deletes an instance based on the class name and id
        Args:
            class_model: class model of instance to destroy
            id: id of instance to destroy

        '''

        if HBNBCommand.handle_errors(args, command = 'destroy'):
            return

        args = args.split(" ")
        with open("file.json", 'r') as f_obj:
            data = json.load(f_obj)

        for k, v in data.items():
            key = k.split(".")
            if key[0] == args[0] and key[1] == args[1]:
                del data[k]
                with open('file.json', 'w') as f_obj:
                    json.dump(data, f_obj)
                return

        print("** no instance found **")
        
    def help_destroy(self):
        doc = '''
        Deletes an instance based on the class name and id
        Args:
            class_model: class model of instance to destroy
            id: id of instance to destroy

        '''

        print(doc)

    def do_all(self, args):
        '''
        Prints all string representation of all instances based 
        or not on the class name.

        Args:
            class_model: class name to print
        '''

        if HBNBCommand.handle_errors(args):
            return

        args = args.split(" ")
        with open("file.json", 'r') as f_obj:
            data = json.load(f_obj)

        _all = []
        for k, v in data.items():
            key = k.split(".")
            if key[0] == args[0]:
                _all.append(str(eval(key[0])(**v)))

        print(_all)

    def help_all(self):
        pass

    def do_update(self, args):
        '''
        Updates an instance based on the class name and id 
        by adding or updating attribute (save the change into the JSON file).
        '''

        if HBNBCommand.handle_errors(args, command= 'update'):
            return
        
        args = args.split(" ")
        attr_name = args[2]
        attr_value = str(args[3])

        with open('file.json', 'r') as f_obj:
            data = json.load(f_obj)

        found = False
        for k, v in data.items():
            key = k.split(".")
            if key[0] == args[0] and key[1] == args[1]:
                found = True
                break
        if found:
            v[attr_name] = attr_value
            data[k] = v

            with open('file.json', 'w') as f_obj:
                json.dump(data, f_obj)
        else:
            print("** no instance found **")
    
    def help_update(self):
        doc = '''
        Updates an instance based on the class name and id 
        by adding or updating attribute (save the change into the JSON file).

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        '''

        print(doc)

        
if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()