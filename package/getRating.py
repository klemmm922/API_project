# github_request.py
import requests
import json 
from keyvault import keyvault

class ratingRequest:
    _base_url = keyvault.get_url_imdb()
    _api_key = keyvault.get_key_imdb()
        
    @classmethod
    def get_rating(cls,id):

        result = requests.get(cls._base_url+"/Ratings/"+cls._api_key+"/"+id).content

        result = json.loads(result)

        # we have the rating of different sources so we are going to take the mean of all of them
        # the exception is about the rating from metacritic and rottenTomatoes wich is between 0 and 100, not between 0 and 10

        imDb = float (result["imDb"])
        metacritic = float (result["metacritic"])/10
        theMovieDb = float (result["theMovieDb"])
        rottenTomatoes = float (result["rottenTomatoes"])/10
        filmAffinity = float (result["filmAffinity"])

        mean = (imDb+metacritic+theMovieDb+rottenTomatoes+filmAffinity)/5

        return mean
        