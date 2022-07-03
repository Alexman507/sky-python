# #Где играет
# Выведите названия всех сериалов('TV Show'), в которых участвует
# Рене Зеллвегер (Renée Zellweger) – победительница
# номинации за лучшую женскую роль
# "WHERE `cast` LIKE '%Renée Zellweger%' "
# Пример результата:
# +-----------+
# |   title   |
# +-----------+
# |  Any show |
# +-----------+
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
sqlite_query = ("SELECT title FROM 'netflix' "
                "WHERE `cast` LIKE '%Renée Zellweger%' "
                "AND type = 'TV Show'")  # TODO измените код запроса
result = cur.execute(sqlite_query)

# не удаляйте код дальше, он нужен для вывода результата
# запроса в красивом формате

mytable = prettytable.from_db_cursor(result)
mytable.max_width = 30

if __name__ == '__main__':
    print(mytable)
