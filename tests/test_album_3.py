from lib.album_3 import *

"""
Construct an album with id, title, release year,
and artist_id
"""

def test_construction_of_album_properties():
    album = Album(1, "Doolittle", 1989, 1)
    assert album.id == 1
    assert album.title == "Doolittle"
    assert album.release_year == 1989
    assert album.artist_id == 1


"""
Returning album properties in a nice sentence
"""

def test_albums_format_nicely():
    album = Album(1,'Doolittle', 1989, 1)
    assert str(album) == "Album(1, Doolittle, 1989, 1)"


"""
Test comparing albums
"""

def test_comparing_albums():
    album1 = Album(1,'Doolittle', 1989, 1)
    album2 = Album(1,'Doolittle', 1989, 1)
    assert album1 == album2