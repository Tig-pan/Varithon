import random

from commands.command import Command
from commands.var import Var
from commands.get import Get
from errors import *
from utils import *


class Collection(Command):
    """ Collection is a command which can be used initialize a collection. It can be used to initialize
        a list, including lists with deterministic contents, as well as lists with variable contents.
        Lists with variable contents can be generated using the results of other commands.

        Usage:
            collection <entry_1> <entry_2> <entry_3> ...
            collection -b <size> <element>

        Flags:
            -b      : for 'build', builds a new list from a given element repeated size times, if this element
                is a Command, it will be re-collapsed each time it is executed
        """

    def __init__(self, tokens):
        super().__init__(tokens)

        if len(tokens) < 1:
            raise SyntaxException(f"Invalid 'collection' command.")

        if tokens[0] == '-b':   # 'build' flag
            if len(tokens) != 3:
                raise SyntaxException(f"Invalid 'collection' command with -b flag.")

            self.flag = "b"
        else:
            self.flag = ""

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

        choice = random.random()

        if choice < 0.2:    # build list using append
            collection = self.get_collection(varithon_state, python_state, context)

            var_name = rand_v_name()

            self.pre_lines.append([get_indentation(context), Var([var_name]), " = []\n"])
            self.result = Get([var_name])

            for item in collection:
                self.post_lines.append([get_indentation(context), Get([var_name]), ".append(", item, ")\n"])
        else:
            self.result = get_list_literal_string(self.get_collection(varithon_state, python_state, context)) # TODO: fix by adding new command that converts its arguments to a list literal string

    def get_collection(self, varithon_state, python_state, context):
        """ Gets a list of tokens representing the output of this collection command.

            :param varithon_state a dictionary containing the current state of varithon memory for this
                compilation, contains information such as variable name associations
            :param python_state a set containing python variable names in the current scope
            :param context the line this command is contained within, this is a list containing
                strings and Command objects
            :return a list of tokens representing the output of this collection command"""
        collection = []

        if self.flag == "b":
            try:
                size = int(self.tokens[1])

                if size >= 1:
                    collection.append(self.add_token_lines(self.tokens[2]))

                for i in range(1, size):
                    collection.append(self.tokens[2])
            except ValueError as e:
                raise SyntaxException(f"Could not convert size parameter to integer.")
        else:
            for item in self.tokens:
                collection.append(self.add_token_lines(item))

        return collection
