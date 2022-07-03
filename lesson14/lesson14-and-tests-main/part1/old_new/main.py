# Старый и новый
# Найдите фильмы, снятые режиссером Guy Ritchie до 2010 года включительно.
# Выведите название и список актеров в каждом фильме.
#
# Пример результата:
# +--------------------------------+--------------------------------+
# |             title              |              cast              |
# +--------------------------------+--------------------------------+
# |  Lock, Stock and Two Smoking   |     Jason Flemyng, Dexter      |
# |            Barrels"            |  Fletcher, Nick Moran, Jason   |
# |                                |  Statham, Steven Mackintosh,   |
# |                                |   Nicholas Rowe, Nick Marcq,   |
# |                                | Charles Forbes, Vinnie Jones,  |
# |                                |          Lenny McLean          |
# +--------------------------------+--------------------------------+
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
import prettytable

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("SELECT `title`, `cast` FROM netflix "
                "WHERE `director` LIKE '%Guy Ritchie%' "
                "AND `release_year` <= '2010'")  # TODO измените код запроса
result = cur.execute(sqlite_query)

# не удаляйте код дальше, он нужен для вывода результата
# запроса в красивом формате

mytable = prettytable.from_db_cursor(result)
mytable.max_width = 30


if __name__ == '__main__':
    print(mytable)
