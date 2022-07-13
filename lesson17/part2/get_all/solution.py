from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
app. config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 2}

api = Api(app)
book_ns = api.namespace('books')

books = [
    {
        "id": 1,
        "name": "Harry Potter",
        "year": 2000,
        "author": "Joan Routing"
    },
    {
        "id": 2,
        "name": "Le Comte de Monte-Cristo",
        "year": 1844,
        "author": "Alexandre Dumas"
    }
]


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        return books, 200


if __name__ == '__main__':
    app.run(debug=True)
