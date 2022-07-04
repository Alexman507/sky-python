import sqlite3
# 28:15

def get_value_from_db(sql_response):
    with sqlite3.connect("../netflix.db") as connection:
        connection.row_factory = sqlite3.Row

        result = connection.execute(sql_response).fetchall()

        return result


def search_by_title(title):
    sql = f"""
        SELECT * FROM netflix
        WHERE title = {title}
        ORDER BY release_year DESC
        LIMIT 1
        """

    result = get_value_from_db(sql)
    for item in result:
        return dict(item)



