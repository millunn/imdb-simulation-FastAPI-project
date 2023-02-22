""" MovieActorActress Exceptions module """


class MovieActorActressNotFoundException(Exception):
    """MovieActorActress pair not found exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
