import random

from commands.command import Command
from errors import *


class Rand(Command):
    """ Rand is a function that allows you to generate random values within some range. It requires a
        flag that determines the type of the outputted value.

        Usage:
            rand -i <lower-inclusive> <upper-inclusive>
            rand -f <lower-inclusive> <upper-inclusive>

        Flags:
            -i      : for 'integer', will output an integer between lower-inclusive and upper-exclusive
            -f      : for 'float', will output a float between lower-inclusive and upper-exclusive
        """

    def __init__(self, tokens):
        super().__init__(tokens)

        if len(tokens) != 3:
            raise SyntaxException(f"Invalid 'rand' command.")

        match tokens[0]:
            case "-i":
                self.flag = "i"
            case "-f":
                self.flag = "f"
            case _:
                raise SyntaxException(f"Invalid 'rand' command, invalid flag.")

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

        try:
            match self.flag:
                case "i":
                    self.result = self.add_token_lines(random.randint(int(self.tokens[1]), int(self.tokens[2])))
                case "f":
                    lower = float(self.tokens[1])
                    upper = float(self.tokens[2])

                    self.result = self.add_token_lines(lower + (upper - lower) * random.random())
        except ValueError as e:
            raise SyntaxException("Invalid bounds, could not convert.")