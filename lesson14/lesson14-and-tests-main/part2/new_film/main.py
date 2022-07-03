# #Самый свежий фильм
# Давайте узнаем, какой фильм или сериал был добавлен в базу самым последним.
#
# Пример результата:
# 100 Meters
#
# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание
# -----------------------
import sqlite3

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("""
    SELECT title FROM netflix
    ORDER BY date_added DESC
    LIMIT 1
    """)  # TODO измените код запроса
cur.execute(sqlite_query)
executed_query = cur.fetchall()

# TODO Результат запроса сохраните в переменной result
# для последующей выдачи в требуемом формате
movie_title = executed_query[0][0]
result = f'{movie_title}'
con.close()

if __name__ == '__main__':
    print(result)
