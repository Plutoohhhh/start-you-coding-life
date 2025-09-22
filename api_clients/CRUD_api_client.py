import requests
from commom.config_reader import get_config

class CURDApiClient:

    def __init__(self):
        self.base_url = get_config("api","base_url2")
        self.session = requests.Session()

    def get_posts(self):
        return self.session.get(f"{self.base_url}/posts")
