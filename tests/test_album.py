from lib.album import *

def test_album_constructs():
    album = Album(1, "Test album title", 2019, 3)
    assert album.id == 1
    assert album.title == "Test album title"
    assert album.release_year == 2019
    assert album.artist_id == 3

def test_formatting():
    album = Album(1, "Test album title", 2019, 3)
    assert str(album) == "Album(1, Test album title, 2019, 3)"

def test_album_are_equal():
    album1 = Album(1, "Test album title", 2019, 3)
    album2 = Album(1, "Test album title", 2019, 3)
    assert album1 == album2