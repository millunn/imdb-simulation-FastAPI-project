""" Award Exceptions module """


class AwardNotFoundException(Exception):
    """Award not found exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
