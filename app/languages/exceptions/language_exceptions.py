""" Language Exceptions module """


class LanguageNotFoundException(Exception):
    """Language not found exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
