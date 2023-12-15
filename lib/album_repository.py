from lib.album import *

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM albums')
        artists = []
        for row in rows:
            item = Album(row['id'], row["title"], row["release_year"], row["artist_id"])
            artists.append(item)
        return artists

    def find(self, id):
        rows = self._connection.execute('SELECT * FROM albums WHERE id = %s', [id])
        row = rows[0]
        return Album(row['id'], row["title"], row["release_year"], row["artist_id"])
    

    def create(self, album):
        rows = self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s) RETURNING id', [album.title, album.release_year, album.artist_id])
        row = rows[0]
        album.id = row['id']
        return album
    
    def delete(self, title):
        self._connection.execute('DELETE FROM albums WHERE title = %s', [title])
        return None