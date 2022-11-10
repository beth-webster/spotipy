import re

def id_from_url(url):
    try:
        url_regex = re.search(r"^https?:\/\/(?:open\.)?spotify.com\/(user|episode|playlist|track|album)\/(?:spotify\/playlist\/)?(\w*)", url)

        return url_regex.group(1), url_regex.group(2)

    except AttributeError:
        return 'invalid URL'

def get_artists(results):
    artist_list = []
    for artist in results['artists']:
        for key in artist:
                if key == 'name':
                    artist_list.append((artist[key]))
    artists = '/'.join([str(artist) for artist in artist_list])
    return artists
