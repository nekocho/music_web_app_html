from playwright.sync_api import Page, expect


# Tests for your routes go here

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

# TEST ALBUMS

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql') # Seed to database for test
    page.goto(f'http://{test_web_address}/albums') # Go to page for test

    divtag = page.locator('div') # Where on the page to test - tags to indicate where Jinja tags are

    expect(divtag).to_have_text([
        "Doolittle",
        "Surfer Rosa"
    ])

def test_find_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql') # Seed to database for test
    page.goto(f'http://{test_web_address}/albums') # Go to page for test


    page.click("text=Doolittle")

    title_element = page.locator(".title")
    expect(title_element).to_have_text("Title: Doolittle")

    release_element = page.locator(".release_year")
    expect(release_element).to_have_text("Released: 1989")

def test_create_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f'http://{test_web_address}/albums')

    page.click("text=Add New Album")

    page.fill("input[name='title']", 'Folklore')
    page.fill("input[name='release_year']", '2020')

    page.click("text=Add Album")

    title_element = page.locator(".title")
    expect(title_element).to_have_text('Title: Folklore')
    release_year = page.locator(".release_year")
    expect(release_year).to_have_text('Released: 2020')

 # TEST ARTISTS

def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f'http://{test_web_address}/artists')

    div_tag = page.locator('div')
    expect(div_tag).to_have_text([
        '\n              Pixies\n            ', 
        '\n              ABBA\n            ', 
        '\n              Taylor Swift\n            ', 
        '\n              Nina Simone\n            '
        ])
# Not too sure why the result is giving so much white space


def test_get_single_artist(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f'http://{test_web_address}/artists')

    page.click('text=Pixies')

    band = page.locator('.band')
    expect(band).to_have_text('Pixies')

    genre = page.locator('.genre')
    expect(genre).to_have_text('Genre: Rock')

def test_create_artist(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f'http://{test_web_address}/artists')

    page.click("text=Add New Artist")

    page.fill("input[name='name']", 'Blink182')
    page.fill("input[name='genre']", 'Punk')

    page.click("text=Add Album")

    title_element = page.locator(".band")
    expect(title_element).to_have_text('Blink182')
    release_year = page.locator(".genre")
    expect(release_year).to_have_text('Genre: Punk')
