class UserInvalidPasswordException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserNotSuperUserException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
