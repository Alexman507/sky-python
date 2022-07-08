import json

from flask import Flask

from lesson14.hw14 import utils

app = Flask(__name__)


@app.get("/movie/<title>")
def page_index(title):
    """Поиск по названию фильма или сериала"""

    result = utils.search_by_title(title)

    return app.response_class(
        response=json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"
    )


@app.get("/movie/<int:year1>/to/<int:year2>/")
def search_date(year1: int, year2: int):
    """Поиск по годам в диапазоне"""

    result = utils.search_between_years(year1, year2)

    return app.response_class(
        response=json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"
    )


@app.get("/rating/<rating>/")
def search_rating_view(rating: str):
    """Поиск по назначению 'Для детей', 'семейный', 'для взрослых' - значения
    'children', 'family', 'adult' соответственно"""

    result = utils.search_rating(rating)

    return app.response_class(
        response=json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"
    )


@app.get("/genre/<genre>/")
def search_genre_view(genre: str):
    """Поиск по жанру"""

    result = utils.search_genre(genre)

    return app.response_class(
        response=json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"
    )


if __name__ == "__main__":
    #
    #

    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
