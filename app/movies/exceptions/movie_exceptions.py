""" Movie Exceptions module """


class MovieNotFoundException(Exception):
    """Movie not found exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class MovieIntegrityException(Exception):
    """Movie integrity exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class MovieReleaseYearDigitException(Exception):
    """Release year not all digits exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class MovieReleaseYearLenghtException(Exception):
    """Release year lenght breach exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class MovieDurationException(Exception):
    """Movie duration breach exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
