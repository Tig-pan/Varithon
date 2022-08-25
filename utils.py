import random

from commands.command import Command

def get_list_literal_string(collection):
    """ Converts a list of tokens into a separate list of tokens that is the given collection of tokens
        represented as a list literal

        :param collection a list of tokens
        :returns a string representation of the given collection """
    if len(collection) == 0:
        return "[]"

    spacing = " " if random.random() < 0.7 else ""

    s = f"[{collection[0]}"
    for i in range(1, len(collection)):
        if random.random() < 0.01: # concat two list
            s += f"]{spacing}+{spacing}[{collection[i]}"
        else:
            s += f",{spacing}{collection[i]}"

    return s + "]"


def get_indentation(context):
    """ Gets a string representing the level of indentation for the current context

        :param context the line this command is contained within, this is a list containing
                strings and Command objects
        :return a string representing the level of indentation for the current context"""
    if str(context[0]).isspace():
        return context[0]
    return ""

def rand_v_name():
    """ Creates a random 20 character Varithon variable name. To be used for expanding commands.

        :return a random 20 character Varithon variable name. To be used for expanding commands."""

    v_name = ""
    for i in range(20):
        v_name += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_")

    return v_name
