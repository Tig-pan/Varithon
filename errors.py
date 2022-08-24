class SyntaxException(Exception):
    def __init__(self, message):
        """ Constructs a SyntaxException given an error message.

            :param message a string giving details about this exception """

        self.message = message

    def __str__(self):
        return f"{self.message}"


class VarithonSyntaxException(SyntaxException):
    def __init__(self, message, filepath, line):
        """ Constructs a VarithonSyntaxException given a filepath, line, and
            error message.

            :param filepath a string representing a path to the file on which the
                syntax exception was found
            :param line an integer representing the line number the syntax error
                was found on
            :param message a string giving details about this exception """

        super().__init__(message)

        self.filepath = filepath
        self.line = line

    def __str__(self):
        return f"Syntax Error in [{self.filepath}] on line {self.line}: {self.message}"
