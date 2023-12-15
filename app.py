import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.artist_repository import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# ALBUM ROUTES

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums.html', albums=albums)
    
@app.route('/show_album/<int:id>', methods=['GET'])
def find_single_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.find(id)
    return render_template('show_album.html', album=albums)

@app.route('/new_album', methods=['GET'])
def get_new_album():
    return render_template('new_album.html')

@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']

    album = Album(None, title, release_year, artist_id)

    repository.create(album)
    
    return redirect(f'/show_album/{album.id}')

    


# ARTIST ROUTES

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    list_artist = repository.all()
    return render_template('artists.html', artists=list_artist)


@app.route('/show_artist/<int:id>', methods=['GET'])
def find_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    artist = repository.find(id)
    return render_template('/show_artist.html', artist=artist)

@app.route('/new_artist', methods=['GET'])
def get_new_artists():
    return render_template('new_artist.html')

@app.route('/artists', methods=['POST'])
def create_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    name = request.form['name']
    genre = request.form['genre']


    artist = Artist(None, name, genre)

    repository.create(artist)
    
    return redirect(f'/show_artist/{artist.id}')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

