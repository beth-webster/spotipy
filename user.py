from spotify_api_func import write_csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="##",
                                                           client_secret="##"))

url = 'https://open.spotify.com/album/4sgYpkIASM1jVlNC8Wp9oF?si=212HxJxaTA-ZcwhUZ3mspw'

file_name = 'output.csv'

write_csv(url, file_name, sp)
