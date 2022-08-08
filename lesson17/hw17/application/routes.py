from flask import current_app as app, request
from flask_restx import Api, Namespace, Resource

from lesson17.hw17.application import models, schema
from models import db

api: Api = app.config['api']
movies_ns: Namespace = api.namespace('movies')


movies_schema = schema.Movie(many=True)


@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id):
        movie = db.session.query(models.Movie).filter(models.Movie.id == movie_id).first()

        if movie is None:
            return None, 404

        return movies_schema.dump(movie), 200


@movies_ns.route('/')
class MoviesView(Resource):

    def get(self):
        movies = db.session.query(models.Movie)

        args = request.args

        director_id = args.get('director_id')
        if director_id is not None:
            movies = movies.filter(models.Movie.director_id == director_id)

        genre_id = args.get('genre_id')
        if genre_id is not None:
            movies = movies.filter(models.Movie.genre_id == genre_id)

        movies = movies.all()

        return movies_schema.dump(movies), 200

