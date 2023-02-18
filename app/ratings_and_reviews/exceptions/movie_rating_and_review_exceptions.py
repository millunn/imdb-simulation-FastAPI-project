class MovieRatingAndReviewNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class MovieRatingAndReviewGradeException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
