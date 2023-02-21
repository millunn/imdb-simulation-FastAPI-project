class ActorActressNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ActorActressGenderException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
