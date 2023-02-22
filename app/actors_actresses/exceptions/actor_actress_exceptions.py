""" Actor/Actress Exceptions module """


class ActorActressNotFoundException(Exception):
    """Actor/Actress not found exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class ActorActressGenderException(Exception):
    """Actor/Actress gender not found exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
