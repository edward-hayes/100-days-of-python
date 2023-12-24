import requests

BASE_URL = "https://api.themoviedb.org/3"
API_KEY = "2055dae4c1ffeced8317595a3794ace4"

class Imdb():
    def __init__(self) -> None:
        pass
    
    def get_movies(self, query):
        endpoint = "/search/movie"
        params = {
            "api_key": API_KEY,
            "query": query,

        }
        response = requests.get(f"{BASE_URL}{endpoint}", params=params)
        data = response.json()
        self.first_six_results = data['results'][:6]

# imdb = Imdb()
# imdb.get_movies("alien")
# print(imdb.first_six_results)