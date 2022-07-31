from billboardTop100 import billboardTop100
from spotifyApi import spotipyPlaylist

# Enter Desired Week (YYYY-MM-DD)
DATE = "1988-09-07"

billboard_top_100 = billboardTop100(DATE)
playlist = spotipyPlaylist(DATE)

#scrape song names & artist names, and use that to search for corresponding uris in spotify
track_tuples = zip(billboard_top_100.artist_list,billboard_top_100.song_list)
track_uris = [playlist.get_song_uri(artist,song) for artist,song in track_tuples if playlist.get_song_uri(artist,song) is not None]

# create a new playlist, and add songs to it
playlist.create_playlist(name=f"Billboard Top 100 - Week of {DATE}")
response = playlist.add_tracks(track_uris)

# let the user know if there were any errors
no_results = [f"{artist} - {song}" for artist,song in playlist.no_results]
if no_results:
    print(f"Was not able to locate the follwing songs:\n{no_results}")

