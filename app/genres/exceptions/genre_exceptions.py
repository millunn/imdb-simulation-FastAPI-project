""" Genre Exceptions module """


class GenreNotFoundException(Exception):
    """Genre not found exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
