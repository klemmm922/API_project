import requests
import json
from keyvault import keyvault


class boxOfficeAllTimeRequest:
    _base_url = keyvault.get_url_imdb()
    _api_key = keyvault.get_key_imdb()

    @classmethod
    def get_box_office(cls):

        list = [] 

        result = requests.get(cls._base_url+"/BoxOfficeAllTime/"+cls._api_key).content

        json1 = json.loads(result).get("items")

        for i in json1:
            title = i.get("title")
            list.append(title)

        return list 