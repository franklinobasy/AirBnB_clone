#!/usr/bin/python3
'''Entry point of the command interpreter
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''Shell for database
    '''

    prompt = '(hbnb) '
    
    def do_quit(self, stdin):
        pass

    def do_EOF(self, stdin):
        pass