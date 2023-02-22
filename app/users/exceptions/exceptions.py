""" Award Exceptions module """


class UserInvalidPasswordException(Exception):
    """Invalid Password exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserNotSuperUserException(Exception):
    """User not SuperUser exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserNotFoundException(Exception):
    """User not found exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
