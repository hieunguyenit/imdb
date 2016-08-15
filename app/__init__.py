from flask import Flask, flash, redirect, render_template, request, session, abort
from db import load_data

# Define the application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')


@app.route("/")
def index():
    return "My IMDB!"


###
@app.route("/actor")
def actor():
    return "Actor"


@app.route("/actor/<string:actor_id>")
def get_actor_id(actor_id):
    actor_list = load_data(app.config['DATA_DIR'], 'actor')

    found_actor = actor_list.get(actor_id)

    return render_template(
        'actor.html', actor_id=actor_id, actor=found_actor)


###
@app.route("/movie")
def movie():
    return "Movie"


@app.route("/movie/<string:movie_id>")
def get_movie_id(movie_id):
    movie_list = load_data(app.config['DATA_DIR'], 'movie')

    found_movie = movie_list.get(movie_id)
    
    return render_template(
        'movie.html', movie_id=movie_id, movie=found_movie)
