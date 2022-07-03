# Болливуд
#
# Индийские фильмы одно время были очень популярны.
# Давайте проверим, как это отразилось на Нетфликсе!
# Нам нужно посчитать, сколько индийских фильмов и сериалов есть на платформе.
# Также считаются фильмы и сериалы которые были сняты совместно с Индией
#
# Пример результата:
#
# фильмы: 50 шт
# сериалы: 10 шт
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
sqlite_query = ("select `type`, COUNT(*) "
                "FROM netflix "
                "WHERE country LIKE '%India%' "
                "GROUP BY `type`")  # TODO измените код
cur.execute(sqlite_query)
result = cur.fetchall()
films = result[0][1]
tv_shows = result[1][1]

# TODO Результат запроса сохраните в переменной result
# для последующей выдачи в требуемом формате
res_ = f"Это тест{result}"
result = f"фильмы: {films} шт\nсериалы: {tv_shows} шт"

con.close()

if __name__ == '__main__':
    print(result, "\n", res_)
