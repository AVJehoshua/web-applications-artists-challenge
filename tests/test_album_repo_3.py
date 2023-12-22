from lib.album_repo_3 import *
from lib.album_3 import *
"""
When we call AlbumRepository(all), we get a list of all albums
in the repository
"""

def test_functionality_of_returning_all_albums(db_connection):
    db_connection.seed("seeds/music_web.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.all()

    assert albums == [
        Album(1,'Doolittle', 1989, 1),
        Album(2,'Surfer Rosa', 1988, 1),
        Album(3,'Waterloo', 1974, 2),
        Album(4,'Super Trouper', 1980, 2),
        Album(5,'Bossanova', 1990, 1),
        Album(6,'Lover', 2019, 3),
        Album(7,'Folklore', 2020, 3),
        Album(8,'I Put a Spell on You', 1965, 4),
        Album(9,'Baltimore', 1978, 4),
        Album(10,'Here Comes the Sun', 1971, 4),
        Album(11,'Fodder on My Wings', 1982, 4),
        Album(12,'Ring Ring', 1973, 2),
        ]
    

"""
Test to find one album using find() method
"""

def test_find_method_return_one_row(db_connection):
    db_connection.seed("seeds/music_web.sql")

    repo = AlbumRepository(db_connection)

    result = repo.find(11) 

    assert result == Album(11, "Fodder on My Wings", 1982, 4)


"""
Given i call the create() function, it is reflected
in the list of albums, when i call the all() function
"""

def test_creation_of_new_album(db_connection):
    db_connection.seed('seeds/music_web.sql')
    repo = AlbumRepository(db_connection)
    repo.create(Album(None, 'An absurd album', 2023, 4))
    result = repo.all()

    assert result == [
        Album(1,'Doolittle', 1989, 1),
        Album(2,'Surfer Rosa', 1988, 1),
        Album(3,'Waterloo', 1974, 2),
        Album(4,'Super Trouper', 1980, 2),
        Album(5,'Bossanova', 1990, 1),
        Album(6,'Lover', 2019, 3),
        Album(7,'Folklore', 2020, 3),
        Album(8,'I Put a Spell on You', 1965, 4),
        Album(9,'Baltimore', 1978, 4),
        Album(10,'Here Comes the Sun', 1971, 4),
        Album(11,'Fodder on My Wings', 1982, 4),
        Album(12,'Ring Ring', 1973, 2),
        Album(13,'An absurd album', 2023, 4)
    ]


"""
Given i call the delete() function, it deletes specified album,
and returns the updated list when we call all().
"""

def test_deletion_of_specified_album_row(db_connection):
    db_connection.seed('seeds/music_web.sql')
    repo = AlbumRepository(db_connection)
    repo.delete(13)

    result = repo.all()

    assert result == [
        Album(1,'Doolittle', 1989, 1),
        Album(2,'Surfer Rosa', 1988, 1),
        Album(3,'Waterloo', 1974, 2),
        Album(4,'Super Trouper', 1980, 2),
        Album(5,'Bossanova', 1990, 1),
        Album(6,'Lover', 2019, 3),
        Album(7,'Folklore', 2020, 3),
        Album(8,'I Put a Spell on You', 1965, 4),
        Album(9,'Baltimore', 1978, 4),
        Album(10,'Here Comes the Sun', 1971, 4),
        Album(11,'Fodder on My Wings', 1982, 4),
        Album(12,'Ring Ring', 1973, 2),
    ]