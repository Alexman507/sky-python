import sqlite3
import prettytable

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("select country as Страна, COUNT(*) as количество "
                "FROM netflix "
                "WHERE Страна is not null "
                "GROUP BY Страна "
                "HAVING количество >= 100 "
                "ORDER BY количество desc ")
cur.execute(sqlite_query)
result = cur.execute(sqlite_query)

# не удаляйте код дальше, он нужен для вывода результата
# запроса в красивом формате

mytable = prettytable.from_db_cursor(result)
mytable.max_width = 30


if __name__ == '__main__':
    print(mytable)
