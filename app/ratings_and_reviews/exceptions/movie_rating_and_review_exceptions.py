""" MovieRatingAndReview Exceptions module """


class MovieRatingAndReviewNotFoundException(Exception):
    """MovieRatingAndReview not found exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code


class MovieRatingAndReviewGradeException(Exception):
    """MovieRatingAndReview grade breach exception"""

    def __init__(self, message, code):
        self.message = message
        self.code = code
