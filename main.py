# Varithon: Variation/Python
# A language that cannot be executed on its own, but can be compiled to python.
# In addition, when compiled, it is not compiled to a single output python file.
# Instead, it is compiled to many variations, all with the same behaviour.
# The main purpose of this language is to use it to build large, customizable
# datasets of python code very quickly. The file extension for Varithon is .vy

# By: Timothy Letkeman

from commands.command import Command
from commands.var import Var
from commands.get import Get
from errors import *


COMMAND_START = "~~["
COMMAND_END = "]~~"


def parse_command(string):
    """ Parses and returns a Command object given a string representing
        that command. Ex. The full varithon statement ~~[var-data a]~~ would result
        in calling this function with the argument of "var-data a".

        :param string A string representing the body of a varithon statement
            If this string is unable to be converted, this function will throw
            a VarithonSyntaxException exception
        :return a Command object, possibly a SyntaxException is thrown
            if the string is unable to be parsed """

    args = string.strip().lower().split(" ")

    match args[0]:
        case "var":
            return Var(args)
        case "get":
            return Get(args)
        case "collection":
            return "TODO"
        case "high":
            return "TODO"
        case "low":
            return "TODO"


def parse_line(line):
    """ Parses a single line of a .vy file into a list, each entry in the list
        either being a string, or a Command object. This function is called recursively to

        :param line: the line to parse as a string
        :return: A list of strings and Command objects, possibly a SyntaxException
            is thrown if the file is unable to be parsed """

    if len(line) == 0:
        return []

    if COMMAND_START in line:
        command_start_index = line.index(COMMAND_START)

        before_start, after_start = line[:command_start_index], line[command_start_index + len(COMMAND_START):]

        if COMMAND_END in after_start:
            command_end_index = after_start.index(COMMAND_END)

            command, after_end = after_start[:command_end_index], after_start[command_end_index + len(COMMAND_END):]

            line_list = [parse_command(command)]
            if len(before_start) > 0:       # prepend before the start of the command, as long as it isn't empty
                line_list.insert(0, before_start)
            line_list.extend(parse_line(after_end))  # recursive to get all commands in the line

            return line_list
        else:
            raise SyntaxException(f"'{COMMAND_START}' found, but no matching '{COMMAND_END}'")
    else:
        return [line]


def parse_varithon_file(filepath):
    """ Parses the given .vy file into a list of lists, each interior list containing only
    strings, or Command objects.

    :param filepath: a path to the .vy file to parse
    :return: A list of strings and Command objects, possibly a SyntaxException
        is thrown if the file is unable to be parsed """

    parsed_line_list = []

    with open(filepath, "r") as f:
        line_number = 1
        for line in f:
            try:
                parsed_line_list.append(parse_line(line))
            except SyntaxException as e:
                raise VarithonSyntaxException(filepath, line_number, e.message)
            line_number += 1

    return parsed_line_list


def compile_varithon_file(destination_filepath, parsed_line_list):
    """ Compiles a parsed list of lines into a single python file. Each compilation is random and independent
        of any previous compilation.

        :param destination_filepath a string representing a filepath for the destination compiled file
        :param parsed_line_list a list of lists, each interior list representing a single line of the Varithon file """
    state = {}

    # first collapse every command in sequence
    for line in parsed_line_list:
        for item in line:
            if isinstance(item, Command):
                item.collapse(state)

    # then open the file and write each command to it
    with open(destination_filepath, "w") as f:
        for line in parsed_line_list:
            for item in line:
                if isinstance(item, Command):
                    f.write(item.get_result(state))
                else:               # string
                    f.write(item)


if __name__ == "__main__":
    FILE_NAME = "hello"
    FILE_EXTENSION = ".txt"
    COMPILATION_COUNT = 5

    parsed = parse_varithon_file(FILE_NAME + FILE_EXTENSION)

    for i in range(COMPILATION_COUNT):
        compile_varithon_file("compiled/" + FILE_NAME + "_" + str(i) + FILE_EXTENSION, parsed)


