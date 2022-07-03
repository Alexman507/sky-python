import sqlite3
import prettytable

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("select director as Режиссер, COUNT(*) as количество "
                "FROM netflix "
                "WHERE director is not null "
                "GROUP BY `director` "
                "HAVING количество > 10")
cur.execute(sqlite_query)
result = cur.execute(sqlite_query)

# не удаляйте код дальше, он нужен для вывода результата
# запроса в красивом формате

mytable = prettytable.from_db_cursor(result)
mytable.max_width = 30


if __name__ == '__main__':
    print(mytable)
