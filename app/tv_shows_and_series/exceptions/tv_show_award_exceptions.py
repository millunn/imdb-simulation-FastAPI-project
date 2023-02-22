""" TVShowAward Exceptions module """


class TVShowAwardNotFoundException(Exception):
    """TVShowAward pair not found exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
