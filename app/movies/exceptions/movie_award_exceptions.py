""" MovieAward Exceptions module """


class MovieAwardNotFoundException(Exception):
    """MovieAward pair not found exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
