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

        self.variable_name = args[1]

    def get_result(self, state):
        """ Get the 'result' of this command. I.e., what string should replace this command in the
            resulting compiled file. Note that this is not the only way that a command can affect
            the result of the compilation, most notably they can affect the internal state of Varithon.

            :param state a dictionary containing the current state of memory for this compilation,
                contains information such as variable name associations"""
        name = None
        while name is None or name in state:
            name = random.choice([self.variable_name, "a_var", "variable", "my_var", "some_var", "new_var", random.choice("abcdefghijklmnopqrstuvwxyz"), "temp"])

        state[self.variable_name] = name
        return name
