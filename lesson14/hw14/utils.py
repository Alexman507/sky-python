import json
import sqlite3


def get_value_from_db(sql_response: str) -> list[dict]:
    """Загрузка данных из netflix.db"""

    with sqlite3.connect("../netflix.db") as connection:
        connection.row_factory = sqlite3.Row

        result = connection.execute(sql_response).fetchall()

        return result


def search_by_title(title: str) -> dict:
    """Принимает название фильма/сериала, возвращает все данные по самому новому фильму"""

    sql = f"""
        SELECT * FROM netflix
        WHERE title = {title}
        ORDER BY release_year DESC
        LIMIT 1
        """

    result = get_value_from_db(sql)
    for item in result:
        return dict(item)


def search_between_years(year1: int, year2: int) -> list[dict]:
    """Принимает 2 значение годов, возвращает до 100 результатов название и год выпуска в запрошенном диапазоне"""

    sql = f"""
    SELECT title, release_year
    FROM netflix
    where release_year between '{year1}' and '{year2}'
    limit 100
    """
    result = []

    for item in get_value_from_db(sql):
        result.append(dict(item))

    return result


def search_rating(rating: str) -> list[dict]:
    """Принимает категорию "children", "family", "adult"; возвращает название, возрастной рейтинг, описание"""

    rate_dict = {
        "children": ("G", "G"),
        "family": ("G", "PG", "PG-13"),
        "adult": ("R", "NC-17")
    }

    sql = f"""
       SELECT title, rating, description
       from netflix
       where rating in '{rate_dict.get(rating, ("R", "R"))}'
       """

    result = []

    for item in get_value_from_db(sql):
        result.append(dict(item))

    return result


def search_genre(genre: str) -> list[dict]:
    """Принимает жанр, возвращает 10 результатов новинок"""

    sql = f"""
        SELECT * 
        FROM netflix
        WHERE listed_in like '%{genre}'
        ORDER BY release_year DESC
        LIMIT 10
        """

    result = []

    for item in get_value_from_db(sql):
        result.append(dict(item))

    return result


def get_band_cast(actor1: str, actor2: str) -> list[dict]:
    """
    Принимает имена 2‑х актеров, возвращает тех актеров,
    которые играли с ними больше 2‑х раз
    """

    sql = f"""
    select `cast`
    from netflix
    where `cast` like '%{actor1}%' 
    and `cast` like '%{actor2}%' 
    """

    result = []

    names_dict = {}
    for item in get_value_from_db(sql):
        names = set(dict(item).get('cast').spit(",")) - {actor1, actor2}

        for name in names:
            names_dict[str(name).strip()] += names_dict.get(str(name).strip(), 0) + 1

    for key, value in names_dict.items():
        if value >= 2:
            result.append(key)

    return result


def get_title_description_by_type_year_genre(type_: str, year: int, genre: str) -> str:
    """Принимает тип, год жанр; возвращает названия с описанием"""

    sql = f"""
    select title, description, listed_in
    from netflix
    where type = '%{type_}'
    and release_year = '{year}'
    and listed_in like '%{genre}'
    """

    result = []

    for item in get_value_from_db(sql):
        result.append(dict(item))

    return json.dumps(result, ensure_ascii=False, indent=4)
