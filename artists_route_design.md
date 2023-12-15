# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```

Add a route GET /artists/ 
    which returns an HTML page showing details for a single artist.

Add a route GET /artists/ 
    which returns an HTML page with the list of artists. 

This page should contain a link for each artist listed, 
linking to /artists/ where needs to be the corresponding artist id.


# All artist route
GET /artists

# Single artist route
GET /artists/1

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE


# GET /artists
#  Expected response (200 OK):
"""
Pixies
Abba
Taylore Swift
Nina Simone
"""

# GET /artists/1
#  Expected response (200 OK):
"""
Pixies
Genre: Rock
"""


## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /artists

Pixies
Abba
Taylore Swift
Nina Simone
"""
def test_get_artists(web_client, db_connection):
    db_connection.seed('seed/music_library.sql')
    response = web_client.get('/artists')

    tag = page.locator('tag')
    expected(tag).to_have_text([
            'Pixies',
            'Abba',
            'Taylore Swift',
            'Nina Simone',
            ])

def test_get_single_artist(web_client, db_connection):
    db_connection.seed('seed/music_library.sql')
    response = web_client.get('/artists')

    page.click('Pixies')

    band = page.locator('.band')
    expected(band).to_have_text('Pixies')

    genre = page.locator('.genre')
    expected(band).to_have_text('Rock')


```


