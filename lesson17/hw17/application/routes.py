from flask import current_app as app, request
from flask_restx import Api, Namespace, Resource

from lesson17.hw17.application import models, schema
from models import db
from utils import convert_and_register_model

api: Api = app.config['api']
movies_ns: Namespace = api.namespace('movies')
directors_ns: Namespace = api.namespace('directors')
genres_ns: Namespace = api.namespace('genres')

movie_schema = schema.Movie()
movies_schema = schema.Movie(many=True)

director_schema = schema.Director()
directors_schema = schema.Director(many=True)

genre_schema = schema.Genre()
genres_schema = schema.Genre(many=True)

convert_and_register_model('movie', movie_schema)
convert_and_register_model('movies', movies_schema)
convert_and_register_model('director', director_schema)
convert_and_register_model('directors', directors_schema)


@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):
    @movies_ns.response(200, description='Возвращает фильм по его id.', model=api.models['movie'])
    @movies_ns.response(404, description='Фильм не найден.')
    def get(self, movie_id):
        movie = db.session.query(models.Movie).filter(models.Movie.id == movie_id).first()

        if movie is None:
            return None, 404

        return movie_schema.dump(movie), 200

    @movies_ns.response(204, description='Фильм обновлен.')
    @movies_ns.response(404, description='Неправильный id фильма.')
    def put(self, movie_id):
        updated_rows = db.session.query(models.Movie).filter(models.Movie.id == movie_id).update(request.json)
        if updated_rows != 1:
            return None, 400

        db.session.commit()

        return None, 204

    def delete(self, movie_id):
        deleted_rows = db.session.query(models.Movie).filter(models.Movie.id == movie_id).delete()
        if deleted_rows != 1:
            return None, 404

        db.session.commit()
        return None, 200


@movies_ns.route('/')
class MoviesView(Resource):

    @movies_ns.response(200, description='Возвращает все фильмы', model=api.model['movies'])
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

    @movies_ns.expect(api.models['movie'])
    @movies_ns.response(201, description='Фильм успешно создан.')
    def post(self):
        movie = movie_schema.load(request.json)
        db.session.add(models.Movie(**movie))
        db.session.commit()

        return None, 201



@directors_ns.route('/<int:director_id')
class DirectorView(Resource):

    def get(self, director_id):
        director = db.session.query(models.Director).filter(models.Director.id == director_id)

        if director is None:
            return None, 404

        return director_schema.dump(director), 200


@directors_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        directors = db.session.query(models.Director).all()

        return directors_schema.dump(directors), 200


@genres_ns.route('/<int:genre_id')
class GenreView(Resource):

    def get(self, genre_id):
        genre = db.session.query(models.Genre).filter(models.Genre.id == genre_id)

        if genre is None:
            return None, 404

        return genre_schema.dump(genre), 200


@genres_ns.route('/')
class GenresView(Resource):

    def get(self):
        genres = db.session.query(models.Genre).all()

        return genres_schema.dump(genres), 200



