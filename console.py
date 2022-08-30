#!/usr/bin/python3
'''Entry point of the command interpreter
'''
import cmd

import models
from models import BaseModel


class HBNBCommand(cmd.Cmd):
    '''Shell for database
    '''

    prompt = '(hbnb) '
    model_list = ['BaseModel']

    @classmethod
    def handle_errors(cls, args):
        if len(args) < 1:
            print("** class name missing **")
            return True

        elif args[0] not in HBNBCommand.model_list:
            print("** class doesn't exist **")
            return True
    
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

    def do_create(self, *args):
        '''Creates a new instance of a class, saves it to JSON
        file, prints the instance id

        Args:
            args: class name to instantiate

        Example:
            (hbnb) create BaseModel

            93605ea4-0fc7-4593-a2d5-002348057cd1
        '''
        if HBNBCommand.handle_errors(args):
            return

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

    def do_show(self, *args):
        pass

    def help_show(self):
        pass

    def do_destroy(self, *args):
        pass

    def help_destroy(self):
        pass

    def do_all(self, *args):
        pass

    def help_all(self):
        pass

    def do_update(self, *args):
        pass

    def help_update(self):
        pass

if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()