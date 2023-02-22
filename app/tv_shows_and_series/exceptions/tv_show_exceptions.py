""" TVShow Exceptions module """


class TVShowNotFoundException(Exception):
    """TVShow not found exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class TVShowReleaseYearDigitException(Exception):
    """Release year not all digits exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class TVShowReleaseYearLenghtException(Exception):
    """Release year lenght breach exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class TVShowEpisodeDurationException(Exception):
    """Episode duration breach exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
