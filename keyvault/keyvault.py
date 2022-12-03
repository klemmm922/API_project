# use to store the key for the API

"""
This file is used to store the key for the API
"""

class keyvault:
    _key_imdb = "k_mznd1sb2"
    _url_imdb = "https://imdb-api.com/API"


    @classmethod
    def get_key_imdb(cls):
        return cls._key_imdb

    @classmethod
    def get_url_imdb(cls):
        return cls._url_imdb
