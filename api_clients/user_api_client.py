import requests
from commom.config_reader import get_config

class UserApiClient:
#####
    def __init__(self):
        self.base_url = get_config("api","base_url")

    def get_list_of_users(self,page_number=2):
        url = f"{self.base_url}/api/users"
        params = {'page':page_number}

        response = requests.get(url,params=params)
        return response

    def get_info(self):
        url = f"{self.base_url}/"
        