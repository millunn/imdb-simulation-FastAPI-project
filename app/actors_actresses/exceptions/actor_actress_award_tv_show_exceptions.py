""" Actor/Actress-Award-TvShow Exceptions module """


class ActorActressAwardTVShowNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
