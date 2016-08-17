from flask import Flask, flash, redirect, render_template, request, session, abort
from db import *

# Define the application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# IMDB indexing
imdb_index = build_index(app.config['DATA_DIR']+'/join.data')


@app.route("/")
def index():
    return "My IMDB!"


@app.route("/actor/<string:actor_id>")
def get_actor_id(actor_id):
    actor_list = load_data(app.config['DATA_DIR'], 'actor')

    found_actor = actor_list.get(actor_id)

    movie_ref = (imdb_index.get('actor')).get(actor_id)

    return render_template(
        'actor.html', actor_id=actor_id, actor=found_actor, movies=movie_ref)


@app.route("/movie/<string:movie_id>")
def get_movie_id(movie_id):
    movie_list = load_data(app.config['DATA_DIR'], 'movie')

    found_movie = movie_list.get(movie_id)

    actor_ref = (imdb_index.get('movie')).get(movie_id)

    return render_template(
        'movie.html', movie_id=movie_id, movie=found_movie, actors=actor_ref)
