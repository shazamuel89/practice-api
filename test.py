import musicbrainzngs as mbz
import pprint

mbz.set_useragent("MyPracticeAPI", 1.0, contact="shazamuel89@gmail.com")
autechre = mbz.search_artists(query='autechre')['artist-list'][0];

limit = 100
offset = 0
release_list = []

while True:
    response = mbz.browse_release_groups(artist=autechre['id'], limit=limit, offset=offset)
    releases = response['release-group-list']
    release_list.extend(releases)
    if offset + limit >= response['release-group-count']:
        break
    offset += limit

clean_release_list = []
for release in release_list:
    clean_release_list.append({
        'title': release.get('title'),
        'id': release.get('id')
    })

pprint.pprint(clean_release_list)