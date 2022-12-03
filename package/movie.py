from package.searchMovie.searchMovie import searchMovieRequest
from package.getRating.getRating import ratingRequest

class movie:

    """
    class movie is a class that represent a movie
    param name: the name of the movie
    param id: the id of the movie
    param rating: the rating of the movie
    """

    def __init__(self,name):
        self.name = name
        self.id = searchMovieRequest.get_movie_id(name)
        self.rating = ratingRequest.get_rating(self.id)

    def __str__(self):

        response = "The movie "+self.name+" has an average rating of "+str(self.rating)

        return response