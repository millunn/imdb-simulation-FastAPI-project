""" TVShowActorActress Exceptions module """


class TVShowActorActressNotFoundException(Exception):
    """TVShowActorActress pair not found exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
