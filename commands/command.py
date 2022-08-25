class Command(object):
    def __init__(self, tokens):
        self.__pre_lines = []
        self.result = ""
        self.__post_lines = []

        self.tokens = tokens

    def collapse(self, varithon_state, python_state, context):
        """ 'Collapses' the internal state of the command. I.e., forces it to decide exactly what it's
            behaviour will be. This should also completely reset the command, any previous collapses
            of this command should have no effect on future collapses.

            :param varithon_state a dictionary containing the current state of varithon memory for this
                compilation, contains information such as variable name associations
            :param python_state a set containing python variable names in the current scope
            :param context the line this command is contained within, this is a list containing
                strings and Command objects """
        self.clear()

        for token in self.tokens:
            if isinstance(token, Command):
                token.collapse(varithon_state, python_state, context)

    def get_pre_lines(self):
        """ Gets a list of lists, each interior list representing a single block of code that must be
            executed prior to accessing the result of this command. For most commands this will return
            an empty list.

            :return a list of lists, each interior list (containing only strings or Command objects)
                represents a single block of code that must be executed prior to accessing the result
                of this command"""

        return self.__pre_lines

    def get_post_lines(self):
        """ Gets a list of lists, each interior list representing a single block of code that must be
            executed after accessing the result of this command. For most commands this will return
            an empty list.

            :return a list of lists, each interior list (containing only strings or Command objects)
                represents a single block of code that must be executed after to accessing the result
                of this command"""

        return self.__post_lines

    def __str__(self):
        """ Get the 'result' of this command as a string. I.e., what string should replace this command in the
            resulting compiled file.

            :return a string representing the 'result' of this command"""

        return self.result

    def clear(self):
        """ Clears the internal memory for these commands pre-lines, result, and post-lines. """

        self.__pre_lines = []
        self.result = ""
        self.__post_lines = []

    def add_token_lines(self, token):
        """ Adds the given token's pre-lines and post-lines to these Commands pre-lines and post-lines,
            merely returns the token if it is just a string and not a Command object

            :param token the token to add to the result of this command,
                can be a string or Command object
            :return a string representation of the token"""

        if isinstance(token, Command):
            self.__pre_lines.extend(token.get_pre_lines())
            self.__post_lines.extend(token.get_post_lines())

        return str(token)

