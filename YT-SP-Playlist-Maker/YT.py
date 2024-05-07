import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import googleapiclient.http
from urllib.request import urlopen

def create_playlist(songs_list, playlist_date):
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_327981699886-48a0f0534esq870a8811o62em5116alr.apps.googleusercontent.com.json"

    with open("user_data.json", "r") as user_data:
        data = json.load(user_data)
        DEV_KEY = data["YouTubeData"]["API_KEY"]

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    creds = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=creds, developerKey=DEV_KEY)

    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": f"{playlist_date} Billboard 100",
                "description": "Przykładowa playlista stworzona przez API",
                "tags": [
                    "sample playlist",
                    "API call"
                ],
                "defaultLanguage": "en"
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    )
    response_data = request.execute()

    for song in songs_list:
        song_results = youtube.search().list(q=song, part='snippet', type='video')
        result = song_results.to_json()
        dic = json.loads(result)
        video_info = dic['uri']
        try:
            res = urlopen(video_info)
            data_vide_json = json.loads(res.read())
        except:
            print("Nie udało się pobrać danych")
        else:
            video_id = data_vide_json["items"][0]['id']['videoId']
            request = youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": response_data["id"],
                        "position": 0,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": video_id
                        }
                    }
                }
            )
            try:
                response = request.execute()
                print(f"Pomyślnie dodano: {song}")
            except:
                print(f"Nie udało się dodać: {song}")
