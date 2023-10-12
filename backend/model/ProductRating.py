class ProductRating:
    def __init__(self, stars_rating, comment_rating, rating_date, rating_update=None):
        self._stars_rating = stars_rating
        self._comment_rating = comment_rating
        self._rating_date = rating_date
        self._rating_update = rating_update

