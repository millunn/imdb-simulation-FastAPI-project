class MovieNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class MovieIntegrityException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class MovieReleaseYearDigitException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class MovieReleaseYearLenghtException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
