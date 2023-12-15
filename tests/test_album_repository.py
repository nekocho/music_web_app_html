from lib.album_repository import *
from lib.album import *


def test_get_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    album = repository.all()

    assert album == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1)
    ]

def test_find_single_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(1)
    assert album == Album(1, "Doolittle", 1989, 1)

#Test create function

def test_create_single_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(3,'Voulez-Vous', 1979, 2))

    result = repository.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Voulez-Vous', 1979, 2)
    ]

#Test delete function

def test_delete_single_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.delete('Doolittle')

    result = repository.all()
    assert result == [
        Album(2, 'Surfer Rosa', 1988, 1)
    ]    