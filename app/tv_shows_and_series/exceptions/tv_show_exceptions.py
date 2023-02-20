class TVShowNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TVShowReleaseYearDigitException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TVShowReleaseYearLenghtException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
