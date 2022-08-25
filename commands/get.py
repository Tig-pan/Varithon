from commands.command import Command
from errors import *


class Get(Command):
    """ Get is a command which can be used to access the generated Python variable name for a variable
        in Varithon. If multiple Var commands have used the same variable name, Get will return the name from
        the most recent Var command.

        Usage:
            get <Varithon-variable-name>

        Get takes no additional parameters."""

    def __init__(self, tokens):
        super().__init__(tokens)

        if len(tokens) != 1:
            raise SyntaxException(f"Invalid 'get' command.")

        self.varithon_name = tokens[0]

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

        if self.varithon_name not in varithon_state:
            raise SyntaxException(f"Varithon variable '{self.varithon_name}' not found.")

        self.result += self.add_token_lines(varithon_state[self.varithon_name])
