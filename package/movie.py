from searchMovie import searchMovieRequest
from getRating import ratingRequest

class movie:
    def __init__(self,name):
        self.name = name
        self.id = searchMovieRequest.get_movie_id(name)
        self.rating = ratingRequest.get_rating(self.id)

    def __str__(self):

        response = "The movie "+self.name+" has an average rating of "+str(self.rating)

        return response