class Command(object):
    def get_result(self, state):
        """ Get the 'result' of this command. I.e., what string should replace this command in the
            resulting compiled file. Note that this is not the only way that a command can affect
            the result of the compilation, most notably they can affect the internal state of Varithon.

            :param state a dictionary containing the current state of memory for this compilation,
                contains information such as variable name associations"""
        pass


