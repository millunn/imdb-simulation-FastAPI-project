""" Actor/Actress-Award-Movie Exceptions module """


class ActorActressAwardMovieNotFoundException(Exception):
    """Pair of Actor/Actress-Award-Movie not found exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
