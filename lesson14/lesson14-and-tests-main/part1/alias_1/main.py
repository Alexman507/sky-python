# Свежая подборка
# Попрактикуйтесь с использованием alias в названиях колонок таблицы
# Выведите ТОП 10 фильмов и сериалов которые были добавлены в базу данных самые последние (date_added)
# Название столбцов таблицы должны совпадать с образцом ниже.
#
# Пример результата:
# +---------------------+--------------------------------+---------------------+--------------------+
# |       Название      |            Режиссер            |   Время добавления  | Возрастной рейтинг |
# +---------------------+--------------------------------+---------------------+--------------------+
#
# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актерыактеры
# country — страна производствапроизводства
# date_added — когда добавлендобавлен на Нетфликс
# release_year — когда выпущенвыпущен в прокат
# rating — возрастной рейтингвозрастной рейтинг
# duration — длительностьдлительность
# duration_type — минутыминуты или сезоны
# listed_in — список жанровжанров и подборок
# description — краткое описаниеописание
# -----------------------
import sqlite3
import prettytable

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("SELECT title as Название, director as 'Режиссер' FROM netflix "
                "ORDER BY date_added desc limit 10")  # TODO измените код запроса
result = cur.execute(sqlite_query)

# не удаляйте код дальше, он нужен для вывода результата
# запроса в красивом формате

mytable = prettytable.from_db_cursor(result)
mytable.max_width = 30


if __name__ == '__main__':
    print(mytable)