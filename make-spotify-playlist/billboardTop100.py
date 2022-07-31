import requests
import bs4

class billboardTop100():
    def __init__(self,date) -> None:
        self.get_soup(date)
        self.get_song_list()
        self.get_artist_list()

    def get_url(self,date):
        base_url = "https://www.billboard.com/charts/hot-100"
        return f"{base_url}/{date}/"

    def get_soup(self, date):
        url = self.get_url(date)
        response = requests.get(url)
        billboard_page_source = response.text
        self.soup = bs4.BeautifulSoup(billboard_page_source, "html.parser")

    def get_song_list(self):
        song_scrape = self.soup.select("h3.c-title.a-no-trucate")
        self.song_list = [song.getText().strip() for song in song_scrape]

    def get_artist_list(self):
        artist_scrape = self.soup.select("span.c-label.a-no-trucate")
        self.artist_list = [artist.getText().strip() for artist in artist_scrape]