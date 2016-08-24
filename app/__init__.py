from flask import Flask, render_template
from db import *
import datetime

# Define the application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# IMDB indexing
imdb_index = build_index(app.config['DATA_DIR']+'/join.data')


@app.route("/")
def index():
    """
    Index page
    :return:
    """
    return render_template('index.html')


@app.route("/actor")
@app.route("/actor/")
def list_actor():
    """
    List all actors
    :return:
    """
    try:
        actor_list = load_data(app.config['DATA_DIR'], 'actor')

        return render_template(
            'actor_list.html', actors=actor_list)

    except Exception as e:
        return render_template("500.html", error=str(e))


@app.route("/movie")
@app.route("/movie/")
def list_movie():
    """
    List all movies
    :return:
    """
    try:
        movie_list = load_data(app.config['DATA_DIR'], 'movie')

        return render_template(
            'movie_list.html', movies=movie_list)

    except Exception as e:
        return render_template("500.html", error=str(e))


@app.route("/actor/<string:actor_id>")
def get_actor_id(actor_id):
    """
    Inquiry actor by actor id
    :param actor_id:
    :return:
    """
    try:
        data_path = app.config['DATA_DIR'] + 'actor/' + actor_id + '.data'

        actor_id, found_actor = load_data_by_id('actor', data_path)

        movie_ref = (imdb_index.get('actor')).get(actor_id)

        return render_template(
            'actor.html', actor_id=actor_id, actor=found_actor, movies=movie_ref)

    except Exception as e:
        return render_template("500.html", error=str(e))


@app.route("/movie/<string:movie_id>")
def get_movie_id(movie_id):
    """
    Inquiry movie by movie id
    :param movie_id:
    :return:
    """
    try:
        data_path = app.config['DATA_DIR'] + 'movie/' + movie_id + '.data'

        movie_id, found_movie = load_data_by_id('movie', data_path)

        actor_ref = (imdb_index.get('movie')).get(movie_id)

        return render_template(
            'movie.html', movie_id=movie_id, movie=found_movie, actors=actor_ref)

    except Exception as e:
        return render_template("500.html", error=str(e))


@app.template_filter('datetime')
def format_datetime(s):
    """
    Format datetime to mm/dd/yyy
    :param s:
    :return:
    """
    return datetime.datetime.fromtimestamp(float(s)/1000.0).strftime('%m/%d/%Y')


@app.errorhandler(404)
def page_not_found(error):
    """
    Page not found
    :param error:
    :return:
    """
    return render_template('404.html'), 404


