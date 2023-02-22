""" TVShowRatingAndReview Exceptions module """


class TVShowRatingAndReviewNotFoundException(Exception):
    """TVShowRatingAndReview not found exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class TVShowRatingAndReviewGradeException(Exception):
    """TVShowRatingAndReview grade breach exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
