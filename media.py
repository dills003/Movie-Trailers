import webbrowser

class Movie():
    """This class takes a title, poster, and trailer of a movie.
   It is used to seed fresh_tomatoes to create a html file that you can run in a web browser"""
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
    
    #show_trailer is used to show the movie's youtube trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
