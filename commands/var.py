import random

from commands.command import Command
from errors import *


class Var(Command):
    """ Var is a command that can be used to associate variable names within Varithon to
        variable names within the compiled Python that can have different variations.
        Each call to Var will re-associate the given variable name within Varithon to a new
        generated variable name in Python.

        Usage: var <variable-name> -<possible_name_1> -<possible_name_2> -<possible_name_3> ...
        Result: <generated-variable-name>

        Var will look at the surrounding context that the variable is used in, in order to
        generate possibilities for its name. Possible variable names can also be supplied as
        additional arguments, which will be added to the pool of possibilities for its name. """

    def __init__(self, args):
        if len(args) < 2:
            raise SyntaxException(f"Invalid 'var' command.")

        self.varithon_name = args[1]
        self.python_name = None

    def collapse(self, state):
        """ 'Collapses' the internal state of the command. I.e., forces it to decide exactly what it's
            behaviour will be. This should also completely reset the command, any previous collapses
            of this command should have no effect on future collapses.

            :param state a dictionary containing the current state of memory for this compilation,
                contains information such as variable name associations"""

        self.python_name = None
        while self.python_name is None or self.python_name in state:
            self.python_name = random.choice([self.varithon_name, "a_var", "variable", "my_var", "some_var", "new_var",
                                              random.choice("abcdefghijklmnopqrstuvwxyz"), "temp"])
        state[self.varithon_name] = self.python_name

    def get_pre_lines(self):
        """ Gets a list of lists, each interior list representing a single block of code that must be
            executed prior to accessing the result of this command. For most commands this will return
            an empty list.

            :return a list of lists, each interior list (containing only strings or Command objects)
                represents a single block of code that must be executed prior to accessing the result
                of this command"""

        return []

    def get_post_lines(self):
        """ Gets a list of lists, each interior list representing a single block of code that must be
            executed after accessing the result of this command. For most commands this will return
            an empty list.

            :return a list of lists, each interior list (containing only strings or Command objects)
                represents a single block of code that must be executed after to accessing the result
                of this command"""

        return []

    def get_result(self, state):
        """ Get the 'result' of this command. I.e., what string should replace this command in the
            resulting compiled file. Note that this is not the only way that a command can affect
            the result of the compilation, most notably they can affect the internal state of Varithon.

            :param state a dictionary containing the current state of memory for this compilation,
                contains information such as variable name associations
            :return a string representing the 'result' of this command"""

        return self.python_name
