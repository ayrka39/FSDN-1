import webbrowser


class Movie():
    """define the Movie class"""
    def __init__(self, movie_title, movie_stroyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_stroyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)