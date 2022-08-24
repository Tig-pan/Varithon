from commands.command import Command
from errors import *


class Get(Command):
    """ Get is a command which can be used to access the generated Python variable name for a variable
        in Varithon. If multiple Var commands have used the same variable name, Get will return the name from
        the most recent Var command.

        Usage: get <Verithon-variable-name>
        Result: <corresponding-Python-variable-name>

        Get takes no additional parameters."""

    def __init__(self, args):
        if len(args) != 2:
            raise SyntaxException(f"Invalid 'get' command.")

        self.variable_name = args[1]

    def get_result(self, state):
        """ Get the 'result' of this command. I.e., what string should replace this command in the
            resulting compiled file. Note that this is not the only way that a command can affect
            the result of the compilation, most notably they can affect the internal state of Varithon.

            :param state a dictionary containing the current state of memory for this compilation,
                contains information such as variable name associations"""
        if self.variable_name not in state:
            raise SyntaxException(f"Variable name '{self.variable_name}' not found.")
        return state[self.variable_name]
