# github_request.py
import requests
import json 
from keyvault.keyvault import keyvault

class ratingRequest:
    _base_url = keyvault.get_url_imdb()
    _api_key = keyvault.get_key_imdb()

    @classmethod
    def get_rating(cls,id):
        """
        param cls: the class itself
        param id: the id of the movie

        return the rating of the movie
        """

        result = requests.get(cls._base_url+"/Ratings/"+cls._api_key+"/"+id).content

        result = json.loads(result)

        # we have the rating of different sources so we are going to take the mean of all of them
        # the exception is about the rating from metacritic and rottenTomatoes wich is between 0 and 100, not between 0 and 10

        # store in a list the ratings that are not 0

        rating_list = []

        if result["imDb"] == "":
            imDb = 0
        else :
            imDb = float(result["imDb"])
            rating_list.append(imDb)

        if result["metacritic"] == "":
            metacritic = 0
        else :
            metacritic = float(result["metacritic"])/10
            rating_list.append(metacritic)

        if result['theMovieDb'] == "":
            theMovieDb = 0
        else:
            theMovieDb = float(result["theMovieDb"])
            rating_list.append(theMovieDb)

        if result["rottenTomatoes"] == "":
            rottenTomatoes = 0
        else:
            rottenTomatoes = float(result["rottenTomatoes"])/10
            rating_list.append(rottenTomatoes)

        if result["filmAffinity"] == "":
            filmAffinity = 0
        else:
            filmAffinity = float(result["filmAffinity"])
            rating_list.append(filmAffinity)

        print("imdbrating: "+str(imDb))
        print("metacritic: "+str(metacritic))
        print("theMovieDb: "+str(theMovieDb))
        print("rottenTomatoes: "+str(rottenTomatoes))
        print("filmAffinity: "+str(filmAffinity))

        # we compute the mean by dividing the sum of all the ratings by the number of ratings

        mean = sum(rating_list)/len(rating_list)

        return mean
        