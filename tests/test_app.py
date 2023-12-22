from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
Testing browser GET /albums, displays list of albums
"""

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/html_music_web.sql")
    page.goto(f"http://{test_web_address}/albums")
    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        "Doolittle", 
        "Surfer Rosa",
        "Waterloo",
        "Super Trouper",
        "Bossanova",
        "Lover",
        "Folklore",
        "I Put a Spell on You",
        "Baltimore",
        "Here Comes the Sun",
        "Fodder on My Wings",
        "Ring Ring"
    ])

"""
Testing album main page displays links of albums
"""

def test_visit_all_albums_page_find_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/html_music_web.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Lover'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Absurd Album: Lover")
    release_year_tag = page.locator(".t-release-year")
    expect(release_year_tag).to_have_text("Released: 2019")


def test_visit_album_find_page_go_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/html_music_web.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Lover'")
    page.click("text='Go back to the absurd list'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Absurd Albums")
    

"""
WHEN: I call GET /artists, 
THEN: I can see all artists on the web page
"""

def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/html_music_web.sql")
    page.goto(f"http://{test_web_address}/artists")
    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        'Pixies',
        'ABBA',
        'Taylor Swift',
        'Nina Simone'
    ])


"""
WHEN: i call GET /artists/1
THEN: I can see the specified artist (based on artist.id)
"""

def test_visit_all_artists_find_one_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/html_music_web.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Nina Simone'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Absurd Artist: Nina Simone")
    genre_tag = page.locator(".t-genre")
    expect(genre_tag).to_have_text("Absurd genre: Jazz")


"""
Test to see if we can click a link to go back to artist list
"""

def test_visit_artist_and_go_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/html_music_web.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Nina Simone'")
    page.click("text= Go back to the absurd artist list")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Absurd Artists")

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
