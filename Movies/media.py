from webbrowser import open

class Movie():
    """Simple class used to store basic information about my favorite
       movies.

    Attributes:
        movie_title - String value giving the name of the movie
        movie_storyline - String value stating the basic premise of the
        movie poster_image - String value indicating the directory
        location of JPEG poster image of the movie
        trailer_youtube - String value denoting the YouTube location of
        the movie
    """

    # Class level variable storing the rating values for all movies
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(
        self, movie_title, movie_storyline,
        poster_image, trailer_youtube
    ):
        """Set the instance variables"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        open(self.trailer_youtube_url)
