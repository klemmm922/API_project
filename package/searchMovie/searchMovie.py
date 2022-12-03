import requests 
import json
from keyvault.keyvault import keyvault


class searchMovieRequest:
    _base_url = keyvault.get_url_imdb()
    _api_key = keyvault.get_key_imdb()
        
    @classmethod
    def get_movie_id(cls,name):

        """
        param cls: the class itself
        param name: the name of the movie
    
        return the id of the movie
        """

        result = requests.get(cls._base_url+"/SearchMovie/"+cls._api_key+"/"+name).content
        # but we don't want to return all the content of the request, we want to return only the id of the movie
        # so we need to parse the result

        result = json.loads(result)

        # now we have a dictionary with the result
        # we can access the id of the movie with the key "id"

        # we admit that we are going to return only the first one

        print(result["results"]["id"])

        val = result["results"][0]["id"]

        return val
