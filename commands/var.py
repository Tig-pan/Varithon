import random

from commands.command import Command
from errors import *


class Var(Command):
    """ Var is a command that can be used to associate variable names within Varithon to
        variable names within the compiled Python that can have different variations.
        Each call to Var will re-associate the given variable name within Varithon to a newly
        generated variable name in Python.

        Usage:
            var <Varithon-variable-name> <possible-Python-name_1> -<possible-Python-name-2> -<possible-Python-name-3> ...

        Var will look at the surrounding context that the variable is used in, in order to
        generate possibilities for its name. Possible variable names can also be supplied as
        additional arguments, which will be added to the pool of possibilities for its name. """

    def __init__(self, tokens):
        super().__init__(tokens)

        if len(tokens) < 1:
            raise SyntaxException(f"Invalid 'var' command.")

        self.varithon_name = tokens.pop(0)

        if self.varithon_name[0].isdigit():
            raise SyntaxException(f"Invalid 'var' command, Varithon variable name cannot start with a digit.")

        self.extra_options = tokens  # first element was removed by the pop

    def collapse(self, varithon_state, python_state, context):
        """ 'Collapses' the internal state of the command. I.e., forces it to decide exactly what it's
            behaviour will be. This should also completely reset the command, any previous collapses
            of this command should have no effect on future collapses.

            :param varithon_state a dictionary containing the current state of varithon memory for this
                compilation, contains information such as variable name associations
            :param python_state a set containing python variable names in the current scope
            :param context the line this command is contained within, this is a list containing
                strings and Command objects """
        super().collapse(varithon_state, python_state, context)

        var_name = None
        while var_name is None or str(var_name) in python_state:
            if len(self.extra_options) > 0 and random.random() < 0.5:
                var_name = random.choice(self.extra_options)
            else:
                var_name = random.choice([self.varithon_name, "a_var", "variable", "my_var", "some_var", "new_var",
                                          random.choice("abcdefghijklmnopqrstuvwxyz"), "temp"])
        varithon_state[self.varithon_name] = var_name
        python_state.add(var_name)

        self.result = self.add_token_lines(var_name)
