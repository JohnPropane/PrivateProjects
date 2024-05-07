from bs4 import BeautifulSoup
import requests
import SP
import YT
import re
from datetime import datetime, date, timedelta

URL = "https://www.billboard.com/charts/hot-100/"
start_date = datetime(1900, 1, 6)
end_date = datetime.today() - timedelta(days=datetime.today().weekday()+2)
playlist_date = input(f"Witaj w Spotify/YouTube playlistmaker\n"
                      "Aby rozpocząć podaj date z której chciałbyś zimportować piosenki\n"
                      "\t1. Format daty: YYYY-MM-DD\n"
                      f"\t2. Data w przedziale od {start_date} do {end_date}\n"
                      f"Wpisz datę: ")
date_pattern = "^\d{4}-\d{2}-\d{2}$"
playlist_date_info = playlist_date.split("-")
is_on = True
while is_on:
    if not re.match(date_pattern, playlist_date):
        print("Niepoprawny format daty! Proszę używać YYYY-MM-DD!")
        playlist_date = input("Podaj date z której chciałyś zimportować piosenki? YYYY-MM-DD: ")
        playlist_date_info = playlist_date.split("-")
    elif not start_date <= datetime(int(playlist_date_info[0]), int(playlist_date_info[1]), int(playlist_date_info[2])) <= end_date:
        print(f"Niepoprawna data! Proszę wybrać datę z przedziału od {start_date} do {end_date}")
        playlist_date = input("Podaj date z której chciałyś zimportować piosenki? YYYY-MM-DD: ")
        playlist_date_info = playlist_date.split("-")
    else:
        is_on = False

respond = requests.get(URL+playlist_date)
soup = BeautifulSoup(respond.text, "html.parser")
web_scrap = soup.find_all(name="div", class_="o-chart-results-list-row-container")
songs_list = []
for song in web_scrap:
    data = song.find(name="h3", id="title-of-a-story").get_text().strip()
    songs_list.append(data)

print("Wybierz platforme na której ma zostać utworzona playlist'a.")
print("1. Spotify")
print("2. YouTube")

choice = input()

if choice == "1" or choice.lower() == "spotify":
    SP.create_playlist(songs_list, playlist_date)
elif choice == "2" or choice.lower() == "youtube":
    YT.create_playlist(songs_list, playlist_date)
else:
    print("Podano niepoprawne dane!")



