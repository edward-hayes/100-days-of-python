import requests

class Post:
    def __init__(self) -> None:
        url = "https://api.npoint.io/c790b4d5cab58020d391"
        response = requests.get(url)
        self.all_posts = response.json()

    