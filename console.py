#!/usr/bin/python3
'''Entry point of the command interpreter
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''Shell for database
    '''

    prompt = '(hbnb) '
    
    def do_quit(self, stdin):
        ''' command to quit the interpreter'''

        return True

    def help_quit(self):
        doc = '''
        This command quits the interpreter
        Usage:
            (hbnb) quit
        '''

        print(doc)

    def do_EOF(self, stdin):
        '''Handles end of line'''

        return True

    def help_EOF(self):
        doc = '''
        This command handles EOF
        Usage:
            (hnbn) <Ctrl-d>
        '''

        print(doc)

if __name__ == '__main__':
    interpreter = HBNBCommand()
    interpreter.cmdloop()