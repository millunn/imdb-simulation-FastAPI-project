class TVShowRatingAndReviewNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class TVShowRatingAndReviewGradeException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
