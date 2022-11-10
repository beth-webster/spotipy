import csv
from helper_functions import id_from_url

def write_csv(url, file_name, sp):

    url_type = id_from_url(url)[0]
    id = id_from_url(url)[1]

    if url_type == 'album':
        results_album = sp.album(id, market = 'GB')

        with open (file_name, 'w', newline = '') as f:
            writer = csv.writer(f, dialect='excel')
            
            writer.writerow(('Bundle UPC','Bundle Title', 'Bundle Artists', 'Bundle Release Date', 'Label'))
            bundle_upc = results_album['external_ids'].get('upc')
            label = results_album.get('label')
            bundle_rel_date = results_album.get('release_date')
            bundle_title = results_album.get('name')
            bundle_artists_list = []
            for artist in results_album['artists']:
                for key in artist:
                    if key == 'name':
                        bundle_artists_list.append((artist[key]))
            bundle_artists = '/'.join([str(artist) for artist in bundle_artists_list])
            bundle_rows = (bundle_upc, bundle_title, bundle_artists, bundle_rel_date, label)
            writer.writerow(bundle_rows)

            writer.writerow(('ISRC','Track Title', 'Track Artists', 'Track Number'))
            for track in results_album['tracks']['items']:
                track_title = track.get('name')
                track_number = track.get('track_number')
                track_id = track.get('id')
                results_album_tracks = sp.track(track_id, market = 'GB')
                isrc = results_album_tracks['external_ids'].get('isrc')
                track_artist_list = []
                for artist in track['artists']:
                    for key in artist:
                        if key == 'name':
                            track_artist_list.append((artist[key]))  
                track_artist_names = '/'.join([str(artist) for artist in track_artist_list])        
                track_rows = (isrc, track_title, track_artist_names, track_number)
                writer.writerow(track_rows)



    elif url_type == 'playlist':
        results = sp.playlist(id, market = 'GB')

        with open (file_name, 'w', newline = '') as f:
            writer = csv.writer(f, dialect='excel')
            writer.writerow(('ISRC','Title', 'Artists', 'Release Date'))
            for track in results['tracks']['items']:
                artist_list = []
                if track['track'] is not None:
                    title = track['track'].get('name')
                    if track['track']['external_ids'] is not None:
                        isrc = track['track']['external_ids'].get('isrc')
                    else:
                        isrc = '-'                    
                    if track['track']['album'] is not None:
                        rel_date = track['track']['album'].get('release_date')
                    else:
                        rel_date = '-'
                    if track['track']['artists'] is not None:
                        for artist in track['track']['artists']:
                            for key in artist:
                                if key == 'name':
                                    artist_list.append((artist[key]))
                    else:
                        artist_list.append(('-'))
                else:
                    title = '-'
                artist_names = '/'.join([str(artist) for artist in artist_list])
                rows = (isrc, title, artist_names, rel_date)
                writer.writerow(rows)

    elif url_type == 'track':
        results = sp.track(id, market = 'GB')

        with open (file_name, 'w', newline = '') as f:
            writer = csv.writer(f, dialect='excel')
            writer.writerow(('ISRC','Title', 'Artists'))
            isrc = results['external_ids'].get('isrc')
            artists_list = []
            for artist in results['artists']:
                for key in artist:
                    if key == 'name':
                        artists_list.append((artist[key]))
            artist_names = '/'.join([str(artist) for artist in artists_list])
            title = results.get('name')
            rows = (isrc, title, artist_names)
            writer.writerow(rows)

    else:
        print("invalid URL")
