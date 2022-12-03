import requests
import json
from keyvault.keyvault import keyvault

class boxOfficeAllTimeRequest:
    
    _base_url = keyvault.get_url_imdb()
    _api_key = keyvault.get_key_imdb()

    @classmethod
    def get_box_office(cls):
        """
        param cls: the class itself

        return the list of the movies in the box office of all time
        """
        
        list = [] 

        result = requests.get(cls._base_url+"/BoxOfficeAllTime/"+cls._api_key).content
        print("result : "+str(result))

        json1 = json.loads(result).get("items")

        for i in json1:
            title = i.get("title")
            list.append(title)
        
        print(list)

        return list 