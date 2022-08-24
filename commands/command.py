class Command(object):
    def collapse(self, state):
        """ 'Collapses' the internal state of the command. I.e., forces it to decide exactly what it's
            behaviour will be. This should also completely reset the command, any previous collapses
            of this command should have no effect on future collapses.

            :param state a dictionary containing the current state of memory for this compilation,
                contains information such as variable name associations"""

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

        return ""


