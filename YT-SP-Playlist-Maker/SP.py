import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

def create_playlist(songs_list, playlist_date):

    with open("user_data.json", "r") as user_data:
        data = json.load(user_data)
        CLIENT_ID = data["SpotifyData"]["CLIENT_ID"]
        CLIENT_SECRET = data["SpotifyData"]["CLIENT_SECRET"]

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt",
            username="John Propane xpp",
        )
    )
    user_id = sp.current_user()["id"]

    year = playlist_date.split("-")[0]
    song_uris = []
    for song in songs_list:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
            print(f"Pomyślnie dodano: {song}")
        except IndexError:
            print(f"{song} nie istnieje w Spotify.")

    playlist = sp.user_playlist_create(user=user_id, name=f"{playlist_date} Billboard 100", public=False)

    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
