import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOTIPY_CLIENT_ID = ""
SPOTIPY_CLIENT_SECRET = ""
SPOTIPY_REDIRECT_URI= ""

SCOPE = "playlist-modify-private"

auth_manager = SpotifyOAuth(
    scope=SCOPE,
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI
)

class spotipyPlaylist(spotipy.Spotify):
    def __init__(self,date) -> None:
        super().__init__(auth_manager=auth_manager)
        self.current_id = self.current_user()["id"]
        self.no_results = []
        self.year = date.split("-")[0]

    def get_song_uri(self,artist,song):
        query = f"track:{song}+artist:{artist}+year:{self.year}"
        response = self.search(
            query,
            limit = 1,
            type = "track"
        )
        try:
            uri = response["tracks"]["items"][0]["uri"]
            return uri
        except IndexError:
            self.no_results.append((artist,song))

    def create_playlist(self, name):
        response = self.user_playlist_create(
            user = self.current_id,
            name = name,
            public = False,
            description = ""
        )
        self.playlist_id = response["uri"]

    def add_tracks(self, list_of_tracks):
        self.playlist_add_items(
            playlist_id= self.playlist_id,
            items = list_of_tracks
        )